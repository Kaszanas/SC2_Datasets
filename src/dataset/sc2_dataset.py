from typing import Any, List
from torch.utils.data._typing import T_co
from torch.utils.data import Dataset
import os
import requests
import uuid
import zipfile

from dataset.replay_data import SC2ReplayData
from dataset.replaypack_data import SC2ReplaypackData


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
        list_of_urls: List = [],  # This should probably be hardcoded! After all I want this to be a specific dataset.
        transform=None,
    ):

        self.dataset_download_dir = dataset_download_dir
        self.dataset_unpack_dir = dataset_unpack_dir
        self.transform = transform
        self.list_of_urls = list_of_urls
        # Holds all of the filepaths to .zip packages that contain the dataset:
        self.downloaded_filepaths = []
        self.len = None

        self.downloaded = False
        # If there are files in the dataset_unpack_dir
        # it means that it was downloaded and extracted:
        dataset_unpacked_files = os.listdir(self.dataset_unpack_dir)
        if dataset_unpacked_files:
            self.downloaded = True

        # We have received an URL for the dataset
        # and it migth not have been downloaded:
        if list_of_urls:
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
        # Unpacking the zip files that were downloaded:
        for downloaded_zip_path, downloaded_zip_name in self.downloaded_filepaths:
            with zipfile.ZipFile(downloaded_zip_path, "r") as zip_file:
                path_to_extract = os.path.join(
                    self.dataset_unpack_dir, downloaded_zip_name
                )
                # Checking the existence of the extraction output directory:
                if not os.path.exists(path_to_extract):
                    os.makedirs(path_to_extract)
                zip_file.extractall(path_to_extract)

                # TODO: Lazily load SC2ReplayData so that it holds the paths
                # To the .json files holding different info.

        # Load to the list of files
        # Add the files to the list of files.

        pass

    def ensure_downloaded(self):
        """
        Ensures that the dataset was downloaded before accessing the __len__ or __getitem__ methods.
        """
        if self.downloaded:
            return

        # Download all of the files from the list of provided urls:
        for url in self.list_of_urls:
            response = requests.get(url=url)
            # Get the filename from URL or it needs to be hardcoded!
            zip_filename = uuid.uuid4().hex
            download_filepath = os.path.join(
                self.dataset_download_dir, zip_filename + ".zip"
            )
            with open(download_filepath, "wb") as output_map_file:
                output_map_file.write(response.content)
                self.downloaded_filepaths.append((download_filepath, zip_filename))

        # Unpack the downloaded files:
        self.__unpack_files()

        self.downloaded = True
        return

    def __len__(self) -> int:
        """
        Returns the number of items that are within the dataset
        """
        # TODO: Implement how to calculate the len of the dataset.
        # In the case of SC2EGSet this will be the number of files.
        self.ensure_downloaded()

        # Get len of list of files from SC2ReplaypackData class
        if self.len != None:
            return self.len

        # Otherwise calculate it and return

        pass

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
        self.ensure_downloaded()

        # load and return the specific file that corresponds to the index on the list of files

        # This should return contents of a .json file?
        # Or maybe different IterableDatasets that coincide with the Lists that .json holds?

        # TODO: Get a specific SC2ReplayData from SC2ReplaypackData

        pass
