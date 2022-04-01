from typing import Optional
import pytorch_lightning as pl


class SC2ReplaypackDataModule(pl.LightningDataModule):
    def __init__(
        self,
        train_transforms=None,
        val_transforms=None,
        test_transforms=None,
        dims=None,
    ):
        super().__init__(train_transforms, val_transforms, test_transforms, dims)

    def prepare_data(self) -> None:
        # download, split, etc...
        # only called on 1 GPU/TPU in distributed
        return super().prepare_data()

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
