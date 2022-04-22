from typing import Optional
import pytorch_lightning as pl

from torch.utils.data import random_split
from torch.utils.data.dataloader import DataLoader
from src.dataset.pytorch_datasets.sc2_egset_dataset import SC2EGSetDataset


class SC2EGSetDataModule(pl.LightningDataModule):

    """
    _summary_

    :param dataset_download_dir: _description_, defaults to "./data/unpack"
    :type dataset_download_dir: str, optional
    :param dataset_unpack_dir: _description_, defaults to "./data/unpack"
    :type dataset_unpack_dir: str, optional
    :param transform: _description_, defaults to None
    :type transform: _type_, optional
    :param dims: _description_, defaults to None
    :type dims: _type_, optional
    """

    def __init__(
        self,
        dataset_download_dir: str = "./data/unpack",
        dataset_unpack_dir: str = "./data/unpack",
        download: bool = True,
        transform=None,
        dims=None,
        batch_size: int = 256,
        num_workers: int = 0,
    ):

        super().__init__()

        # PyTorch fields:
        self.transform = transform
        self.dims = dims
        self.batch_size = batch_size
        self.num_workers = num_workers

        # Custom fields:
        self.dataset_download_dir = dataset_download_dir
        self.dataset_unpack_dir = dataset_unpack_dir
        self.download = download

    def prepare_data(self) -> None:

        # download, split, etc...
        # only called on 1 GPU/TPU in distributed
        self.dataset = SC2EGSetDataset(
            dataset_download_dir=self.dataset_download_dir,
            dataset_unpack_dir=self.dataset_unpack_dir,
            transform=self.transform,
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

    def train_dataloader(self):
        return DataLoader(
            self.train_dataset, batch_size=self.batch_size, num_workers=self.num_workers
        )

    def val_dataloader(self):
        return DataLoader(
            self.val_dataset, batch_size=self.batch_size, num_workers=self.num_workers
        )

    def test_dataloader(self):
        return DataLoader(
            self.test_dataset, batch_size=self.batch_size, num_workers=self.num_workers
        )

    def teardown(self, stage: Optional[str] = None) -> None:
        # clean up after fit or test
        # called on every process in DDP
        return super().teardown(stage)
