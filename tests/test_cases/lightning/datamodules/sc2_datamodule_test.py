import shutil
import unittest
from pathlib import Path

import pytest

from sc2_datasets.lightning.datamodules.sc2_datamodule import SC2DataModule
from sc2_datasets.utils.zip_utils import unpack_zipfile
from tests.settings_test import TEST_REAL_REPLAYPACKS, TEST_SYNTHETIC_REPLAYPACKS
from tests.test_utils.test_utils import get_setup_paths


class SC2DataModuleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        (
            cls.test_replaypack_name,
            cls.replaypack_zip_path,
            cls.unpack_dir_path,
            cls.download_dir_path,
            cls.unpacked,
            cls.download,
        ) = get_setup_paths()

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
            shutil.rmtree(path=str(self.downloaded))

        if self.unpacked.exists():
            shutil.rmtree(path=str(self.unpacked))

    @pytest.mark.minor
    def test_unpack_datamodule(self):
        sc2_egset_datamodule = SC2DataModule(
            unpack_dir=self.unpack_dir_path,
            download_dir=self.download_dir_path,
            download=False,
            replaypacks=TEST_SYNTHETIC_REPLAYPACKS,
        )

        self.assertIsInstance(sc2_egset_datamodule, SC2DataModule)

    @pytest.mark.minor
    def test_download_unpack_datamodule_synthetic(self):
        sc2_egset_datamodule = SC2DataModule(
            unpack_dir=self.unpack_dir_path,
            download_dir=self.download_dir_path,
            download=True,
            replaypacks=TEST_SYNTHETIC_REPLAYPACKS,
        )

        self.assertIsInstance(sc2_egset_datamodule, SC2DataModule)

    @pytest.mark.major
    def test_download_unpack_datamodule_real(self):
        sc2_egset_datamodule = SC2DataModule(
            unpack_dir=self.unpack_dir_path,
            download_dir=self.download_dir_path,
            download=True,
            replaypacks=TEST_REAL_REPLAYPACKS,
        )

        self.assertIsInstance(sc2_egset_datamodule, SC2DataModule)
