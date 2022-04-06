import os
from typing import Dict
import unittest
from src.dataset.replay_data.sc2_replay_data import SC2ReplayData

from src.dataset.pytorch_datasets.sc2_replaypack_dataset import SC2ReplaypackDataset


class SC2ReplaypackDatasetTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()

    def test_unpack_load_replaypack(self):

        sc2_replaypack_dataset = SC2ReplaypackDataset(
            replaypack_name="2020_IEM_Katowice",
            replaypack_unpack_dir=os.path.abspath("./test/test_files/unpack"),
        )

        # Replaypack was initialized:
        self.assertIsInstance(sc2_replaypack_dataset, SC2ReplaypackDataset)
        # Supplementary files were loaded properly:
        self.assertIsInstance(sc2_replaypack_dataset.replaypack_processed_info, Dict)
        self.assertIsInstance(sc2_replaypack_dataset.replaypack_dir_mapping, Dict)
        self.assertIsInstance(sc2_replaypack_dataset.replaypack_summary, Dict)

        # Files were properly indexed:
        self.assertNotEqual(len(sc2_replaypack_dataset), 0)
        # It is possible to retrieve a single file by index:
        self.assertIsInstance(sc2_replaypack_dataset[0], SC2ReplayData)

    def test_parsing_replaypack_replays(self):

        sc2_replaypack_dataset = SC2ReplaypackDataset(
            replaypack_name="2020_IEM_Katowice",
            replaypack_unpack_dir=os.path.abspath("./test/test_files/unpack"),
        )

        # Iterating over a single replaypacka and verifying
        # That it is possible to parse the replays into SC2ReplayData:
        for index in len(sc2_replaypack_dataset):
            replay_data = sc2_replaypack_dataset[index]

            self.assertIsInstance(replay_data, SC2ReplayData)
