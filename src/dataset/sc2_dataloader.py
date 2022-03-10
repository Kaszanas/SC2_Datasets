from typing import Any
from torch.utils.data._typing import T_co
from torch.utils.data import Dataset, DataLoader


class SC2EGSetDataset(Dataset):
    def __init__(self, dataset_dir: str, transform=None):

        self.dataset_dir = dataset_dir
        self.transform = transform

    def __len__(self):
        # TODO: Implement how to calculate the len of the dataset.
        # In the case of SC2EGSet this will be the number of files.
        pass

    def __getitem__(self, index: Any) -> T_co:
        # TODO: Implement how to get a single item from the dataset!
        # Most likely this will have to load the JSON file.
        return super().__getitem__(index)
