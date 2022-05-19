import os
import unittest

from src.dataset.pytorch_datasets.sc2_egset_dataset import SC2EGSetDataset
from src.dataset.replay_data.sc2_replay_data import SC2ReplayData


class SC2EGSetDatasetTest(unittest.TestCase):
    def test_loading_replaypacks(self):

        sc2egset_dataset = SC2EGSetDataset(
            unpack_dir=os.path.abspath("./test/test_files/unpack"),
            download_dir=os.path.abspath("./test/test_files/download"),
            download=False,
        )

        # Dataset was initialized:
        self.assertIsInstance(sc2egset_dataset, SC2EGSetDataset)
        # Files were properly indexed:
        self.assertNotEqual(len(sc2egset_dataset), 0)
        # It is possible to retrieve a single file by index:
        self.assertIsInstance(sc2egset_dataset[0], SC2ReplayData)

    def test_parsing_all_files(self):

        sc2egset_dataset = SC2EGSetDataset(
            unpack_dir=os.path.abspath("./test/test_files/unpack"),
            download_dir=os.path.abspath("./test/test_files/download"),
            download=False,
        )
        # Iterate over the whole dataset
        # test replay json parsing every 100 replays:
        for index in range(0, len(sc2egset_dataset), 100):
            sc2_replaydata = sc2egset_dataset[index]

            # Replay was parsed:
            self.assertIsInstance(sc2_replaydata, SC2ReplayData)
