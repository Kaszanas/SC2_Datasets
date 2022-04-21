import os
import sys

# from pl_bolts.models.regression import LogisticRegression
import pytorch_lightning as pl
from pytorch_lightning.loggers import TensorBoardLogger

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.dataset.lightning_datamodules.sc2_replaypack_datamodule import (
    SC2ReplaypackDataModule,
)

from src.experiments.logistic_model import LogisticRegression

from src.dataset.transforms.economy_vs_outcome import economy_average_vs_outcome


# This is required because num_workers needs this guard
# Because otherwise creating processes might be done recursively?
# TODO: Verify this Issue #11
if __name__ == "__main__":
    # Initializing Lightning DataModule
    datamodule = SC2ReplaypackDataModule(
        transform=economy_average_vs_outcome,
        replaypack_name="2020_IEM_Katowice",
        replaypack_unpack_dir="D:/Projects/SC2EGSet_Experiments/test/test_files/unpack",
        download=False,
        batch_size=8,
        num_workers=4,
    )
    # Preparing the data:
    datamodule.prepare_data()
    datamodule.setup()

    # REVIEW: I am blocked here. The LR doesn't train:
    # Defining the model:
    logistic_regression = LogisticRegression(input_dim=2 * 39, num_classes=2)

    # Initializing logger and trainer:
    logger = TensorBoardLogger("tb_logs", name="Logistic Regression")
    trainer = pl.Trainer(
        logger=logger,
        accelerator="gpu",
        devices=1,
        auto_select_gpus=True,
        max_epochs=10,
        log_every_n_steps=5,
    )

    # REVIEW: Something is wrong here!
    # Training the model:
    trainer.fit(model=logistic_regression, datamodule=datamodule)
