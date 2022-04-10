import os
import sys
from typing import Tuple
from pl_bolts.models.regression import LogisticRegression
import pytorch_lightning as pl
import torch

from pl_bolts.datamodules import ImagenetDataModule

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.dataset.replay_data.sc2_replay_data import SC2ReplayData
from src.dataset.lightning_datamodules.sc2_replaypack_datamodule import (
    SC2ReplaypackDataModule,
)

from src.dataset.transforms.economy_vs_outcome import economy_average_vs_outcome

# TODO: Import the dataset:


# TODO: Split the dataset into Cross Validation

# TODO: Train the models:

# TODO: Save the model:

# TODO: Save the metrics:


datamodule = SC2ReplaypackDataModule(
    transform=economy_average_vs_outcome,
    replaypack_name="2020_IEM_Katowice",
    replaypack_unpack_dir="D:/Projects/SC2EGSet_Experiments/test/test_files/unpack",
    download=False,
)
datamodule.prepare_data()
datamodule.setup()

print(datamodule.train_dataloader().dataset[0])

# REVIEW: I am blocked here. The LR doesn't train:
logistic_regression = LogisticRegression(input_dim=39, num_classes=2)

trainer = pl.Trainer(
    accelerator="gpu", devices=1, auto_select_gpus=True, max_epochs=10000
)
trainer.fit(model=logistic_regression, datamodule=datamodule)


# transform_1 = lambda sc2: []
