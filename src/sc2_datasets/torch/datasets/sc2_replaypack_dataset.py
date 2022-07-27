import os
from pathlib import Path
from typing import Any, Callable, Dict, List

from torch.utils.data import Dataset


from sc2_datasets.replay_data.sc2_replay_data import SC2ReplayData
from sc2_datasets.utils.dataset_utils import load_replaypack_information
from sc2_datasets.utils.download_utils import download_and_unpack_replaypack
from sc2_datasets.utils.zip_utils import unpack_zipfile


class SC2ReplaypackDataset(Dataset):
    """
    Represents a Dataset for a single pre-processed replaypack.

    :param replaypack_name: Specifies the name of a replaypack.\
    This can be a name of the tournament or any other arbitrary name.
    :type replaypack_name: str
    :param download_dir: Specifies the directory where the initial archive will be downloaded.
    :type download_dir: str
    :param unpack_dir: Specifies the directory where the archive will be extracted.
    :type unpack_dir: str
    :param url: Specifies the url which will be used to download\
    the .zip archive, defaults to ""
    :type url: str, optional
    :param download: Specifies if the dataset should be downloaded\
    or if it is pre-downloaded and extracted, defaults to False
    :type download: bool, optional
    :param unpack_n_workers: Specifies the number of workers that will\
    be used for unpacking the archive, defaults to 16
    :type unpack_n_workers: int, optional
    :param validator: Specifies a validator for input data, defaults to None
    :type validator: Callable | None, optional
    """

    def __init__(
        self,
        replaypack_name: str,
        unpack_dir: str,
        download_dir: str = "",
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
        self.download_dir = download_dir
        self.unpack_dir = unpack_dir
        # Replaypack unpack directory must exist
        # This is because otherwise we will not be able to load any data:
        if not os.path.isdir(self.unpack_dir):
            raise Exception("Replaypack unpack directory does not exist!")

        self.replaypack_name = replaypack_name
        self.url = url
        self.replaypack_unpack_path = Path(self.unpack_dir, self.replaypack_name)
        self.downloaded_zip_path = Path(
            self.download_dir, self.replaypack_name + ".zip"
        )

        # Downloading the dataset:
        if download:
            # Cannot download the replaypacks if the url is empty
            # or if the download directory does not exist:
            if not url:
                raise Exception("Detected empty URL! Cannot download a replaypack!")

            download_and_unpack_replaypack(
                replaypack_download_dir=self.download_dir,
                replaypack_unpack_dir=self.unpack_dir,
                replaypack_name=self.replaypack_name,
                url=self.url,
            )

        # If the dataset is not unpacked, then look for it in the download folder.
        # If it is there then unpack it and resume:
        if not self.replaypack_unpack_path.exists() and not download:
            if not self.downloaded_zip_path.exists():
                raise Exception(
                    "Dataset was not unpacked nor downloaded!\
                                Please make sure that the replaypack exists!"
                )
            self.replaypack_unpack_path = Path(
                unpack_zipfile(
                    destination_dir=self.unpack_dir,
                    subdir=self.replaypack_name,
                    zip_path=self.downloaded_zip_path.as_posix(),
                    n_workers=self.unpack_n_workers,
                )
            )

        # Loading the dataset information, additional replaypack information is kept:
        (
            data_path,
            self._replaypack_main_log_obj_list,
            self._replaypack_processed_failed,
            self._replaypack_dir_mapping,
            self._replaypack_summary,
        ) = load_replaypack_information(
            replaypack_name=self.replaypack_name,
            replaypack_path=self.replaypack_unpack_path.as_posix(),
            unpack_n_workers=self.unpack_n_workers,
        )

        # Getting the paths to the files that consist of the dataset,
        # These will be used for validation at later step:

        # TODO: This produces an ERROR!
        all_files = [Path(data_path, file).as_posix() for file in os.listdir(data_path)]

        # Validating files:
        self.skip_files = set()
        if validator is not None:
            self.skip_files = validator(all_files)

        # Loading all of the files using,
        # Skipping the ones that were returned from validator:
        self.list_of_files = [
            sc2_replay_file_info
            for sc2_replay_file_info in all_files
            if sc2_replay_file_info not in self.skip_files
        ]
        self.len = len(self.list_of_files)

    def __len__(self) -> int:
        return self.len

    def __getitem__(self, index: int) -> SC2ReplayData:
        """
        Exposes logic of getting a single parsed item from the replaypack.

        :param index: Specifies the index of a file that will be parsed and loaded into memory,
        :type index: int
        :return: Returns a parsed SC2ReplayData.
        :rtype: SC2ReplayData
        """
        # Returning a replay serialized into Python class to assure the ease of use:

        replay_data = SC2ReplayData.from_file(replay_filepath=self.list_of_files[index])
        if self.transform:
            return self.transform(replay_data)
        return replay_data

    @property
    def replaypack_summary(self) -> Dict[str, Any]:
        return self._replaypack_summary

    @property
    def replaypack_dir_mapping(self) -> Dict[str, str]:
        return self._replaypack_dir_mapping

    @property
    def replaypack_processed_failed(self) -> Dict[str, List[str]]:
        return self._replaypack_processed_failed
