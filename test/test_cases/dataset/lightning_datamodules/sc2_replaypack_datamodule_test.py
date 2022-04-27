import os
import unittest

from src.dataset.lightning_datamodules.sc2_replaypack_datamodule import (
    SC2ReplaypackDataModule,
)


class SC2ReplaypackDataModuleTest(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_initialize_datamodule(self):

        sc2_replaypack_datamodule = SC2ReplaypackDataModule(
            replaypack_name="2020_IEM_Katowice",
            unpack_dir=os.path.abspath("./test/test_files/unpack"),
            download=False,
        )

        self.assertIsInstance(sc2_replaypack_datamodule, SC2ReplaypackDataModule)