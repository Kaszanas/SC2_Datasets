from typing import Optional
import pytorch_lightning as pl

from torch.utils.data import random_split
from torch.utils.data.dataloader import DataLoader

from src.dataset.pytorch_datasets.sc2_replaypack_dataset import SC2ReplaypackDataset


class SC2ReplaypackDataModule(pl.LightningDataModule):

    """
    _summary_

    :param replaypack_name: _description_
    :type replaypack_name: str
    :param replaypack_unpack_dir: _description_, defaults to "./data/unpack"
    :type replaypack_unpack_dir: str, optional
    :param replaypack_download_dir: _description_, defaults to "./data/unpack"
    :type replaypack_download_dir: str, optional
    :param url: _description_, defaults to ""
    :type url: str, optional
    :param download: _description_, defaults to True
    :type download: bool, optional
    :param train_transforms: _description_, defaults to None
    :type train_transforms: _type_, optional
    :param val_transforms: _description_, defaults to None
    :type val_transforms: _type_, optional
    :param test_transforms: _description_, defaults to None
    :type test_transforms: _type_, optional
    :param dims: _description_, defaults to None
    :type dims: _type_, optional
    """

    def __init__(
        self,
        replaypack_name: str,
        replaypack_unpack_dir: str = "./data/unpack",
        replaypack_download_dir: str = "./data/unpack",
        url: str = "",
        download: bool = True,
        train_transforms=None,
        val_transforms=None,
        test_transforms=None,
        dims=None,
    ):

        super().__init__()

        self.replaypack_name = replaypack_name
        self.replaypack_unpack_dir = replaypack_unpack_dir
        self.replaypack_download_dir = replaypack_download_dir
        self.url = url
        self.download = download
        self.train_transforms = train_transforms
        self.val_transforms = val_transforms
        self.test_transforms = test_transforms
        self.dims = dims

    def prepare_data(self) -> None:
        # download, split, etc...
        # only called on 1 GPU/TPU in distributed
        self.dataset = SC2ReplaypackDataset(
            replaypack_name=self.replaypack_name,
            replaypack_unpack_dir=self.replaypack_unpack_dir,
            replaypack_download_dir=self.replaypack_download_dir,
            url=self.url,
            download=self.download,
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
        return DataLoader(self.train_dataset)

    def val_dataloader(self):
        return DataLoader(self.val_dataset)

    def test_dataloader(self):
        return DataLoader(self.test_dataset)

    def teardown(self, stage: Optional[str] = None) -> None:
        # clean up after fit or test
        # called on every process in DDP
        return super().teardown(stage)
