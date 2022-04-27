import unittest
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
            test_utils.get_specific_asset(filename="test_replay.json")
        )
        cls.working_test_replay = Path(
            test_utils.get_specific_asset(filename="test_replay1.json")
        )
        cls.list_of_replays = [cls.not_working_test_replay, cls.working_test_replay]

    def test_integrity_validator(self):
        bad_replays = validate_integrity_singleprocess(
            list_of_replays=self.list_of_replays
        )

    def test_multiprocessing_integrity_validator(self):
        bad_replays = validate_replays_integrity(list_of_replays=self.list_of_replays)
