import os
from pathlib import Path
import shutil
import unittest

import pytest
from sc2egset_dataset.dataset.utils.dataset_utils import load_replaypack_information
from sc2egset_dataset.dataset.utils.zip_utils import unpack_zipfile

from tests.test_utils.test_utils import get_specific_asset, get_test_output_dir


@pytest.mark.minor
class DatasetUtilsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:

        cls.test_replaypack_name = "2022_TestReplaypack"
        cls.replaypack_zip_path = get_specific_asset(
            filename=cls.test_replaypack_name + ".zip"
        )

        cls.test_output_path = get_test_output_dir()
        cls.unpack_dir_path = os.path.join(cls.test_output_path, "unpack")

        # Initializing the unpacked where it should be:
        cls.unpacked = Path(cls.unpack_dir_path, cls.test_replaypack_name)

        # If it doesn't exist, unpack the test .zip archive:
        if not cls.unpacked.exists():
            # Unpacks the replaypack that will be used for testing:
            cls.unpacked = Path(
                unpack_zipfile(
                    destination_dir=cls.unpack_dir_path,
                    subdir=cls.test_replaypack_name,
                    zip_path=cls.replaypack_zip_path,
                    n_workers=1,
                )
            )

    @classmethod
    def tearDownClass(cls) -> None:

        # Deletes the replaypack after the testing was finished:
        if cls.unpacked.exists():
            shutil.rmtree(path=cls.unpacked.as_posix())

    def test_load_replaypack_information_correct(self):

        (
            replaypack_data_path,
            replaypack_main_log_obj_list,
            replaypack_processed_failed,
            replaypack_dir_mapping,
            replaypack_summary,
        ) = load_replaypack_information(
            replaypack_name=self.test_replaypack_name,
            replaypack_path=self.unpacked,
            unpack_n_workers=1,
        )

        self.assertIsInstance(replaypack_data_path, str)

        # Assertions for main_log:
        self.assertIsInstance(replaypack_main_log_obj_list, list)
        self.assertEqual(len(replaypack_main_log_obj_list), 1)

        # Assertions for processed_failed:
        self.assertIsInstance(replaypack_processed_failed, dict)
        self.assertEqual(len(replaypack_processed_failed["processedFiles"]), 1)
        self.assertEqual(len(replaypack_processed_failed["failedToProcess"]), 0)

        # Assertions for replaypack mapping:
        self.assertIsInstance(replaypack_dir_mapping, dict)

        # Assertions for replaypack_summary:
        self.assertIsInstance(replaypack_summary, dict)

        # TODO: Some keys were not included here:
        self.assertEqual(len(replaypack_summary["Summary"]["gameVersions"].items()), 1)
        self.assertEqual(len(replaypack_summary["Summary"]["maps"].items()), 1)
        self.assertEqual(len(replaypack_summary["Summary"]["gameTimes"].items()), 1)
        self.assertEqual(len(replaypack_summary["Summary"]["dates"].items()), 1)
        self.assertEqual(len(replaypack_summary["Summary"]["matchupCount"].items()), 1)
