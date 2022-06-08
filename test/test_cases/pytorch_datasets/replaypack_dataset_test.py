import os
from typing import Dict
import unittest

from src.dataset.replay_data.sc2_replay_data import SC2ReplayData
from src.dataset.pytorch_datasets.sc2_replaypack_dataset import SC2ReplaypackDataset
from src.dataset.utils.dataset_utils import (
    validate_replays_integrity,
    validate_integrity_singleprocess,
)

# TODO: Rewrite or update these tests to better support validators:


class SC2ReplaypackDatasetTest(unittest.TestCase):
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

    # REVIEW: Is this test needed?
    @unittest.skip("reason for skipping")
    def test_parsing_replaypack_replays(self):

        sc2_replaypack_dataset = SC2ReplaypackDataset(
            replaypack_name="2020_IEM_Katowice",
            unpack_dir=os.path.abspath("./test/test_files/unpack"),
        )

        # Iterating over a single replaypacka and verifying
        # That it is possible to parse the replays into SC2ReplayData:
        for index in range(len(sc2_replaypack_dataset)):
            replay_data = sc2_replaypack_dataset[index]

            self.assertIsInstance(replay_data, SC2ReplayData)

    def test_replaypack_integrity_validation(self):
        files_rejected = 0

        def validator(list_of_replays):
            nonlocal files_rejected
            result = validate_integrity_singleprocess(list_of_replays=list_of_replays)
            files_rejected = len(result)

            # save to disk

            return result

        sc2_replaypack_dataset = SC2ReplaypackDataset(
            replaypack_name="2021_Dreamhack_SC2_Masters_Fall",
            unpack_dir=os.path.abspath("./test/test_files/unpack"),
            validator=validator,
        )

        self.assertIsInstance(sc2_replaypack_dataset, SC2ReplaypackDataset)
        self.assertGreaterEqual(files_rejected, 1)

    # def test_replaypack_integrity_validation(self):

    #     # path_to_file = ""

    #     # def save_to_disk_validator(list_of_replays):
    #     #     nonlocal path_to_file
    #     #     result = validate_integrity_singleprocess(list_of_replays=list_of_replays)
    #     #     # TODO: save `result` to disk
    #     #     return result

    #     # def load_from_disk_validator(list_of_replays):
    #     #     nonlocal path_to_file
    #     #     # load set from disk and return
    #     #     pass

    #     sc2_replaypack_dataset_1 = SC2ReplaypackDataset(
    #         replaypack_name="2021_Dreamhack_SC2_Masters_Fall",
    #         unpack_dir=os.path.abspath("./test/test_files/unpack"),
    #         validator=save_to_disk_validator,
    #     )
