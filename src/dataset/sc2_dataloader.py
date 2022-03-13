from turtle import down
from typing import Any
from torch.utils.data._typing import T_co
from torch.utils.data import Dataset, DataLoader


class SC2EGSetDataset(Dataset):
    def __init__(self, dataset_dir: str, url: str, transform=None):

        self.dataset_dir = dataset_dir
        self.transform = transform
        self.url = url

        self.dataset = None

        self.downloaded = False

        # TODO: Try to unpack all of the zip files that constitute the dataset.

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

        # load and return the specific file that corresponds to the index on the list of files

        pass
