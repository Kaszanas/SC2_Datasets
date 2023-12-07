from typing import Callable, List, Tuple

from sc2_datasets.available_replaypacks import SC2EGSET_DATASET_REPLAYPACKS

from sc2_datasets.lightning.datamodules.sc2_datamodule import SC2DataModule


class SC2EGSetDataModule(SC2DataModule):
    """
    Defines a LightningDataModule abstraction for the
    SC2EGSet: StarCraft II Esport Game-State Dataset

    Parameters
    ----------
    replaypacks : List[Tuple[str, str]], optional
        Specifies a list of tuples (replaypack_name, replaypack download url),\
        by default SC2EGSET_DATASET_REPLAYPACKS
    download_dir : str, optional
        Specifies the path where the dataset will be downloaded,\
        by default "./data/download"
    unpack_dir : str, optional
        Specifies the path where the dataset will be unpacked\
        into a custom directory structure, by default "./data/unpack"
    download : bool, optional
        _description_, by default True
    transform : Callable, optional
        Specifies the PyTorch transforms to be used\
        on the replaypack (dataset), \
        Deprecated since version v1.5: Will be removed in v1.7.0, by default None
    dims : _type_, optional
        Specifies a tuple describing the shape of your data.\
        Extra functionality exposed in size,\
        Deprecated since version v1.5: Will be removed in v1.7.0,\, by default None
    batch_size : int, optional
        Specifies the size of collating individual\
        fetched data samples, by default 256
    num_workers : int, optional
        Specifies the data loader instance how many sub-processes\
        to use for data loading, by default 0
    unpack_n_workers : int, optional
        Specifies the number of workers\
        that will be used for unpacking the archive, by default 16
    validator : Callable | None, optional
        Specifies the validation option for fetched data, by default None
    """

    def __init__(
        self,
        replaypacks: List[Tuple[str, str]] = SC2EGSET_DATASET_REPLAYPACKS,
        download_dir: str = "./data/download",
        unpack_dir: str = "./data/unpack",
        download: bool = True,
        transform: Callable = None,
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
