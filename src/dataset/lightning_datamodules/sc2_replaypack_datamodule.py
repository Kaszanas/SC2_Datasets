from typing import Optional
import pytorch_lightning as pl

from src.dataset.pytorch_datasets.sc2_replaypack_dataset import SC2ReplaypackDataset


class SC2ReplaypackDataModule(pl.LightningDataModule):
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
        SC2ReplaypackDataset(
            replaypack_name=self.replaypack_name,
            replaypack_unpack_dir=self.replaypack_unpack_dir,
            replaypack_download_dir=self.replaypack_download_dir,
            url=self.url,
            download=self.download,
        )

    def setup(self, stage: Optional[str] = None) -> None:
        # make assignments here (val/train/test split)
        # called on every process in DDP
        return super().setup(stage)

    def train_dataloader(self):
        return super().train_dataloader()

    def val_dataloader(self):
        return super().val_dataloader()

    def test_dataloader(self):
        return super().test_dataloader()

    def teardown(self, stage: Optional[str] = None) -> None:
        # clean up after fit or test
        # called on every process in DDP
        return super().teardown(stage)
