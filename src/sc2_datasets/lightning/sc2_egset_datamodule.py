from typing import Callable, List, Tuple

from sc2_datasets.available_replaypacks import SC2EGSET_DATASET_REPLAYPACKS

from sc2_datasets.lightning.datamodules.sc2_datamodule import SC2DataModule


class SC2EGSetDataModule(SC2DataModule):
    """
    Defines a LightningDataModule abstraction for the
    SC2EGSet: StarCraft II Esport Game-State Dataset

    :param download_dir: Specifies the path where the dataset will be downloaded
    :type download_dir: str, optional
    :param unpack_dir: Specifies the path where the dataset will be unpacked\
    into a custom directory structure, defaults to "./data/unpack"
    :type unpack_dir: str, optional
    :param transform: Specifies the PyTorch transforms to be used\
    on the replaypack (dataset),
    Deprecated since version v1.5: Will be removed in v1.7.0,\
    defaults to None
    :type transform: _type_, optional
    :param dims: Specifies a tuple describing the shape of your data.\
    Extra functionality exposed in size,
    Deprecated since version v1.5: Will be removed in v1.7.0,\
    defaults to None
    :type dims: _type_, optional
    :param batch_size: Specifies the size of collating individual\
    fetched data samples, defaults to 256
    :type batch_size: int, optional
    :param num_workers: Specifies the data loader instance how many sub-processes\
    to use for data loading, defaults to 0
    :type num_workers: int, optional
    :param unpack_n_workers: Specifies the number of workers\
    that will be used for unpacking the archive, defaults to 16
    :type unpack_n_workers: int, optional
    :param validator: Specifies the validation option for fetched data, defaults to None
    :type validator: Callable | None, optional
    """

    def __init__(
        self,
        replaypacks: List[Tuple[str, str]] = SC2EGSET_DATASET_REPLAYPACKS,
        download_dir: str = "./data/download",
        unpack_dir: str = "./data/unpack",
        download: bool = True,
        transform=None,
        dims=None,
        batch_size: int = 256,
        num_workers: int = 0,
        unpack_n_workers: int = 16,
        validator: Callable | None = None,
    ):

        super().__init__(
            replaypacks=replaypacks,
            download_dir=download_dir,
            unpack_dir=unpack_dir,
            download=download,
            transform=transform,
            dims=dims,
            batch_size=batch_size,
            num_workers=num_workers,
            unpack_n_workers=unpack_n_workers,
            validator=validator,
        )
