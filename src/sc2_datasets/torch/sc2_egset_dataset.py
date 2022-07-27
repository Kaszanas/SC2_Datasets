from typing import Callable, List, Tuple

from sc2_datasets.available_replaypacks import SC2EGSET_DATASET_REPLAYPACKS

from sc2_datasets.torch.datasets.sc2_dataset import SC2Dataset


class SC2EGSetDataset(SC2Dataset):
    """
    Inherits from SC2Dataset and ensures that the dataset for SC2EGSet is downloaded.

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
        unpack_dir: str = "./data/unpack/sc2egset_dataset",
        download_dir: str = "./data/download/sc2egset_dataset",
        names_urls: List[Tuple[str, str]] = SC2EGSET_DATASET_REPLAYPACKS,
        download: bool = True,
        unpack_n_workers: int = 16,
        transform: Callable | None = None,
        validator: Callable | None = None,
    ):

        super().__init__(
            unpack_dir=unpack_dir,
            download_dir=download_dir,
            names_urls=names_urls,
            download=download,
            unpack_n_workers=unpack_n_workers,
            transform=transform,
            validator=validator,
        )
