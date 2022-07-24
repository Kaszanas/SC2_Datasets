import os
from pathlib import Path
import shutil
import unittest
from sc2egset_dataset.dataset.lightning_datamodules.sc2_datamodule import SC2DataModule

from sc2egset_dataset.dataset.utils.zip_utils import unpack_zipfile
from tests.test_utils.test_utils import get_specific_asset, get_test_output_dir

from tests.settings_test import TEST_REPLAYPACKS


# REVIEW: Verify these tests
class SC2EGSetDataModuleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.test_replaypack_name = "2022_TestReplaypack"
        cls.replaypack_zip_path = get_specific_asset(
            filename=cls.test_replaypack_name + ".zip"
        )

        cls.test_output_path = get_test_output_dir()
        cls.unpack_dir_path = os.path.join(cls.test_output_path, "unpack")
        cls.download_dir_path = os.path.join(cls.test_output_path, "download")

        # Initializing the unpacked where it should be:
        cls.unpacked = Path(cls.unpack_dir_path, cls.test_replaypack_name)
        cls.download = Path(cls.download_dir_path, cls.test_replaypack_name)

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

    def setUp(self) -> None:

        if self.download.exists():
            shutil.rmtree(path=self.downloaded.as_posix())

        if self.unpacked.exists():
            shutil.rmtree(path=self.unpacked.as_posix())

    def test_unpack_datamodule(self):
        sc2_egset_datamodule = SC2DataModule(
            unpack_dir=self.unpack_dir_path,
            download_dir=self.download_dir_path,
            download=False,
            replaypacks=TEST_REPLAYPACKS,
        )

        self.assertIsInstance(sc2_egset_datamodule, SC2DataModule)

    def test_download_unpack_datamodule(self):
        sc2_egset_datamodule = SC2DataModule(
            unpack_dir=self.unpack_dir_path,
            download_dir=self.download_dir_path,
            download=True,
            replaypacks=TEST_REPLAYPACKS,
        )

        self.assertIsInstance(sc2_egset_datamodule, SC2DataModule)
