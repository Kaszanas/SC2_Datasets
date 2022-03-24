from re import L
import unittest

from src.dataset.replay_data import SC2ReplayData


class SC2ReplayDataTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()

    def test_loading_json(self):

        sc2_replay_data = SC2ReplayData(replay_filepath="")

        self.assertIsInstance(sc2_replay_data, SC2ReplayData)
