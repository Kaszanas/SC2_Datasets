from typing import Callable, Optional

import pytorch_lightning as pl
from torch.utils.data import random_split
from torch.utils.data.dataloader import DataLoader

from sc2_datasets.torch.datasets.sc2_replaypack_dataset import SC2ReplaypackDataset


class SC2ReplaypackDataModule(pl.LightningDataModule):
    """
    Defines a LightningDataModule abstraction for a single StarCraft II replaypack.

    :param replaypack_name: Specifies a replaypack name which will be used as a directory name.
    :type replaypack_name: str
    :param unpack_dir: Specifies the path where the replaypack (dataset)\
    will be unpacked into a custom directory structure, defaults to "./data/unpack"
    :type unpack_dir: str, optional
    :param download_dir: Specifies the path where the replaypack (dataset)\
    will be downloaded, defaults to "./data/unpack"
    :type download_dir: str, optional
    :param url: Specifies the url which will be used to download\
    the replaypack (dataset), defaults to ""
    :type url: str, optional
    :param download: Specifies if the dataset should be downloaded.\
    Otherwise the dataset is loaded from the unpack_dir\
    and a custom directory structure is assumed, defaults to True
    :type download: bool, optional
    :param transform: Specifies the PyTorch transforms to be used on the replaypack (dataset),\
    Deprecated since version v1.5: Will be removed in v1.7.0, defaults to None
    :type transform: _type_, optional
    :param dims: Specifies a tuple describing the shape of your data.\
    Extra functionality exposed in size,\
    Deprecated since version v1.5: Will be removed in v1.7.0, defaults to None
    :type dims: _type_, optional
    :param unpack_n_workers: Specifies the number of workers\
    that will be used for unpacking the archive, defaults to 16
    :type unpack_n_workers: int, optional
    :param validator: Specifies the validation option for fetched data, defaults to None
    :type validator: Callable | None, optional
    """

    def __init__(
        self,
        replaypack_name: str,
        unpack_dir: str = "./data/unpack",
        download_dir: str = "./data/download",
        url: str = "",
        download: bool = True,
        transform: Callable | None = None,
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
        self.replaypack_name = replaypack_name
        self.unpack_dir = unpack_dir
        self.download_dir = download_dir
        self.url = url
        self.download = download
        self.unpack_n_workers = unpack_n_workers
        self.validator = validator

    def prepare_data(self) -> None:
        # download, split, etc...
        # only called on 1 GPU/TPU in distributed
        self.dataset = SC2ReplaypackDataset(
            replaypack_name=self.replaypack_name,
            unpack_dir=self.unpack_dir,
            download_dir=self.download_dir,
            url=self.url,
            download=self.download,
            transform=self.transform,
            unpack_n_workers=self.unpack_n_workers,
            validator=self.validator,
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
