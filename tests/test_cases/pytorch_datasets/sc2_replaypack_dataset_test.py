import shutil
import unittest
from pathlib import Path

import pytest

from sc2egset_dataset.dataset.pytorch_datasets.sc2_replaypack_dataset import (
    SC2ReplaypackDataset,
)
from sc2egset_dataset.dataset.replay_data.sc2_replay_data import SC2ReplayData
from sc2egset_dataset.dataset.utils.zip_utils import unpack_zipfile

from tests.settings_test import TEST_REAL_REPLAYPACKS, TEST_SYNTHETIC_REPLAYPACKS
from tests.test_utils.test_utils import get_setup_paths

# TODO: Rewrite or update these tests to better support validators:


@pytest.mark.minor
class SC2ReplaypackDatasetTest(unittest.TestCase):
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
    def test_unpack_replaypack_synthetic(self):

        sc2_replaypack_dataset = SC2ReplaypackDataset(
            replaypack_name=self.test_replaypack_name,
            unpack_dir=self.unpack_dir_path,
            download_dir=self.download_dir_path,
        )

        # Replaypack was initialized:
        self.assertIsInstance(sc2_replaypack_dataset, SC2ReplaypackDataset)
        # Supplementary files were loaded properly:
        self.assertIsInstance(sc2_replaypack_dataset.replaypack_processed_failed, dict)
        self.assertIsInstance(sc2_replaypack_dataset.replaypack_dir_mapping, dict)
        self.assertIsInstance(sc2_replaypack_dataset.replaypack_summary, dict)

        # Files were properly indexed:
        self.assertNotEqual(len(sc2_replaypack_dataset), 0)
        # It is possible to retrieve a single file by index:
        self.assertIsInstance(sc2_replaypack_dataset[0], SC2ReplayData)

    @pytest.mark.minor
    def test_download_unpack_replaypack_synthetic(self):

        sc2_replaypack_dataset = SC2ReplaypackDataset(
            replaypack_name=TEST_SYNTHETIC_REPLAYPACKS[0][0],
            unpack_dir=self.unpack_dir_path,
            download_dir=self.download_dir_path,
            download=True,
            url=TEST_SYNTHETIC_REPLAYPACKS[0][1],
        )

        # Replaypack was initialized:
        self.assertIsInstance(sc2_replaypack_dataset, SC2ReplaypackDataset)
        # Supplementary files were loaded properly:
        self.assertIsInstance(sc2_replaypack_dataset.replaypack_processed_failed, dict)
        self.assertIsInstance(sc2_replaypack_dataset.replaypack_dir_mapping, dict)
        self.assertIsInstance(sc2_replaypack_dataset.replaypack_summary, dict)

        # Files were properly indexed:
        self.assertNotEqual(len(sc2_replaypack_dataset), 0)
        # It is possible to retrieve a single file by index:
        self.assertIsInstance(sc2_replaypack_dataset[0], SC2ReplayData)

    @pytest.mark.major
    def test_download_unpack_replaypack_real(self):

        for rp_name, rp_url in TEST_REAL_REPLAYPACKS:
            with self.subTest(rp_name):
                sc2_replaypack_dataset = SC2ReplaypackDataset(
                    replaypack_name=rp_name,
                    unpack_dir=self.unpack_dir_path,
                    download_dir=self.download_dir_path,
                    download=True,
                    url=rp_url,
                )

                # Replaypack was initialized:
                self.assertIsInstance(sc2_replaypack_dataset, SC2ReplaypackDataset)
                # Supplementary files were loaded properly:
                self.assertIsInstance(
                    sc2_replaypack_dataset.replaypack_processed_failed, dict
                )
                self.assertIsInstance(
                    sc2_replaypack_dataset.replaypack_dir_mapping, dict
                )
                self.assertIsInstance(sc2_replaypack_dataset.replaypack_summary, dict)

                # Files were properly indexed:
                self.assertNotEqual(len(sc2_replaypack_dataset), 0)
                # It is possible to retrieve a single file by index:
                self.assertIsInstance(sc2_replaypack_dataset[0], SC2ReplayData)
