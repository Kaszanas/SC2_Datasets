from typing import List, Dict

import pandas as pd

from src.dataset.replay_data.replay_parser.tracker_events.tracker_event import (
    TrackerEvent,
)
from src.dataset.replay_data.sc2_replay_data import SC2ReplayData
from src.dataset.transforms.utils import filter_player_stats

# TODO: Document this:
# TODO: Consider renaming:
# REVIEW: Verify this code!
def playerstats_average_to_dict(sc2_replay: SC2ReplayData) -> Dict[str, float]:

    final_dict_average = {}

    # Getting the dataframe representation from tracker events:
    playerID_df_repr = playerstats_to_dict(tracker_events=sc2_replay.trackerEvents)
    for playerID, df_repr in playerID_df_repr.items():
        # Initializing dataframe from dict:
        dataframe = pd.DataFrame.from_dict(df_repr)
        dict_average_repr = average_playerstats_dataframe(playerstats_df=dataframe)

        if playerID not in final_dict_average:
            final_dict_average[playerID] = dict_average_repr

    return final_dict_average


# REVIEW: This needs to be reviewed:
# TODO: Consider renaming:
def playerstats_to_dict(
    tracker_events: List[TrackerEvent],
) -> Dict[str, Dict[str, List[int]]]:
    """
    Exposes a logic of converting a single list of TrackerEvents to a dictionary representation
    of the data that can be used to initialize a pandas DataFrame.

    Example return:
    {"1": {"gameloop": [1,2],
           "army": [120, 250]},
     "2": {"gameloop": [1,2],
           "army: [50, 300]}
    }

    :param tracker_events: Specifies the list of TrackerEvents to be converted.
    :type tracker_events: List[TrackerEvent]
    :return: Returns a dictionary of features.
    :rtype: Dict[str, Dict[str, List[int]]]
    """

    dataframe_representation = {}
    player_stats_dict = filter_player_stats(tracker_events=tracker_events)
    for playerID, list_of_events in player_stats_dict.items():
        # Dataframe representation of playerID will be a dictionary
        # of feature name mapping to the value:
        if playerID not in dataframe_representation:
            dataframe_representation[playerID] = {}
        for event in list_of_events:
            # Adding gameloop information to the dict:
            if "gameloop" not in dataframe_representation[playerID]:
                dataframe_representation[playerID]["gameloop"] = []
            dataframe_representation[playerID]["gameloop"].append(event.loop)
            # Adding all features to the dict:
            for feature_name, feature_value in event.stats.__dict__.items():
                if feature_name not in dataframe_representation[playerID]:
                    dataframe_representation[playerID][feature_name] = []
                dataframe_representation[playerID][feature_name].append(feature_value)

    # # Iterating over playrs and their list of events:
    # for playerID, list_of_events in player_stats_dict.items():
    #     for event in list_of_events:
    #         # Adding the information about event gameloop to the dataframe representation:
    #         gameloop_playerID = f"gameloop_{playerID}"
    #         if gameloop_playerID not in dataframe_representation:
    #             dataframe_representation[gameloop_playerID] = []
    #         dataframe_representation[gameloop_playerID].append(event.loop)
    #         # Iterating over features:
    #         for feature_name, feature_value in event.stats.__dict__.items():
    #             feature_name_playerID = f"{feature_name}_{playerID}"
    #             # Constructing dataframe rows:
    #             if feature_name_playerID not in dataframe_representation:
    #                 dataframe_representation[feature_name_playerID] = []
    #             dataframe_representation[feature_name_playerID].append(feature_value)

    return dataframe_representation


# TODO: Document this:
# TODO: Consider renaming:
def average_playerstats_dataframe(playerstats_df: pd.DataFrame) -> Dict[str, float]:
    """
    _summary_

    :param playerstats_df: _description_
    :type playerstats_df: pd.DataFrame
    :return: _description_
    :rtype: Dict[str, float]
    """

    mean_playerstats = playerstats_df.mean().to_dict()

    return mean_playerstats
