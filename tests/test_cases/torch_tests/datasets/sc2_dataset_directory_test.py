import unittest

import pytest

from sc2_datasets.replay_data.sc2_replay_data import SC2ReplayData
from sc2_datasets.torch.datasets.sc2_dataset_directory import SC2DatasetDirectory
from tests.test_utils.test_utils import get_assets_dir


class SC2DatasetDirectoryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.asset_dir = get_assets_dir()
        cls.dataset_directory_path = cls.asset_dir / "directory_dataset"

    @pytest.mark.minor
    def test_initialize_dataset(self):
        dataset = SC2DatasetDirectory(directory=self.dataset_directory_path)

        self.assertEqual(len(dataset), 2)

        for idx in range(len(dataset)):
            replay_data = dataset[idx]
            self.assertIsInstance(replay_data, SC2ReplayData)

    # TODO:
    @pytest.mark.minor
    def test_invalid_directory(self):
        pass

    # TODO:
    def test_empty_directory(self):
        pass

    # TODO:
    def test_transform_function(self):
        pass

    # TODO:
    def test_validator_function(self):
        pass
