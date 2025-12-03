import shutil
import unittest
from pathlib import Path

import pytest

from sc2_datasets.replay_data.sc2_replay_data import SC2ReplayData
from sc2_datasets.torch.datasets.sc2_dataset_single_json import SC2DatasetSingleJSON
from sc2_datasets.utils.zip_utils import unpack_zipfile
from tests.settings_test import TEST_SINGLE_JSON_REPLAYPACKS
from tests.test_utils.test_utils import get_assets_dir, get_setup_paths


@pytest.mark.minor
class SC2DatasetSingleJSONTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        properties = TEST_SINGLE_JSON_REPLAYPACKS[0]

        cls.dataset_name = properties.name
        cls.dataset_url = properties.url

        (
            cls.test_replaypack_name,
            cls.replaypack_zip_path,
            cls.unpack_dir_path,
            cls.download_dir_path,
            cls.unpacked,
            cls.download,
        ) = get_setup_paths(test_replaypack_name="sc2egset_synthetic_merged")

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

    def test_parsing_dataset(self):
        download_dir = get_assets_dir()

        dataset = SC2DatasetSingleJSON(
            dataset_name=self.dataset_name,
            unpack_dir=self.unpack_dir_path,
            download=False,
            download_dir=download_dir,
        )

        # Dataset was downloaded previously, so this will be tue afte initialization:
        self.assertTrue(dataset.was_downloaded)
        self.assertIsInstance(dataset, SC2DatasetSingleJSON)

        self.assertNotEqual(len(dataset), 0)

        sc2_replaydata_0 = dataset[0]
        self.assertIsInstance(sc2_replaydata_0, SC2ReplayData)
        self.assertIsNotNone(sc2_replaydata_0)

        sc2_replaydata_1 = dataset[1]
        self.assertIsInstance(sc2_replaydata_1, SC2ReplayData)
        self.assertIsNotNone(sc2_replaydata_1)

        sc2_replaydata_last = dataset[-1]
        self.assertIsInstance(sc2_replaydata_last, SC2ReplayData)
        self.assertIsNotNone(sc2_replaydata_last)

    def test_downloading_single_json_dataset(self):
        dataset = SC2DatasetSingleJSON(
            dataset_name=self.dataset_name,
            dataset_url=self.dataset_url,
            unpack_dir=self.unpack_dir_path,
            download_dir=self.download_dir_path,
            download=True,
        )

        # Dataset is downloaded as a part of this test  so this should be tue afte
        # initialization:
        self.assertTrue(dataset.was_downloaded)
        self.assertIsInstance(dataset, SC2DatasetSingleJSON)

        self.assertNotEqual(len(dataset), 0)

        sc2_replaydata_0 = dataset[0]
        self.assertIsInstance(sc2_replaydata_0, SC2ReplayData)
        self.assertIsNotNone(sc2_replaydata_0)

        sc2_replaydata_1 = dataset[1]
        self.assertIsInstance(sc2_replaydata_1, SC2ReplayData)
        self.assertIsNotNone(sc2_replaydata_1)

        sc2_replaydata_last = dataset[-1]
        self.assertIsInstance(sc2_replaydata_last, SC2ReplayData)
        self.assertIsNotNone(sc2_replaydata_last)
