from typing import Any, List, Tuple
from torch.utils.data._typing import T_co
from torch.utils.data import Dataset
from src.dataset.available_replaypacks import AVAILABLE_REPLAYPACKS
from src.dataset.sc2_replay_data import SC2ReplayData

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
        names_urls: List[
            Tuple[str, str]
        ] = AVAILABLE_REPLAYPACKS,  # This should probably be hardcoded! After all I want this to be a specific dataset.
        download: bool = True,
        transform=None,
    ):
        self.dataset_download_dir = dataset_download_dir
        self.dataset_unpack_dir = dataset_unpack_dir
        # TODO: What to do with the transform?
        # I don't think that it will be used
        self.transform = transform
        self.names_urls = names_urls
        self.download = download

        # We have received an URL for the dataset
        # and it migth not have been downloaded:
        self.ensure_downloaded()

    def ensure_downloaded(self):
        """
        Ensures that the dataset was downloaded before accessing the __len__ or __getitem__ methods.
        """

        self.replaypacks = []
        self.len = 0

        for replaypack_name, url in self.names_urls:
            replaypack = SC2ReplaypackDataset(
                replaypack_name=replaypack_name,
                replaypack_download_dir=self.dataset_download_dir,
                replaypack_unpack_dir=self.dataset_unpack_dir,
                url=url,
                download=self.download,
            )
            self.replaypacks.append(replaypack)
            self.len += len(replaypack)

    def __len__(self) -> int:
        """
        Returns the number of items that are within the dataset
        """
        # TODO: Verify that this works
        return self.len

    def __getitem__(self, index: Any) -> SC2ReplayData:
        """
        Exposes logic of getting a single parsed item by using dataset[index].

        :param index: Specifies the index of an item that should be retrieved.
        :type index: Any
        :return: Returns a parsed SC2ReplayData from an underlying SC2ReplaypackDataset.
        :rtype: SC2ReplayData
        """

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
