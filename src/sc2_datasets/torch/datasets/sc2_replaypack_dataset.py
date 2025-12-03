from pathlib import Path
from typing import Any, Callable

from torch.utils.data import Dataset

from sc2_datasets.replay_data.sc2_replay_data import SC2ReplayData
from sc2_datasets.utils.dataset_utils import load_replaypack_information
from sc2_datasets.utils.download_utils import (
    download_replaypack,
)
from sc2_datasets.utils.zip_utils import unpack_zipfile


class SC2ReplaypackDatasetSingleJSON(Dataset):
    pass


class SC2ReplaypackDataset(Dataset):
    """
    Represents a Dataset for a single pre-processed replaypack.

    Parameters
    ----------
    replaypack_name : str
        Specifies the name of a replaypack.\
        This can be a name of the tournament or any other arbitrary name.
    unpack_dir : Path
        Specifies the directory where the archive will be extracted.
    download_dir : Path
        Specifies the directory where the initial archive will be downloaded.
    url : str, optional
        Specifies the URL which will be used to download the .zip archive,\
        defaults to "".
    download : bool, optional
        Specifies if the dataset should be downloaded or if it is pre-downloaded\
        and extracted, defaults to False.
    unpack_n_workers : int, optional
        Specifies the number of workers that will be used for unpacking the archive,\
        defaults to 16.
    validator : Callable | dict, optional
        Specifies a validator for input data, defaults to None.
    """

    def __init__(
        self,
        replaypack_name: str,
        unpack_dir: Path | str,
        download_dir: Path | str = Path(""),
        url: str = "",
        download: bool = False,
        unpack_n_workers: int = 16,
        transform: None | Callable = None,
        validator: None | Callable = None,
    ):
        # PyTorch fields:
        self.transform = transform

        # Custom fields:
        self.unpack_n_workers = unpack_n_workers
        self.download_dir = (
            download_dir
            if isinstance(download_dir, Path)
            else Path(download_dir).resolve()
        )

        # The path to the downloaded zip file, this will be either downloaded
        # and set to the path of the downloaded file, or detected if the file
        # was already downloaded and set to the path of the file:
        self.maybe_downloaded_zip_path = Path(
            download_dir, replaypack_name + ".zip"
        ).resolve()
        self.was_downloaded = False
        if self.maybe_downloaded_zip_path.exists():
            self.was_downloaded = True

        # Replaypack download directory must exist, we create it if it does not exist:
        if not self.download_dir.exists():
            self.download_dir.mkdir(parents=True, exist_ok=True)

        self.unpack_dir = (
            unpack_dir if isinstance(unpack_dir, Path) else Path(unpack_dir).resolve()
        )
        # Replaypack unpack directory must exist, we create it if it does not exist:
        # This is because otherwise we will not be able to load any data:
        if not self.unpack_dir.exists():
            self.unpack_dir.mkdir(parents=True, exist_ok=True)

        if not self.unpack_dir.is_dir():
            raise Exception("Replaypack unpack directory is not a directory!")

        self.replaypack_name = replaypack_name
        self.url = url
        self.replaypack_unpack_path = Path(
            self.unpack_dir,
            self.replaypack_name,
        ).resolve()
        self.maybe_downloaded_zip_path = Path(
            self.download_dir,
            self.replaypack_name + ".zip",
        ).resolve()

        # Downloading the replaypack dataset only if it was not downloaded yet:
        if download and not self.was_downloaded:
            # Cannot download the replaypacks if the url is empty
            # or if the download directory does not exist:
            if not url:
                raise Exception("Detected empty URL! Cannot download a replaypack!")

            self.maybe_downloaded_zip_path = download_replaypack(
                destination_dir=self.download_dir,
                replaypack_name=self.replaypack_name,
                replaypack_url=self.url,
            )
            if not self.maybe_downloaded_zip_path:
                raise Exception("Replaypack download failed!")

        # If the dataset is not unpacked, then look for it in the download folder.
        # If it is there then unpack it and resume:
        replaypack_unpack_path_exists = self.replaypack_unpack_path.exists()
        downloaded_zip_path_exists = self.maybe_downloaded_zip_path.exists()

        # Unpack the top level zip file, it contains nested .zip file with the actual data,
        # the nested data is downloaded in the next step:
        if not replaypack_unpack_path_exists:
            if not downloaded_zip_path_exists:
                raise Exception(
                    "Dataset was not unpacked nor downloaded!\
                                Please make sure that the replaypack exists!"
                )
            self.replaypack_unpack_path = Path(
                unpack_zipfile(
                    destination_dir=self.unpack_dir,
                    subdir=self.replaypack_name,
                    zip_path=self.maybe_downloaded_zip_path,
                    n_workers=self.unpack_n_workers,
                )
            )

        # Unpack the nested .zip file with the actual .json files, replaypack data:
        data_zipfile = Path(
            self.replaypack_unpack_path,
            self.replaypack_name + "_data.zip",
        ).resolve()
        if not data_zipfile.exists():
            raise Exception(
                f"Data zipfile {str(data_zipfile)} does not exist! Please verify if the replaypack was downloaded and unpacked correctly!"
            )
        data_path = unpack_zipfile(
            destination_dir=self.replaypack_unpack_path,
            subdir=self.replaypack_name + "_data",
            zip_path=data_zipfile,
            n_workers=self.unpack_n_workers,
        )

        # Loading the dataset information, additional replaypack metadata is kept:
        (
            self._replaypack_main_log_obj_list,
            self._replaypack_processed_failed,
            self._replaypack_dir_mapping,
            self._replaypack_summary,
        ) = load_replaypack_information(
            replaypack_path=self.replaypack_unpack_path,
        )

        # Getting the paths to the files that consist of the dataset,
        # These will be used for validation at later step:
        all_files: list[Path] = []
        for file in data_path.iterdir():
            all_files.append(Path(data_path, file))

        # Validating files:
        self.skip_files = set()
        if validator is not None:
            self.skip_files = validator(all_files)

        # Loading all of the files using,
        # Skipping the ones that were returned from validator:
        self.list_of_files = []
        for sc2_replay_file_info in all_files:
            if sc2_replay_file_info in self.skip_files:
                continue
            self.list_of_files.append(sc2_replay_file_info)

        self.len = len(self.list_of_files)

    def __len__(self) -> int:
        return self.len

    def __getitem__(self, index: int) -> SC2ReplayData:
        """
        Exposes logic of getting a single parsed item from the replaypack.

        Parameters
        ----------
        index : int
            Specifies the index of a file that will be parsed and loaded into memory.

        Returns
        -------
        SC2ReplayData
            Returns a parsed SC2ReplayData representation of a StarCraft 2 replay.
        """
        # Returning a replay serialized into Python class to assure the ease of use:

        replay_data = SC2ReplayData.from_file(
            replay_filepath=self.list_of_files[index],
        )
        if self.transform:
            return self.transform(replay_data)
        return replay_data

    @staticmethod
    def from_args(args: dict[str, Any]) -> "SC2ReplaypackDataset":
        """
        Creates a SC2ReplaypackDataset object from a dictionary of arguments.

        Parameters
        ----------
        args : dict[str, Any]
            Specifies the dictionary of arguments that will be used to initialize the dataset.

        Returns
        -------
        SC2ReplaypackDataset
            Returns a SC2ReplaypackDataset object initialized with the provided arguments.
        """
        return SC2ReplaypackDataset(**args)

    @property
    def replaypack_summary(self) -> dict[str, Any]:
        return self._replaypack_summary

    @property
    def replaypack_dir_mapping(self) -> dict[str, str]:
        return self._replaypack_dir_mapping

    @property
    def replaypack_processed_failed(self) -> dict[str, list[str]]:
        return self._replaypack_processed_failed
