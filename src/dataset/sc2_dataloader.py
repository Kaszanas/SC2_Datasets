from typing import Any
from torch.utils.data._typing import T_co
from torch.utils.data import Dataset, DataLoader
import os


class SC2EGSetDataset(Dataset):
    def __init__(
        self,
        dataset_unpack_dir: str = "./data/unpack",
        dataset_download_dir: str = "./data/download",
        url: str = "",
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
        if url != "" and not self.downloaded:
            # TODO: Download the dataset to the dataset_download_dir

            self.downloaded = True

        # TODO: Try to unpack all of the zip files that constitute the dataset.
        # If the directory is correctly specified:
        if os.path.isdir(dataset_download_dir):
            # And there are files in the dataset directory:
            dataset_packed_files = os.listdir(dataset_download_dir)
            if dataset_packed_files and not dataset_unpacked_files:
                # Unpack all of the .zip files in that directory:
                # Create it if it doesnt exist

                self.downloaded = True

    def ensure_downloaded(self):
        if self.downloaded:
            return

        # TODO: download and unpack:

        # Load to the list of files

        self.downloaded = True
        return

    def __len__(self):
        # TODO: Implement how to calculate the len of the dataset.
        # In the case of SC2EGSet this will be the number of files.
        self.ensure_downloaded()

        # Get len of list of files

        pass

    def __getitem__(self, index: Any) -> T_co:
        # TODO: Implement how to get a single item from the dataset!
        # Most likely this will have to load the JSON file.
        self.ensure_downloaded()

        # load and return the specific file that corresponds to the index on the list of files

        pass
