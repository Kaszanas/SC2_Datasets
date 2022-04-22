import unittest

from src.dataset.lightning_datamodules.sc2_egset_datamodule import SC2EGSetDataModule


class SC2EGSetDataModuleTest(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_initialize_datamodule(self):

        sc2_egset_datamodule = SC2EGSetDataModule()

        self.assertIsInstance(sc2_egset_datamodule, SC2EGSetDataModule)
