import os
import unittest

from src.dataset.pytorch_datasets.sc2_egset_dataset import SC2EGSetDataset
from src.dataset.replay_data.sc2_replay_data import SC2ReplayData


class SC2EGSetDatasetTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()

    def test_loading_replaypacks(self):

        sc2egset_dataset = SC2EGSetDataset(
            dataset_unpack_dir=os.path.abspath("./test/test_files/unpack"),
            dataset_download_dir=os.path.abspath("./test/test_files/download"),
            names_urls=[
                ("2020_IEM_Katowice", ""),
            ],
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
            dataset_unpack_dir=os.path.abspath("./test_files/unpack"),
            dataset_download_dir=os.path.abspath("./test_files/download"),
            names_urls=[
                ("2020_IEM_Katowice", ""),
            ],
            download=False,
        )
        # Iterate over the whole dataset and test replay json parsing
        for index in range(len(sc2egset_dataset)):
            sc2_replaydata = sc2egset_dataset[index]

            # Replay was parsed:
            self.assertIsInstance(sc2_replaydata, SC2ReplayData)
