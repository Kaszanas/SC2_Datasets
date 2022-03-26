import unittest

from src.dataset.sc2_replaypack_dataset import SC2ReplaypackDataset


class SC2ReplaypackDatasetTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()

    def test_load_unpacked_replaypack(self):

        sc2_replaypack_dataset = SC2ReplaypackDataset()

        self.assertIsInstance(sc2_replaypack_dataset, SC2ReplaypackDataset)

    def test_download_load_replaypack(self):
        pass
