from __future__ import annotations

import logging
from pathlib import Path
from typing import Any, Callable

from torch.utils.data import Dataset

from sc2_datasets.replay_data.sc2_replay_data import SC2ReplayData
from sc2_datasets.utils.download_utils import download_replaypack
from sc2_datasets.utils.json_utils import (
    get_json_offsets,
    get_object_at_index,
)
from sc2_datasets.utils.zip_utils import unpack_zipfile


class SC2DatasetSingleJSON(Dataset):
    def __init__(
        self,
        dataset_name: str | None = None,
        unpack_dir: Path | str | None = None,
        json_path: Path | str | None = None,
        download: bool = True,
        download_dir: Path | str | None = None,
        dataset_url: str = "",
        transform: Callable | None = None,
        validator: Callable | None = None,
    ):
        if not dataset_name:
            raise Exception("Dataset name cannot be empty!")

        # PyTorch fields:
        self.transform = transform

        # Custom fields:
        # Set by the logic below:
        self.dataset_name: str | None = None

        self.download_dir: Path | None = None
        self.maybe_downloaded_zip_path: Path | None = None

        self.was_downloaded: bool | None = None

        self.unpack_dir: Path | None = None
        self.unpack_path: Path | None = None
        self.dataset_path: Path | None = None

        if json_path:
            self.dataset_name = json_path.stem
            self.dataset_path = (
                json_path if isinstance(json_path, Path) else Path(json_path).resolve()
            )

            if not self.dataset_path.exists():
                raise Exception(
                    f"Provided JSON path {self.dataset_path} does not exist!"
                )

            self.unpack_path = self.dataset_path.parent.resolve()
        else:
            # Download and unpack logic is triggered only if no json_path is provided:
            self.download_and_unpack(
                dataset_name=dataset_name,
                download=download,
                download_dir=download_dir,
                unpack_dir=unpack_dir,
                dataset_url=dataset_url,
            )

        # Indexing logic for faster file lookup:
        self.json_offsets = self.calculate_offsets(
            unpack_path=self.unpack_path,
            dataset_name=self.dataset_name,
        )

        # Begin validation logic:
        self.validator = validator

        # TODO: This might need to change based on the specific
        # dataset differences, it might not be a skip_files, but skip indices?
        self.skip_files: dict[str, set[str]] = {}

        if self.validator:
            logging.warning(
                "Validation logic for SC2DatasetSingleJSON is not yet implemented!"
            )

        self.len = len(self.json_offsets)
        self.file_handle = None

    def __check_download_args(
        self,
        dataset_name: str,
        download: bool,
        download_dir: Path,
        dataset_url: str,
    ):
        """
        Checks the arguments for downloading the dataset.

        Parameters
        ----------
        dataset_name : str
            Name of the dataset to be downloaded.
        download : bool
            Whether to download the dataset or not.
        download_dir : Path
            Directory where the dataset will be downloaded.
        dataset_url : str
            URL from which the dataset will be downloaded.

        Raises
        ------
        Exception
            If the dataset URL is empty when download is requested.
        Exception
            If the download directory is None when download is requested.
        Exception
            If the dataset name is empty when download is requested.
        """

        # No need to check the download arguments if the download is not requested:
        if not download:
            return

        if not dataset_url:
            raise Exception("Dataset URL cannot be empty if download is requested!")
        if not download_dir:
            raise Exception(
                "Download directory cannot be None if download is requested!"
            )
        if not dataset_name:
            raise Exception("Dataset name cannot be empty for downloading!")

    def __download(
        self,
        dataset_name: str,
        download: bool,
        download_dir: Path,
        dataset_url: str,
    ):
        self.__check_download_args(
            dataset_name=dataset_name,
            download=download,
            download_dir=download_dir,
            dataset_url=dataset_url,
        )

        # Custom fields:
        self.dataset_name = dataset_name

        if download:
            self.download_dir = (
                download_dir
                if isinstance(download_dir, Path)
                else Path(download_dir).resolve()
            )
            if not self.download_dir.exists():
                self.download_dir.mkdir(parents=True, exist_ok=True)

            self.maybe_downloaded_zip_path = Path(
                self.download_dir, self.dataset_name + ".zip"
            ).resolve()

            maybe_downloaded_zip_path = download_replaypack(
                destination_dir=self.download_dir,
                replaypack_name=self.dataset_name,
                replaypack_url=self.dataset_url,
            )
            if not self.maybe_downloaded_zip_path.exists():
                raise Exception("Dataset download failed!")

            # If we reached this point, the dataset was downloaded for sure:
            self.was_downloaded = True

        if not self.maybe_downloaded_zip_path and not download:
            raise Exception(
                f"Dataset zip file {self.maybe_downloaded_zip_path} does not exist!"
            )

        return maybe_downloaded_zip_path

    # TODO: This logic could be moved to use Pydantic validators for cleaner code:
    def __check_unpack_args(
        self,
        dataset_name: str | None,
        unpack_dir: Path | None,
    ):
        """
        Checks the arguments for unpacking the dataset.

        Parameters
        ----------
        dataset_name : str
            Name of the dataset to be unpacked.
        unpack_dir : Path
            Directory where the dataset will be unpacked.

        Raises
        ------
        Exception
            If the dataset name is empty.
        Exception
            If the unpack directory is None.
        """

        if not dataset_name:
            raise Exception("Dataset name cannot be empty for unpacking!")
        if not unpack_dir:
            raise Exception("Unpack directory cannot be None for unpacking!")

    def __unpack(self, dataset_name: str, unpack_dir: Path):
        """
        Unpacks the dataset if it was not unpacked previously.

        Parameters
        ----------
        dataset_name : str
            Name of the dataset, this will be used for naming the unpacked
            directory.
        unpack_dir : Path
            Directory where the dataset will be unpacked.

        Raises
        ------
        Exception
            If the unpack directory is not a directory.
        """

        self.__check_unpack_args(
            dataset_name=dataset_name,
            unpack_dir=unpack_dir,
        )

        self.unpack_dir = (
            unpack_dir if isinstance(unpack_dir, Path) else Path(unpack_dir).resolve()
        )

        if not self.unpack_dir.exists():
            self.unpack_dir.mkdir(parents=True, exist_ok=True)

        if not unpack_dir.is_dir():
            raise Exception("Unpack directory is not a directory!")

        self.unpack_path = Path(self.unpack_dir, self.dataset_name).resolve()

        # The zip should contain a single JSON file. No need for more workers:
        self.unpack_path = unpack_zipfile(
            destination_dir=self.unpack_dir,
            subdir="",
            zip_path=self.maybe_downloaded_zip_path,
            n_workers=1,
        )

        # Parsing the dataset to counte the number of entries:
        self.dataset_path = Path(
            self.unpack_path,
            self.dataset_name,
            self.dataset_name + ".json",
        ).resolve()

    def download_and_unpack(
        self,
        dataset_name: str | None,
        download: bool,
        download_dir: Path | str | None,
        unpack_dir: Path | str | None,
        dataset_url: str | None,
    ):
        """
        Downloads and unpacks the dataset if needed.

        Parameters
        ----------
        dataset_name : str | None
            Name of the dataset, this will be used for naming the downloaded
            zip file and by extension the unpacked directory.
        download : bool
            Whether to download the dataset or not.
        download_dir : Path | str | None
            Directory where the dataset will be downloaded.
        unpack_dir : Path | str | None
            Directory where the dataset will be unpacked.
        dataset_url : str | None
            URL from which the dataset will be downloaded.
        """

        self.__download(
            dataset_name=dataset_name,
            download=download,
            download_dir=download_dir,
            dataset_url=dataset_url,
        )

        self.__unpack(
            dataset_name=dataset_name,
            unpack_dir=unpack_dir,
        )

    def calculate_offsets(self, unpack_path: Path, dataset_name: Path) -> list[int]:
        """
        Calculates JSON offsets for fast indexing of dataset objects.

        Parameters
        ----------
        unpack_path : Path
            Path where the dataset is unpacked.
        dataset_name : Path
            Name of the dataset.

        Returns
        -------
        list[int]
            List of offsets for each object in the JSON dataset.
        """

        json_offsets_filepath = Path(
            unpack_path, dataset_name + "_offsets.json"
        ).resolve()

        json_offsets = get_json_offsets(
            json_filepath=self.dataset_path,
            offsets_filepath=json_offsets_filepath,
        )

        return json_offsets

    def __len__(self) -> int:
        return self.len

    def __getitem__(self, index: Any) -> tuple[Any, Any] | SC2ReplayData:
        # If the index is negative, treat it as if expressed from the back of the sequence.

        # If the index is negative, treat it as if expressed from the back of the sequence.
        # For example, if index is -1 and lenght is 10,
        # it means we are looking for the last element, which is at index 10 + (-1) = 9
        if index < 0:
            index = self.len + index

        if index < 0:
            raise IndexError(f"Computed index {index} is still less than zero!")

        if index > self.len:
            raise IndexError(f"Computed index {index} is greater than {self.len}!")

        if not self.file_handle:
            self.file_handle = self.dataset_path.open(mode="rb")

        python_obj = get_object_at_index(
            file_handle=self.file_handle,
            offsets=self.json_offsets,
            index=index,
        )

        single_json_filename = python_obj.get("filename", f"index_{index}.json")
        replay_data = SC2ReplayData.from_dict(
            loaded_data=python_obj,
            replay_filepath=single_json_filename,
        )

        if self.transform:
            return self.transform(replay_data)

        return replay_data

    def __del__(self):
        if hasattr(self, "file_handle") and self.file_handle:
            self.file_handle.close()

    @staticmethod
    def from_json_path(
        json_path: Path | str,
        validator: Callable | None = None,
        transform: Callable | None = None,
    ) -> SC2DatasetSingleJSON:
        """
        Creates a SC2DatasetSingleJSON object directly from a JSON path,
        skipping download and unpack steps.

        Parameters
        ----------
        json_path : Path | str
            Path to the JSON file with the correct dataset structure.
        validator : Callable | None, optional
            Validator to use when deciding about objects within the dataset, by default None
        transform : Callable | None, optional
            Transform for each of the SC2ReplayData objects,
            a function taking SC2ReplayData and returning
            the transformed object, by default None

        Returns
        -------
        SC2DatasetSingleJSON
            Returns a SC2DatasetSingleJSON object initialized with the provided JSON path.
        """

        return SC2DatasetSingleJSON(
            json_path=json_path,
            dataset_name=None,  # Inferred from the filename of the JSON
            download=False,  # json_path is provided, no need to download
            unpack_dir=None,  # json_path is provided, no need to unpack
            download_dir=None,  # json_path is provided, no need to download
            dataset_url="",  # json_path is provided, no need to download
            validator=validator,
            transform=transform,
        )
