from typing import Callable, List, Optional, Tuple

import pytorch_lightning as pl
from torch.utils.data import random_split
from torch.utils.data.dataloader import DataLoader

from sc2_datasets.torch.datasets.sc2_dataset import SC2Dataset


class SC2DataModule(pl.LightningDataModule):
    """
    Defines a LightningDataModule abstraction for some StarCraft II DataModule.

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
        replaypacks: List[Tuple[str, str]],
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
