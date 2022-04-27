import unittest
from src.dataset.utils.sc2_replay_file_info.sc2_replay_file_info import (
    SC2ReplayFileInfo,
)
from src.dataset.validators.integrity_validator import (
    validate_integrity_singleprocess,
    validate_replays_integrity,
)
import test.test_utils.test_utils as test_utils

from pathlib import Path


class IntegrityValidatorTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.not_working_test_replay = Path(
            test_utils.get_specific_asset(filename="test_bit_flip_example.json")
        )
        cls.working_test_replay = Path(
            test_utils.get_specific_asset(filename="test_replay.json")
        )
        cls.list_of_replays = [
            SC2ReplayFileInfo(
                directory=cls.not_working_test_replay.parent,
                filename=cls.not_working_test_replay.name,
            ),
            SC2ReplayFileInfo(
                directory=cls.working_test_replay.parent,
                filename=cls.working_test_replay.name,
            ),
        ]

    def test_integrity_validator(self):
        bad_replays = validate_integrity_singleprocess(
            list_of_replays=self.list_of_replays
        )
        self.assertIsInstance(next(iter(bad_replays)), SC2ReplayFileInfo)
        self.assertEqual(len(bad_replays), 1)

    def test_multiprocessing_integrity_validator(self):
        bad_replays = validate_replays_integrity(
            list_of_replays=self.list_of_replays, n_workers=2
        )
        self.assertIsInstance(next(iter(bad_replays)), SC2ReplayFileInfo)
        self.assertEqual(len(bad_replays), 1)
