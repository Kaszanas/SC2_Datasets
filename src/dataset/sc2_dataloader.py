from typing import Any
from torch.utils.data._typing import T_co
from torch.utils.data import Dataset, DataLoader
import os


class SC2EGSetDataset(Dataset):
    """
    Inherits from PyTorch Dataset and ensures that the dataset for SC2EGSet is downloaded.

    :param dataset_unpack_dir: Specifies the path of a directory where the dataset files will be downloaded.
    :type dataset_unpack_dir: str
    :param dataset_download_dir: Specifies the path of a directory where the dataset files will be unpacked.
    :type dataset_download_dir: str
    :param url: Specifies the URL of the dataset which will be used to download the files.
    :type url: str
    :param transform: PyTorch transform.
    :type transform: ??????????
    """

    def __init__(
        self,
        dataset_unpack_dir: str = "./data/unpack",
        dataset_download_dir: str = "./data/download",
        url: str = "",  # This should probably be hardcoded! After all I want this to be a specific dataset.
        transform=None,
    ):

        self.dataset_download_dir = dataset_download_dir
        self.dataset_unpack_dir = dataset_unpack_dir
        self.transform = transform
        self.url = url

        self.downloaded = False
        # If there are files in the dataset_unpack_dir it means that it was downloaded and extracted:
        dataset_unpacked_files = os.listdir(self.dataset_unpack_dir)
        if dataset_unpacked_files:
            self.downloaded = True

        # We have received an URL for the dataset and it was not downloaded:
        if url != "":
            self.ensure_downloaded()

        # TODO: Try to unpack all of the zip files that constitute the dataset.
        # If the directory is correctly specified:
        if os.path.isdir(dataset_download_dir):
            # And there are files in the dataset directory:
            dataset_packed_files = os.listdir(dataset_download_dir)
            if dataset_packed_files and not dataset_unpacked_files:
                # Unpack all of the .zip files in that directory:
                # Create it if it doesnt exist

                self.downloaded = True

    def __unpack_files(self):
        """
        Implements unpacking logic for the dataset.
        """
        pass

    def ensure_downloaded(self):
        """
        Ensures that the dataset was downloaded before accessing the __len__ or __getitem__ methods.
        """
        if self.downloaded:
            return

        # TODO: download and unpack:

        # Load to the list of files

        self.downloaded = True
        return

    def __len__(self):
        """Returns the number of items that are within the dataset"""
        # TODO: Implement how to calculate the len of the dataset.
        # In the case of SC2EGSet this will be the number of files.
        self.ensure_downloaded()

        # Get len of list of files

        pass

    def __getitem__(self, index: Any) -> T_co:
        """_summary_

        :param index: Specifies the index of an item that should be retrieved.
        :type index: Any
        :return: Returns an item from the dataset.
        :rtype: T_co
        """
        # TODO: Implement how to get a single item from the dataset!
        # Most likely this will have to load the JSON file.
        self.ensure_downloaded()

        # load and return the specific file that corresponds to the index on the list of files

        pass
