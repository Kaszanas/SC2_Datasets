import os
import unittest

from sc2egset_dataset.dataset.lightning_datamodules.sc2_egset_datamodule import (
    SC2EGSetDataModule,
)


class TestSC2EGSetDataModule(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_initialize_datamodule(self):
        sc2_egset_datamodule = SC2EGSetDataModule(
            unpack_dir=os.path.abspath("./test/test_files/unpack"),
            download=False,
        )

        self.assertIsInstance(sc2_egset_datamodule, SC2EGSetDataModule)
