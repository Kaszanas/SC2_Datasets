import os
import sys
from pl_bolts.models.regression import LogisticRegression
import pytorch_lightning as pl
import torch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.dataset.lightning_datamodules.sc2_egset_datamodule import SC2EGSetDataModule
from src.dataset.lightning_datamodules.sc2_replaypack_datamodule import (
    SC2ReplaypackDataModule,
)
from src.dataset.pytorch_datasets.sc2_replaypack_dataset import SC2ReplaypackDataset

# TODO: Import the dataset:


# logistic_regression = LogisticRegression(input_dim=2, num_classes=2)

# trainer = pl.Trainer()
# trainer.fit(model=logistic_regression, datamodule=dataset)
# TODO: Split the dataset into Cross Validation

# TODO: Train the models:

# TODO: Save the model:

# TODO: Save the metrics:

transform_1 = lambda sc2replay: [
    sc2replay.metadata.mapName,
    sc2replay.toonPlayerDescMap[0].toon_player_info.APM,
    sc2replay.toonPlayerDescMap[1].toon_player_info.APM,
]

datamodule = SC2ReplaypackDataModule(
    transform=transform_1,
    replaypack_name="2020_IEM_Katowice",
    replaypack_unpack_dir="D:/Projects/SC2EGSet_Experiments/test/test_files/unpack",
    download=False,
)
datamodule.prepare_data()
datamodule.setup()

print(datamodule.train_dataloader().dataset[0])
# class UnitType:
#     def __init__(self, name: str) -> None:
#         self._name = name

#     @property
#     def name(self):
#         return self._name

#     @property
#     def torch_name(self):
#         return torch.int32(self._name)


# transform_1 = lambda sc2: []
