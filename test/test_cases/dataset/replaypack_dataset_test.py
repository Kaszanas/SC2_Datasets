import os
from typing import Dict
import unittest

from src.dataset.sc2_replaypack_dataset import SC2ReplaypackDataset


class SC2ReplaypackDatasetTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()

    def test_unpack_load_replaypack(self):

        sc2_replaypack_dataset = SC2ReplaypackDataset(
            replaypack_name="2020_IEM_Katowice",
            replaypack_unpack_dir=os.path.abspath("./test/test_files/unpack"),
        )

        self.assertIsInstance(sc2_replaypack_dataset, SC2ReplaypackDataset)
        self.assertIsInstance(sc2_replaypack_dataset.replaypack_processed_info, Dict)

    def test_download_load_replaypack(self):
        pass

    def test_get_item(self):
        pass

    def test_get_len(self):
        pass
