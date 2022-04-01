from typing import Optional
import pytorch_lightning as pl

from src.dataset.pytorch_datasets.sc2_egset_dataset import SC2EGSetDataset


class SC2EGSetDataModule(pl.LightningDataModule):
    def __init__(
        self,
        dataset_download_dir: str = "",
        dataset_unpack_dir: str = "",
        train_transforms=None,
        val_transforms=None,
        test_transforms=None,
        dims=None,
    ):
        super().__init__()

        self.dataset_download_dir = dataset_download_dir
        self.dataset_unpack_dir = dataset_unpack_dir
        self.train_transforms = train_transforms
        self.val_transforms = val_transforms
        self.test_transforms = test_transforms
        self.dims = dims

    def prepare_data(self) -> None:

        # download, split, etc...
        # only called on 1 GPU/TPU in distributed
        SC2EGSetDataset(
            dataset_download_dir=self.dataset_download_dir,
            dataset_unpack_dir=self.dataset_unpack_dir,
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
