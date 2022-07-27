from pathlib import Path
import shutil
import unittest

import pytest

from sc2_datasets.torch.datasets.sc2_dataset import SC2Dataset
from sc2_datasets.replay_data.sc2_replay_data import SC2ReplayData
from sc2_datasets.utils.zip_utils import unpack_zipfile

from tests.test_utils.test_utils import get_setup_paths
from tests.settings_test import TEST_SYNTHETIC_REPLAYPACKS


@pytest.mark.minor
class SC2DatasetTest(unittest.TestCase):
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

    def test_parsing_test_files(self):

        # REVIEW: Will this work correctly?
        sc2egset_dataset = SC2Dataset(
            unpack_dir=self.unpack_dir_path,
            download_dir=self.download_dir_path,
            download=False,
            names_urls=[(self.test_replaypack_name, "")],
        )

        self.assertIsInstance(sc2egset_dataset, SC2Dataset)
        # Files were properly indexed:
        self.assertNotEqual(len(sc2egset_dataset), 0)

        # Testing positive indexing:
        sc2_replaydata_0 = sc2egset_dataset[0]
        self.assertIsInstance(sc2_replaydata_0, SC2ReplayData)

        # Testing Negative indexing:
        sc2_replaydata_1 = sc2egset_dataset[-1]
        self.assertIsInstance(sc2_replaydata_1, SC2ReplayData)

        # There is only one replay loaded, so two indexing methods should return
        # the same object:
        self.assertEqual(hash(sc2_replaydata_0), hash(sc2_replaydata_1))

    def test_downloading_replaypacks(self):

        sc2egset_dataset = SC2Dataset(
            unpack_dir=self.unpack_dir_path,
            download_dir=self.download_dir_path,
            download=True,
            names_urls=TEST_SYNTHETIC_REPLAYPACKS,
        )

        # Dataset was initialized:
        self.assertIsInstance(sc2egset_dataset, SC2Dataset)
        # Files were properly indexed:
        self.assertNotEqual(len(sc2egset_dataset), 0)
        # It is possible to retrieve a single file by index:
        self.assertIsInstance(sc2egset_dataset[0], SC2ReplayData)
