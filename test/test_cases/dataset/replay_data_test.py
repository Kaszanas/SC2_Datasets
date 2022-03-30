import unittest

from src.dataset.sc2_replay_data import SC2ReplayData
import test.test_utils.test_utils as test_utils


class SC2ReplayDataTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.test_replay = test_utils.get_specific_asset(filename="test_replay.json")

    def test_loading_json(self):

        sc2_replay_data = SC2ReplayData.from_file(replay_filepath=self.test_replay)

        self.assertIsInstance(sc2_replay_data, SC2ReplayData)

    def test_empty_json(self):

        # Empty json should raise a KeyError:
        with self.assertRaises(KeyError):
            sc2_replay_data = SC2ReplayData(loaded_replay_object={})
