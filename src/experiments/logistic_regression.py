from pl_bolts.models.regression import LogisticRegression
import pytorch_lightning as pl

from src.dataset.lightning_datamodules.sc2_egset_datamodule import SC2EGSetDataModule

# TODO: Import the dataset:
dataset = SC2EGSetDataModule()

logistic_regression = LogisticRegression(input_dim=2, num_classes=2)

trainer = pl.Trainer()
trainer.fit(model=logistic_regression, datamodule=dataset)
# TODO: Split the dataset into Cross Validation

# TODO: Train the models:

# TODO: Save the model:

# TODO: Save the metrics:
