from typing import Any, List, Tuple
from torch.utils.data._typing import T_co
from torch.utils.data import Dataset
from src.dataset.available_replaypacks import AVAILABLE_REPLAYPACKS

from src.dataset.sc2_replay_data import SC2ReplaypackData
from src.dataset.sc2_replaypack_dataset import SC2ReplaypackDataset


class SC2EGSetDataset(Dataset):
    """
    Inherits from PyTorch Dataset and ensures that the dataset for SC2EGSet is downloaded.

    :param dataset_unpack_dir: Specifies the path of a directory where the dataset files will be unpacked.
    :type dataset_unpack_dir: str
    :param dataset_download_dir: Specifies the path of a directory where the dataset files will be downloaded.
    :type dataset_download_dir: str
    :param urls: Specifies the URL of the dataset which will be used to download the files.
    :type urls: List[str]
    :param transform: PyTorch transform.
    :type transform: ??????????
    """

    def __init__(
        self,
        dataset_unpack_dir: str = "./data/unpack",
        dataset_download_dir: str = "./data/download",
        urls: List[
            Tuple[str, str]
        ] = AVAILABLE_REPLAYPACKS,  # This should probably be hardcoded! After all I want this to be a specific dataset.
        transform=None,
    ):
        self.dataset_download_dir = dataset_download_dir
        self.dataset_unpack_dir = dataset_unpack_dir
        self.transform = transform
        self.list_of_urls = urls  # TODO: maybe rename to self.urls

        # We have received an URL for the dataset
        # and it migth not have been downloaded:
        self.ensure_downloaded()

    def ensure_downloaded(self):
        """
        Ensures that the dataset was downloaded before accessing the __len__ or __getitem__ methods.
        """

        self.replaypacks = []
        self.len = 0

        for url in self.urls:
            replaypack = SC2ReplaypackData(self.dataset_download_dir + "/aaa/")
            self.replaypacks.append(replaypack)
            self.len += len(replaypack)

    def __len__(self) -> int:
        """
        Returns the number of items that are within the dataset
        """
        # TODO: Implement how to calculate the len of the dataset.
        # In the case of SC2EGSet this will be the number of files.

        # Get len of list of files from SC2ReplaypackData class
        return self.len

    def __getitem__(self, index: Any) -> T_co:
        """
        Implements the dataset[index] acquisition of data.

        :param index: Specifies the index of an item that should be retrieved.
        :type index: Any
        :return: Returns an item from the dataset.
        :rtype: T_co
        """
        # TODO: Implement how to get a single item from the dataset!
        # Most likely this will have to load the JSON file.

        # load and return the specific file that corresponds to the index on the list of files

        # This should return contents of a .json file?
        # Or maybe different IterableDatasets that coincide with the Lists that .json holds?

        # TODO: Get a specific SC2ReplayData from SC2ReplaypackData

        # If the index is negative, treat it as if expressed from the back of the sequence.
        # For example, if index is -1 and lenght is 10, it means we are looking for the last element, which is at index 10 + (-1) = 9
        if index < 0:
            index = self.len + index

        if index < 0:
            raise IndexError(f"Computed index {index} is still less than zero!")

        if index > self.len:
            raise IndexError(f"Computed index {index} is greater than {self.len}!")

        for replaypack in self.replaypacks:
            if index < len(replaypack):
                return replaypack[index]
            else:
                index -= len(replaypack)

    def load_files(self):

        # TODO: Lazily load SC2ReplayData so that it holds the paths
        # To the .json files holding different info.

        # Load to the list of files
        # Add the files to the list of files.

        pass
