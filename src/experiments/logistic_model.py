# https://github.com/PyTorchLightning/pytorch-lightning/blob/master/LICENSE
# This code is under the license that is presented above

from argparse import ArgumentParser
from typing import Any, Dict, List, Tuple, Type

import torch
from pytorch_lightning import LightningModule, Trainer, seed_everything
from torch import Tensor, nn
from torch.nn import functional as F
from torch.nn.functional import softmax
from torch.optim import Adam
from torch.optim.optimizer import Optimizer
from torchmetrics.functional import accuracy


class LogisticRegression(LightningModule):
    """Logistic regression model."""

    def __init__(
        self,
        input_dim: int,
        num_classes: int,
        bias: bool = True,
        learning_rate: float = 1e-4,
        optimizer: Type[Optimizer] = Adam,
        l1_strength: float = 0.0,
        l2_strength: float = 0.0,
        **kwargs: Any,
    ) -> None:
        """
        Args:
            input_dim: number of dimensions of the input (at least 1)
            num_classes: number of class labels (binary: 2, multi-class: >2)
            bias: specifies if a constant or intercept should be fitted (equivalent to fit_intercept in sklearn)
            learning_rate: learning_rate for the optimizer
            optimizer: the optimizer to use (default: ``Adam``)
            l1_strength: L1 regularization strength (default: ``0.0``)
            l2_strength: L2 regularization strength (default: ``0.0``)
        """
        super().__init__()
        self.save_hyperparameters()
        self.optimizer = optimizer

        self.linear = nn.Linear(
            in_features=self.hparams.input_dim,
            out_features=self.hparams.num_classes,
            bias=bias,
        )

    def forward(self, x: Tensor) -> Tensor:
        x = self.linear(x)
        y_hat = softmax(x)
        return y_hat

    def training_step(
        self, batch: Tuple[Tensor, Tensor], batch_idx: int
    ) -> Dict[str, Tensor]:
        x, y = batch

        # flatten any input
        x = x.view(x.size(0), -1)

        y_hat = self.linear(x)

        # PyTorch cross_entropy function combines log_softmax and nll_loss in single function
        loss = F.cross_entropy(y_hat, y, reduction="sum")

        # L1 regularizer
        if self.hparams.l1_strength > 0:
            l1_reg = self.linear.weight.abs().sum()
            loss += self.hparams.l1_strength * l1_reg

        # L2 regularizer
        if self.hparams.l2_strength > 0:
            l2_reg = self.linear.weight.pow(2).sum()
            loss += self.hparams.l2_strength * l2_reg

        loss /= x.size(0)

        self.log(
            "train_ce_loss",
            loss,
            on_step=True,
            on_epoch=True,
            prog_bar=True,
            logger=True,
        )

        return loss

    def validation_step(
        self, batch: Tuple[Tensor, Tensor], batch_idx: int
    ) -> Dict[str, Tensor]:
        x, y = batch
        x = x.view(x.size(0), -1)
        y_hat = self.linear(x)
        acc = accuracy(F.softmax(y_hat, -1), y)

        loss = F.cross_entropy(y_hat, y)

        self.log("val_loss", loss)
        self.log("acc", acc)

        return loss

    # def validation_epoch_end(
    #     self, outputs: List[Dict[str, Tensor]]
    # ) -> Dict[str, Tensor]:
    #     acc = torch.stack([x["acc"] for x in outputs]).mean()
    #     val_loss = torch.stack([x["val_loss"] for x in outputs]).mean()

    #     self.log("val_ce_loss", val_loss)
    #     self.log("val_acc", acc)

    #     return val_loss

    def test_step(
        self, batch: Tuple[Tensor, Tensor], batch_idx: int
    ) -> Dict[str, Tensor]:
        x, y = batch
        x = x.view(x.size(0), -1)
        y_hat = self.linear(x)
        acc = accuracy(F.softmax(y_hat, -1), y)

        loss = F.cross_entropy(y_hat, y)

        self.log("test_loss", loss)
        self.log("acc", acc)

        return loss

    # def test_epoch_end(self, outputs: List[Dict[str, Tensor]]) -> Dict[str, Tensor]:
    #     acc = torch.stack([x["acc"] for x in outputs]).mean()
    #     test_loss = torch.stack([x["test_loss"] for x in outputs]).mean()

    #     self.log("test_ce_loss", test_loss)
    #     self.log("test_acc", acc)

    #     return test_loss

    def configure_optimizers(self) -> Optimizer:
        return self.optimizer(self.parameters(), lr=self.hparams.learning_rate)
