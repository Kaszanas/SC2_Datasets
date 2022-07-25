from pathlib import Path
import shutil
import unittest

import pytest

from sc2egset_dataset.dataset.lightning_datamodules.sc2_egset_datamodule import (
    SC2EGSetDataModule,
)
from sc2egset_dataset.dataset.utils.zip_utils import unpack_zipfile
from tests.test_utils.test_utils import get_setup_paths

from tests.settings_test import (
    TEST_REAL_REPLAYPACKS,
    TEST_SYNTHETIC_REPLAYPACKS,
)


class SC2EGSetDataModuleTest(unittest.TestCase):
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
            shutil.rmtree(path=self.downloaded.as_posix())

        if self.unpacked.exists():
            shutil.rmtree(path=self.unpacked.as_posix())

    @pytest.mark.minor
    def test_unpack_datamodule(self):
        sc2_egset_datamodule = SC2EGSetDataModule(
            unpack_dir=self.unpack_dir_path,
            download_dir=self.download_dir_path,
            download=False,
            replaypacks=TEST_SYNTHETIC_REPLAYPACKS,
        )

        self.assertIsInstance(sc2_egset_datamodule, SC2EGSetDataModule)

    @pytest.mark.minor
    def test_download_unpack_datamodule(self):
        sc2_egset_datamodule = SC2EGSetDataModule(
            unpack_dir=self.unpack_dir_path,
            download_dir=self.download_dir_path,
            download=True,
            replaypacks=TEST_SYNTHETIC_REPLAYPACKS,
        )

        self.assertIsInstance(sc2_egset_datamodule, SC2EGSetDataModule)

    @pytest.mark.major
    def test_download_unpack_datamodule_real(self):
        sc2_egset_datamodule = SC2EGSetDataModule(
            unpack_dir=self.unpack_dir_path,
            download_dir=self.download_dir_path,
            download=True,
            replaypacks=TEST_REAL_REPLAYPACKS,
        )

        self.assertIsInstance(sc2_egset_datamodule, SC2EGSetDataModule)
