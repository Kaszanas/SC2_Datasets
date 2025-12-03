from pathlib import Path

from sc2_datasets.available_replaypacks import (
    SC2EGSET_DATASET_REPLAYPACKS,
    SC2EGSET_SINGLE_JSON,
    DatasetProperties,
)
from sc2_datasets.lightning.datamodules.sc2_datamodule import (
    SC2DataModule,
    SC2SingleJSONDataModule,
)


class SC2EGSetDataModuleSingleJSON(SC2SingleJSONDataModule):
    def __init__(
        self,
        dataset_name: str = SC2EGSET_SINGLE_JSON.name,
        unpack_dir: Path | str = Path("./data/unpack/sc2egset_single_json"),
        download=True,
        download_dir: Path | str = Path("./data/download/sc2egset_single_json"),
        dataset_url: str = SC2EGSET_SINGLE_JSON.url,
        transform: callable | None = None,
        validator: callable | None = None,
    ):
        super().__init__(
            dataset_name,
            unpack_dir,
            download,
            download_dir,
            dataset_url,
            transform,
            validator,
        )


class SC2EGSetDataModule(SC2DataModule):
    """
    Defines a LightningDataModule abstraction for the
    SC2EGSet: StarCraft II Esport Game-State Dataset

    Parameters
    ----------
    replaypacks : list[DatasetProperties], optional
        Specifies a list of tuples (replaypack_name, replaypack download url),\
        by default SC2EGSET_DATASET_REPLAYPACKS
    download_dir : Path | str, optional
        Specifies the path where the dataset will be downloaded,\
        by default "./data/download"
    unpack_dir : Path | str, optional
        Specifies the path where the dataset will be unpacked\
        into a custom directory structure, by default "./data/unpack"
    download : bool, optional
        _description_, by default True
    transform : Callable, optional
        Specifies the PyTorch transforms to be used\
        on the replaypack (dataset), \
        Deprecated since version v1.5: Will be removed in v1.7.0, by default None
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
        replaypacks: list[DatasetProperties] = SC2EGSET_DATASET_REPLAYPACKS,
        download_dir: Path | str = Path("./data/download/sc2egset_dataset"),
        unpack_dir: Path | str = Path("./data/unpack/sc2egset_dataset"),
        download: bool = True,
        transform: callable = None,
        batch_size: int = 256,
        num_workers: int = 0,
        unpack_n_workers: int = 16,
        validator: callable | None = None,
    ):
        super().__init__(
            replaypacks=replaypacks,
            download_dir=download_dir,
            unpack_dir=unpack_dir,
            download=download,
            transform=transform,
            batch_size=batch_size,
            num_workers=num_workers,
            unpack_n_workers=unpack_n_workers,
            validator=validator,
        )
