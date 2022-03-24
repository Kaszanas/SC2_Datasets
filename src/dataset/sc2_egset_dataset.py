from typing import Any, List, Tuple
from torch.utils.data._typing import T_co
from torch.utils.data import Dataset
import os
import requests
import uuid
import zipfile

from dataset.replay_data import SC2ReplayData
from dataset.replaypack_data import SC2ReplaypackData


def download_dataset(urls, destination_dir) -> List[Tuple[str, str]]:
    result = []

    for url in urls:
        response = requests.get(url=url)
        # Get the filename from URL or it needs to be hardcoded!
        zip_filename = uuid.uuid4().hex
        download_filepath = os.path.join(destination_dir, zip_filename + ".zip")
        with open(download_filepath, "wb") as output_map_file:
            output_map_file.write(response.content)
            result.append((download_filepath, zip_filename))

    if len(result) != len(urls):
        raise Exception("dupa")

    return result


def find_downloaded_datasets(directory) -> List[Tuple[str, str]]:
    result = []
    files = os.listdir(directory)
    for file in files:
        result.append(file, os.path.splitext(file)[0])
    return result


def unpack_files(dataset_archives: List[str, str], destination_dir):
    """
    Implements unpacking logic for the dataset.
    """
    # Unpacking the zip files that were downloaded:
    for dataset_path, zip_filename in dataset_archives:

        # for downloaded_zip_path, downloaded_zip_name in self.downloaded_filepaths:
        with zipfile.ZipFile(dataset_path, "r") as zip_file:
            path_to_extract = os.path.join(destination_dir, zip_filename)
            # Checking the existence of the extraction output directory:
            if not os.path.exists(path_to_extract):
                os.makedirs(path_to_extract)
            zip_file.extractall(path_to_extract)

            # TODO: Further down extract the dataset
    pass


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
            str
        ] = [],  # This should probably be hardcoded! After all I want this to be a specific dataset.
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

        # # If there are files in the dataset_unpack_dir
        # # it means that it was downloaded and extracted:
        # dataset_unpacked_files = os.listdir(self.dataset_unpack_dir)
        # if dataset_unpacked_files:
        #     # TODO: calculate length
        #     return

        # dataset_downloaded_files = os.listdir(self.dataset_download_dir)
        # if dataset_downloaded_files:
        #     downloaded_filepaths = find_downloaded_datasets(self.dataset_download_dir)

        #     unpack_files(
        #         dataset_archives=downloaded_filepaths,
        #         destination_dir=self.dataset_download_dir,
        #     )

        #     # TODO: calculate length
        #     return

        # # If we are here, we need to download, unpack, calculate lenght
        # downloaded_filepaths = download_dataset(
        #     urls=self.list_of_urls, destination_dir=self.dataset_download_dir
        # )

        # # Unpack the downloaded files:
        # unpack_files(
        #     dataset_archives=downloaded_filepaths,
        #     destination_dir=self.dataset_unpack_dir,
        # )

    def __len__(self) -> int:
        """
        Returns the number of items that are within the dataset
        """
        # TODO: Implement how to calculate the len of the dataset.
        # In the case of SC2EGSet this will be the number of files.

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

        # load and return the specific file that corresponds to the index on the list of files

        # This should return contents of a .json file?
        # Or maybe different IterableDatasets that coincide with the Lists that .json holds?

        # TODO: Get a specific SC2ReplayData from SC2ReplaypackData

        pass

    def load_files(self):

        # TODO: Lazily load SC2ReplayData so that it holds the paths
        # To the .json files holding different info.

        # Load to the list of files
        # Add the files to the list of files.

        pass