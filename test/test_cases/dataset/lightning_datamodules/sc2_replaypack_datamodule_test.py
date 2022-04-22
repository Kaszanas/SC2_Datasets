import unittest

from src.dataset.lightning_datamodules.sc2_replaypack_datamodule import (
    SC2ReplaypackDataModule,
)


class SC2ReplaypackDataModuleTest(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_initialize_datamodule(self):

        sc2_replaypack_datamodule = SC2ReplaypackDataModule()

        self.assertIsInstance(sc2_replaypack_datamodule, SC2ReplaypackDataModule)
