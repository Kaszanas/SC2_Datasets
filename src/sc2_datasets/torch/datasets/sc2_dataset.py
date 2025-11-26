import logging
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any, Callable

from torch.utils.data import Dataset
from tqdm import tqdm

from sc2_datasets.replay_data.sc2_replay_data import SC2ReplayData
from sc2_datasets.torch.datasets.sc2_replaypack_dataset import SC2ReplaypackDataset
from sc2_datasets.utils.download_utils import download_replaypack
from sc2_datasets.utils.json_utils import (
    get_json_offsets,
    get_object_at_index,
)
from sc2_datasets.utils.zip_utils import unpack_zipfile


class SC2DatasetSingleJSON(Dataset):
    def __init__(
        self,
        dataset_name: str,
        unpack_dir: Path | str,
        download: bool = True,
        download_dir: Path | str | None = None,
        dataset_url: str = "",
        transform: Callable | None = None,
        validator: Callable | None = None,
    ):
        if not dataset_name:
            raise Exception("Dataset name cannot be empty!")

        if download:
            if not dataset_url:
                raise Exception("Dataset URL cannot be empty if download is requested!")
            if not download_dir:
                raise Exception(
                    "Download directory cannot be None if download is requested!"
                )

        # PyTorch fields:
        self.transform = transform

        # Custom fields:
        self.download = download
        self.download_dir = None
        self.maybe_downloaded_zip_path = None
        if self.download:
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

        self.unpack_dir = (
            unpack_dir if isinstance(unpack_dir, Path) else Path(unpack_dir).resolve()
        )

        if not self.unpack_dir.exists():
            self.unpack_dir.mkdir(parents=True, exist_ok=True)

        if not self.unpack_dir.is_dir():
            raise Exception("Replaypack unpack directory is not a directory!")

        self.dataset_name = dataset_name
        self.dataset_url = dataset_url

        self.validator = validator

        # TODO: This might need to change based on the specific
        # dataset differences, it might not be a skip_files, but skip indices?
        self.skip_files: dict[str, set[str]] = {}

        # We have received an URL for the dataset
        # and it migth not have been downloaded:
        self.len = 0
        self.replaypacks: list[SC2ReplaypackDataset] = []

        # Download the dataset if needed:
        self.was_downloaded = False
        self.unpack_path = Path(self.unpack_dir, self.dataset_name).resolve()

        if self.download and not self.was_downloaded:
            if not self.dataset_url:
                raise Exception("Detected empty URL! Cannot download a replaypack!")

            self.maybe_downloaded_zip_path = download_replaypack(
                destination_dir=self.download_dir,
                replaypack_name=self.dataset_name,
                url=self.dataset_url,
            )
            if not self.maybe_downloaded_zip_path.exists():
                raise Exception("Dataset download failed!")

        dataset_unpack_path_exists = self.unpack_path.exists()

        if not dataset_unpack_path_exists:
            logging.info("Dataset was not unpacked yet, unpacking now...")
            if not self.maybe_downloaded_zip_path:
                raise Exception("Download zip path is not set! Cannot unpack dataset!")

            if not self.maybe_downloaded_zip_path.exists():
                raise Exception(
                    "Cannot unpack dataset without either downloading it or having download directory set!"
                )

            # The zip should contain a single JSON file. No need for more workers:
            self.unpack_path = unpack_zipfile(
                destination_dir=self.unpack_dir,
                subdir=self.dataset_name,
                zip_path=self.maybe_downloaded_zip_path,
                n_workers=1,
            )

        # If we reached this point, the dataset was downloaded for sure:
        self.was_downloaded = True

        # Parsing the dataset to counte the number of entries:
        self.dataset_path = Path(
            self.unpack_path, self.dataset_name + ".json"
        ).resolve()

        json_offsets_filepath = Path(
            self.unpack_path, self.dataset_name + "_offsets.json"
        ).resolve()

        self.json_offsets = get_json_offsets(
            json_filepath=self.dataset_path,
            offsets_filepath=json_offsets_filepath,
        )

        if self.validator:
            logging.warning(
                "Validation logic for SC2DatasetSingleJSON is not yet implemented!"
            )

        self.len = len(self.json_offsets)
        self.file__handle = None

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
            self.file_handle = self.dataset_path.open(mode="r", encoding="utf-8")

        python_obj = get_object_at_index(
            json_filepath=self.unpack_path,
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


class SC2Dataset(Dataset):
    """
    Inherits from PyTorch Dataset and ensures that the dataset for SC2EGSet is downloaded.

    Parameters
    ----------
    names_urls : list[tuple[str, str]]
        Specifies the URL of the dataset which will be used to download the files.
    unpack_dir : Path | str
        Specifies the path of a directory where the dataset files will be unpacked.
    download_dir : Path | str
        Specifies the path of a directory where the dataset files will be downloaded.
    unpack_n_workers : int, optional
        Specifies the number of workers that will be used for unpacking the archive, defaults to 16.
    transform : Func[SC2ReplayData, T]
        PyTorch transform function that takes SC2ReplayData and returns something.
    validator : Callable | None, optional
        Specifies the validation option for fetched data, defaults to None.
    """

    def __init__(
        self,
        names_urls: list[tuple[str, str]],
        unpack_dir: Path | str = Path("./data/unpack").resolve(),
        download_dir: Path | str = Path("./data/download").resolve(),
        download: bool = True,
        unpack_n_workers: int = 16,
        transform: Callable | None = None,
        validator: Callable | None = None,
    ):
        # PyTorch fields:
        self.transform = transform

        # Custom fields:
        self.download_dir = (
            download_dir
            if isinstance(download_dir, Path)
            else Path(download_dir).resolve()
        )
        self.unpack_dir = (
            unpack_dir if isinstance(unpack_dir, Path) else Path(unpack_dir).resolve()
        )
        self.names_urls = names_urls
        self.download = download
        self.unpack_n_workers = unpack_n_workers
        self.validator = validator

        self.skip_files: dict[str, set[str]] = {}

        # We have received an URL for the dataset
        # and it migth not have been downloaded:
        self.len = 0
        self.ensure_downloaded()

    def ensure_downloaded(self):
        """
        Ensures that the dataset was downloaded before accessing the __len__ or __getitem__ methods.
        """

        list_of_arguments = []
        for replaypack_name, url in self.names_urls:
            list_of_arguments.append(
                {
                    "replaypack_name": replaypack_name,
                    "unpack_dir": self.unpack_dir,
                    "download_dir": self.download_dir,
                    "url": url,
                    "download": self.download,
                    "unpack_n_workers": self.unpack_n_workers,
                    "validator": self.validator,
                }
            )

        # NOTE: The parameter of max_workers may be customizable,
        # Be wary that this operation is downloading the dataset,
        # don't DDOS people with this:
        with ThreadPoolExecutor(
            max_workers=3,
            initializer=tqdm.set_lock,
            initargs=(tqdm.get_lock(),),
        ) as executor:
            self.replaypacks = list(
                executor.map(
                    SC2ReplaypackDataset.from_args,
                    list_of_arguments,
                )
            )

        for replaypack in self.replaypacks:
            self.len += len(replaypack)

    def __len__(self) -> int:
        """
        Returns the number of items that are within the dataset
        """
        return self.len

    def __getitem__(self, index: Any) -> tuple[Any, Any] | SC2ReplayData:
        """
        Exposes logic of getting a single parsed item by using dataset[index].

        Parameters
        ----------
        index : Any
            Specifies the index of an item that should be retrieved.

        Raises
        ------
        IndexError
            To support negative indexing, if the index is less than zero twice,\
            IndexError is raised.
        IndexError
            If the index is greater than length of the dataset, IndexError is raised.

        Returns
        -------
        tuple[Any, Any] | SC2ReplayData
            Returns a parsed SC2ReplayData from an underlying SC2ReplaypackDataset,
            or a result of a transform that was passed to the dataset.
        """

        # If the index is negative, treat it as if expressed from the back of the sequence.
        # For example, if index is -1 and lenght is 10,
        # it means we are looking for the last element, which is at index 10 + (-1) = 9
        if index < 0:
            index = self.len + index

        if index < 0:
            raise IndexError(f"Computed index {index} is still less than zero!")

        if index > self.len:
            raise IndexError(f"Computed index {index} is greater than {self.len}!")

        for replaypack in self.replaypacks:
            if index < len(replaypack):
                if self.transform:
                    return self.transform(replaypack[index])
                return replaypack[index]
            else:
                index -= len(replaypack)
