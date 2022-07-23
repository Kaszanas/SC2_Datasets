import os
from pathlib import Path
import shutil
import unittest
from sc2egset_dataset.dataset.utils.dataset_utils import load_replaypack_information
from sc2egset_dataset.dataset.utils.zip_utils import unpack_zipfile

from tests.test_utils.test_utils import get_specific_asset, get_test_output_dir


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

    def test_load_replaypack_information(self):

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
        self.assertIsInstance(replaypack_main_log_obj_list, list)
        self.assertIsInstance(replaypack_processed_failed, dict)
        self.assertIsInstance(replaypack_dir_mapping, dict)
        self.assertIsInstance(replaypack_summary, dict)
