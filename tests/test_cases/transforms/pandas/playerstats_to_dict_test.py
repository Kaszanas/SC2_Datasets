import unittest

import pandas as pd
import pytest

from sc2_datasets.replay_data.sc2_replay_data import SC2ReplayData
from sc2_datasets.transforms.pandas.player_stats_to_dict import (
    average_playerstats_dataframe,
    playerstats_average_to_dict,
    playerstats_to_dict,
)

import tests.test_utils.test_utils as test_utils

# REVIEW: These tests are only verifying the types of the data structures.
# Should these also verify their contents? How deep should these tests go?


@pytest.mark.minor
class PlayerStatsToDictTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        list_of_test_filenames = ["test_replay.json", "test_replay_victory_defeat.json"]

        cls.test_replays = []
        for filename in list_of_test_filenames:
            cls.test_replays.append(
                test_utils.get_specific_asset_path(filename=filename)
            )

        cls.sc2_replays_data = []
        for replay in cls.test_replays:
            sc2_replay = SC2ReplayData.from_file(replay_filepath=replay)
            cls.sc2_replays_data.append(sc2_replay)

    def test_playerstats_to_dict(self):
        res_dict = playerstats_to_dict(sc2_replay=self.sc2_replay_data)

        # Type assertions for data:
        for playerID, feature_dict in res_dict.items():
            self.assertIsInstance(playerID, str)
            self.assertIsInstance(feature_dict, dict)
            for key, feature_list in feature_dict.items():
                self.assertIsInstance(key, str)
                self.assertIsInstance(feature_list, list)

    def test_playerstats_to_dict_additional_data(self):
        additional_data = {
            "1": {"outcome": 1},
            "2": {"outcome": 2},
        }

        res_dict = playerstats_to_dict(
            sc2_replay=self.sc2_replay_data,
            additional_data_dict=additional_data,
        )

        # Type assertions for data:
        for playerID, feature_dict in res_dict.items():
            self.assertIsInstance(playerID, str)
            self.assertIsInstance(feature_dict, dict)
            # Assertions for additional data:
            self.assertTrue("outcome" in feature_dict)
            for key, feature_list in feature_dict.items():
                self.assertIsInstance(key, str)
                self.assertIsInstance(feature_list, list)

    def test_playerstats_average_to_dict(self):
        res_dict = playerstats_average_to_dict(sc2_replay=self.sc2_replay_data)

        # Type assertions for data:
        self.assertIsInstance(res_dict, dict)
        for key, value in res_dict.items():
            self.assertIsInstance(key, str)
            self.assertIsInstance(value, dict)

    def test_average_playerstats_dataframe(self):
        ps_dict = playerstats_to_dict(sc2_replay=self.sc2_replay_data)
        for playerID, df_repr in ps_dict.items():
            # Initializing dataframe from dict:
            dataframe = pd.DataFrame.from_dict(df_repr)
            dict_average_repr = average_playerstats_dataframe(playerstats_df=dataframe)

            # Type assertions for the data:
            self.assertIsInstance(playerID, str)
            for key, value in dict_average_repr.items():
                self.assertIsInstance(key, str)
                self.assertIsInstance(value, float)
