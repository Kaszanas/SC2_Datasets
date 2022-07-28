from typing import Any, Callable, Dict, List, Set, Tuple

from torch.utils.data import Dataset

from sc2_datasets.torch.datasets.sc2_replaypack_dataset import SC2ReplaypackDataset
from sc2_datasets.replay_data.sc2_replay_data import SC2ReplayData


class SC2Dataset(Dataset):
    """
    Inherits from PyTorch Dataset and ensures that the dataset for SC2EGSet is downloaded.

    :param unpack_dir: Specifies the path of a directory\
    where the dataset files will be unpacked.
    :type unpack_dir: str
    :param download_dir: Specifies the path of a directory where\
    the dataset files will be downloaded.
    :type download_dir: str
    :param names_urls: Specifies the URL of the dataset which\
    will be used to download the files.
    :type names_urls: List[Tuple[str, str]]
    :param unpack_n_workers: Specifies the number of workers\
    that will be used for unpacking the archive, defaults to 16
    :type unpack_n_workers: int, optional
    :param transform: PyTorch transform. function that takes SC2ReplayData and return something
    :type transform: Func[SC2ReplayData, T]
    :param validator: Specifies the validation option for fetched data, defaults to None
    :type validator: Callable | None, optional
    """

    def __init__(
        self,
        names_urls: List[Tuple[str, str]],
        unpack_dir: str = "./data/unpack",
        download_dir: str = "./data/download",
        download: bool = True,
        unpack_n_workers: int = 16,
        transform: Callable | None = None,
        validator: Callable | None = None,
    ):

        # PyTorch fields:
        self.transform = transform

        # Custom fields:
        self.download_dir = download_dir
        self.unpack_dir = unpack_dir
        self.names_urls = names_urls
        self.download = download
        self.unpack_n_workers = unpack_n_workers
        self.validator = validator

        self.skip_files: Dict[str, Set[str]] = {}

        # We have received an URL for the dataset
        # and it migth not have been downloaded:
        self.len = 0
        self.ensure_downloaded()

    def ensure_downloaded(self):
        """
        Ensures that the dataset was downloaded before accessing the __len__ or __getitem__ methods.
        """

        self.replaypacks: List[SC2ReplaypackDataset] = []

        # Iterating over the provided URLs:
        for replaypack_name, url in self.names_urls:
            # Initializing SC2ReplaypackDataset cumulatively calculating its length:
            replaypack = SC2ReplaypackDataset(
                replaypack_name=replaypack_name,
                download_dir=self.download_dir,
                unpack_dir=self.unpack_dir,
                url=url,
                download=self.download,
                unpack_n_workers=self.unpack_n_workers,
                validator=self.validator,
            )

            # Retrieving files that were skipped when initializing a dataset,
            # This is based on validator:
            # TODO: This will be used later:
            # self.skip_files[replaypack_name] = replaypack.skip_files
            self.replaypacks.append(replaypack)
            self.len += len(replaypack)

    def __len__(self) -> int:
        """
        Returns the number of items that are within the dataset
        """
        return self.len

    def __getitem__(self, index: Any) -> Tuple[Any, Any] | SC2ReplayData:
        """
        Exposes logic of getting a single parsed item by using dataset[index].

        :param index: Specifies the index of an item that should be retrieved.
        :type index: Any
        :raises IndexError: To support negative indexing,\
        if the index is less than zero twice, IndexError is raised.
        :raises IndexError: If the index is greater than length\
        of the dataset IndexError is raised.
        :return: Returns a parsed SC2ReplayData from an underlying SC2ReplaypackDataset,\
        or a result of a transform that was passed to the dataset.
        :rtype: Tuple[Any, Any] | SC2ReplayData
        """

        # If the index is negative, treat it as if expressed from the back of the sequence.
        # For example, if index is -1 and lenght is 10,
        # it means we are looking for the last element, which is at index 10 + (-1) = 9
        if index < 0:
            index = self.len + index

        if index < 0:
            raise IndexError(f"Computed index {index} is still less than zero!")

        if index > self.len:
            raise IndexError(f"Computed index {index} is greater than {self.len}!")

        for replaypack in self.replaypacks:
            if index < len(replaypack):
                if self.transform:
                    return self.transform(replaypack[index])
                return replaypack[index]
            else:
                index -= len(replaypack)
