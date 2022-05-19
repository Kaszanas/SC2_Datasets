import unittest

import pandas as pd

from src.dataset.replay_data.sc2_replay_data import SC2ReplayData
from src.dataset.transforms.pandas.player_stats_to_dict import (
    average_playerstats_dataframe,
    playerstats_average_to_dict,
    playerstats_to_dict,
)
import test.test_utils.test_utils as test_utils


class PlayerStatsToDictTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.test_replay = test_utils.get_specific_asset(filename="test_replay.json")
        cls.sc2_replay_data = SC2ReplayData.from_file(replay_filepath=cls.test_replay)

    def test_playerstats_to_dict(self):

        res_dict = playerstats_to_dict(
            tracker_events=self.sc2_replay_data.trackerEvents
        )

        # print(res_dict)

        # Type assertions for data:
        for playerID, feature_dict in res_dict.items():
            self.assertIsInstance(playerID, str)
            self.assertIsInstance(feature_dict, dict)
            for key, feature_list in feature_dict.items():
                self.assertIsInstance(key, str)
                self.assertIsInstance(feature_list, list)

    def test_playerstats_average_to_dict(self):

        res_dict = playerstats_average_to_dict(sc2_replay=self.sc2_replay_data)

        # print(res_dict)

        # Type assertions for data:
        self.assertIsInstance(res_dict, dict)
        for key, value in res_dict.items():
            self.assertIsInstance(key, str)
            self.assertIsInstance(value, dict)

    def test_average_playerstats_dataframe(self):

        ps_dict = playerstats_to_dict(tracker_events=self.sc2_replay_data.trackerEvents)
        for playerID, df_repr in ps_dict.items():
            # Initializing dataframe from dict:
            dataframe = pd.DataFrame.from_dict(df_repr)
            dict_average_repr = average_playerstats_dataframe(playerstats_df=dataframe)

            # print(dict_average_repr)

            # Type assertions for the data:
            self.assertIsInstance(playerID, str)
            for key, value in dict_average_repr.items():
                self.assertIsInstance(key, str)
                self.assertIsInstance(value, float)
