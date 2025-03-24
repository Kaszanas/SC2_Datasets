from typing import Callable, List, Optional, Tuple

import pytorch_lightning as pl
from torch.utils.data import random_split
from torch.utils.data.dataloader import DataLoader

from sc2_datasets.torch.datasets.sc2_dataset import SC2Dataset


class SC2DataModule(pl.LightningDataModule):
    """
    Defines a LightningDataModule abstraction for some StarCraft II DataModule.

    Parameters
    ----------
    replaypacks : List[Tuple[str, str]]
        _description_
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
        on the replaypack (dataset),
        Deprecated since version v1.5: Will be removed in v1.7.0, by default None
    dims : _type_, optional
        Specifies a tuple describing the shape of your data.\
        Extra functionality exposed in size,
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
        Specifies the validation option for fetched data,\
        this can also act as a filtering function that will be\
        applied for the entirety of the dataset, by default None
    """

    def __init__(
        self,
        replaypacks: List[Tuple[str, str]],
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
        super().__init__()

        # PyTorch fields:
        self.transform = transform
        self.dims = dims
        self.batch_size = batch_size
        self.num_workers = num_workers

        # Custom fields:
        self.download_dir = download_dir
        self.unpack_dir = unpack_dir
        self.download = download
        self.unpack_n_workers = unpack_n_workers
        self.validator = validator

        self.replaypacks = replaypacks

    def prepare_data(self) -> None:
        # download, split, etc...
        # only called on 1 GPU/TPU in distributed
        self.dataset = SC2Dataset(
            names_urls=self.replaypacks,
            download=self.download,
            download_dir=self.download_dir,
            unpack_dir=self.unpack_dir,
            transform=self.transform,
            unpack_n_workers=self.unpack_n_workers,
        )

    def setup(self, stage: Optional[str] = None) -> None:
        # make assignments here (val/train/test split)
        # called on every process in DDP

        total_length = len(self.dataset)
        # Add these to be a parameter in the initialization:
        # 16.(6)% of total entries will be used for testing:
        test_length = int(total_length / 6)
        # 10% of total entries will be used for validation
        val_length = int(total_length / 10)
        # everything else will be used for training
        train_length = total_length - test_length - val_length

        self.train_dataset, self.test_dataset, self.val_dataset = random_split(
            self.dataset,
            [train_length, test_length, val_length],
        )

    def train_dataloader(self) -> DataLoader:
        return DataLoader(
            self.train_dataset, batch_size=self.batch_size, num_workers=self.num_workers
        )

    def val_dataloader(self) -> DataLoader:
        return DataLoader(
            self.val_dataset, batch_size=self.batch_size, num_workers=self.num_workers
        )

    def test_dataloader(self) -> DataLoader:
        return DataLoader(
            self.test_dataset, batch_size=self.batch_size, num_workers=self.num_workers
        )

    def teardown(self, stage: Optional[str] = None) -> None:
        # clean up after fit or test
        # called on every process in DDP
        return super().teardown(stage)
