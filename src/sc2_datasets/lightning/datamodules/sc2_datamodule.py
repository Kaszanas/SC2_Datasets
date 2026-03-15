from pathlib import Path
from typing import Callable

import pytorch_lightning as pl
from torch.utils.data import random_split
from torch.utils.data.dataloader import DataLoader

from sc2_datasets.available_replaypacks import DatasetProperties
from sc2_datasets.torch.datasets.sc2_dataset import SC2Dataset
from sc2_datasets.torch.datasets.sc2_dataset_single_json import SC2DatasetSingleJSON


class SC2DataModuleSingleJSON(pl.LightningDataModule):
    def __init__(
        self,
        dataset_name: str,
        unpack_dir: Path,
        download: bool = True,
        download_dir: Path | str | None = None,
        json_path: Path | str | None = None,
        dataset_url: str = "",
        transform: Callable | None = None,
        validator: Callable | None = None,
        batch_size: int = 256,
        num_workers: int = 0,
    ):
        super().__init__()

        self.dataset_name = dataset_name
        self.unpack_dir = unpack_dir
        self.download = download
        self.download_dir = download_dir
        self.dataset_url = dataset_url
        self.transform = transform
        self.validator = validator
        self.batch_size = batch_size
        self.num_workers = num_workers

        self.json_path = json_path

    def prepare_data(self) -> None:
        self.dataset = SC2DatasetSingleJSON(
            dataset_name=self.dataset_name,
            unpack_dir=self.unpack_dir,
            json_path=self.json_path,
            download=self.download,
            download_dir=self.download_dir,
            dataset_url=self.dataset_url,
            transform=self.transform,
            validator=self.validator,
        )

    def setup(self, stage: str | None = None) -> None:
        # make assignments here (val/train/test split)
        # called on every process in DDP
        total_length = len(self.dataset)
        # 10% of total entries will be used for testing
        test_length = int(total_length * 0.1)
        # 10% of total entries will be used for validation
        val_length = int(total_length * 0.1)
        # 80% of total entries will be used for training
        train_length = total_length - test_length - val_length

        self.train_dataset, self.test_dataset, self.val_dataset = random_split(
            self.dataset,
            [train_length, test_length, val_length],
        )

    def train_dataloader(self) -> DataLoader:
        return DataLoader(
            self.train_dataset,
            batch_size=self.batch_size,
            num_workers=self.num_workers,
        )

    def val_dataloader(self) -> DataLoader:
        return DataLoader(
            self.val_dataset,
            batch_size=self.batch_size,
            num_workers=self.num_workers,
        )

    def test_dataloader(self) -> DataLoader:
        return DataLoader(
            self.test_dataset,
            batch_size=self.batch_size,
            num_workers=self.num_workers,
        )

    def teardown(self, stage):
        return super().teardown(stage)


class SC2DataModule(pl.LightningDataModule):
    """
    Defines a LightningDataModule abstraction for some StarCraft II DataModule.

    Parameters
    ----------
    replaypacks : list[DatasetProperties]
        Specifies a list of properties of replaypacks that will be used for downloading.
    download_dir : Path | str, optional
        Specifies the path where the dataset will be downloaded,\
        by default "./data/download"
    unpack_dir : Path | str, optional
        Specifies the path where the dataset will be unpacked\
        into a custom directory structure, by default "./data/unpack"
    download : bool, optional
        If the underlying dataset should be downloaded, by default True
    transform : Callable, optional
        Specifies the PyTorch transforms to be used\
        on the replaypack (dataset),
        Deprecated since version v1.5: Will be removed in v1.7.0, by default None
    batch_size : int, optional
        The size of collating individual\
        fetched data samples, by default 256
    num_workers : int, optional
        How many sub-processes\
        to use for data loading, by default 0
    unpack_n_workers : int, optional
        The number of workers\
        that will be used for unpacking the archive, by default 16
    validator : Callable | None, optional
        Specifies the validation option for fetched data,\
        this can also act as a filtering function that will be\
        applied for the entirety of the dataset, by default None
    """

    def __init__(
        self,
        replaypacks: list[DatasetProperties],
        download_dir: Path | str = Path("./data/download").resolve(),
        unpack_dir: Path | str = Path("./data/unpack").resolve(),
        download: bool = True,
        transform: Callable = None,
        batch_size: int = 256,
        num_workers: int = 0,
        unpack_n_workers: int = 16,
        validator: Callable | None = None,
    ):
        super().__init__()

        # PyTorch fields:
        self.transform = transform
        self.batch_size = batch_size
        self.num_workers = num_workers

        # Custom fields:
        self.download_dir = (
            download_dir
            if isinstance(download_dir, Path)
            else Path(download_dir).resolve()
        )
        self.unpack_dir = (
            unpack_dir if isinstance(unpack_dir, Path) else Path(unpack_dir).resolve()
        )
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

    def setup(self, stage: str | None = None) -> None:
        # make assignments here (val/train/test split)
        # called on every process in DDP
        total_length = len(self.dataset)
        # 10% of total entries will be used for testing
        test_length = int(total_length * 0.1)
        # 10% of total entries will be used for validation
        val_length = int(total_length * 0.1)
        # 80% of total entries will be used for training
        train_length = total_length - test_length - val_length

        self.train_dataset, self.test_dataset, self.val_dataset = random_split(
            self.dataset,
            [train_length, test_length, val_length],
        )

    def train_dataloader(self) -> DataLoader:
        return DataLoader(
            self.train_dataset,
            batch_size=self.batch_size,
            num_workers=self.num_workers,
        )

    def val_dataloader(self) -> DataLoader:
        return DataLoader(
            self.val_dataset,
            batch_size=self.batch_size,
            num_workers=self.num_workers,
        )

    def test_dataloader(self) -> DataLoader:
        return DataLoader(
            self.test_dataset,
            batch_size=self.batch_size,
            num_workers=self.num_workers,
        )

    def teardown(self, stage: str | None = None) -> None:
        # clean up after fit or test
        # called on every process in DDP
        return super().teardown(stage)
