from typing import List, Dict

import pandas as pd

from src.dataset.replay_data.replay_parser.tracker_events.tracker_event import (
    TrackerEvent,
)
from src.dataset.replay_data.sc2_replay_data import SC2ReplayData
from src.dataset.transforms.utils import filter_player_stats

# TODO: Document this:
# TODO: Consider renaming:
def average_playerstats_to_dict(sc2_replay: SC2ReplayData) -> Dict[str, float]:

    playerstats_dataframe = playerstats_to_dataframe(
        tracker_events=sc2_replay.trackerEvents
    )

    dict_average_repr = average_playerstats_dataframe(
        playerstats_df=playerstats_dataframe
    )

    return dict_average_repr


# REVIEW: This needs to be reviewed:
# TODO: Consider renaming:
def playerstats_to_dict(
    tracker_events: List[TrackerEvent],
) -> Dict[str, int]:
    """
    Exposes a logic of converting a single list of TrackerEvents to a dictionary representation
    of the data that can be used to initialize a pandas DataFrame.

    Example return:
    {"gameloop_1": [1,2],
     "gameloop_2": [1,2],
     "army_1": [120, 250],
     "army_2: [50, 300]}

    :param tracker_events: Specifies the list of TrackerEvents to be converted.
    :type tracker_events: List[TrackerEvent]
    :return: Returns a dictionary of features.
    :rtype: Dict[str, int]
    """

    dataframe_representation = {}
    player_stats_dict = filter_player_stats(tracker_events=tracker_events)
    # Iterating over playrs and their list of events:
    for playerID, list_of_events in player_stats_dict.items():
        for event in list_of_events:
            # Adding the information about event gameloop to the dataframe representation:
            gameloop_playerID = f"gameloop_{playerID}"
            if gameloop_playerID not in dataframe_representation:
                dataframe_representation[gameloop_playerID] = []
            dataframe_representation[gameloop_playerID].append(event.loop)
            # Iterating over features:
            for feature_name, feature_value in event.stats.__dict__.items():
                feature_name_playerID = f"{feature_name}_{playerID}"
                # Constructing dataframe rows:
                if feature_name_playerID not in dataframe_representation:
                    dataframe_representation[feature_name_playerID] = []
                dataframe_representation[feature_name_playerID].append(feature_value)

    return dataframe_representation


# TODO: Consider renaming:
def playerstats_to_dataframe(
    tracker_events: List[TrackerEvent],
) -> pd.DataFrame:
    """
    Exposes the logic of selecting and averaging PlayerStats events from within TrackerEvents list and returns a dictionary that can be treated as a pandas dataframe row.

    :param player_tracker_events: Specifies a list of TrackerEvents as parsed from original JSON files.
    :type player_tracker_events: List[TrackerEvent]
    :return: Returns a dataframe representation of a game.
    :rtype: pd.DataFrame
    """

    # Getting the dataframe representation from tracker events:
    dataframe_representation = playerstats_to_dict(tracker_events=tracker_events)
    # Initializing dataframe from dict:
    dataframe = pd.DataFrame.from_dict(dataframe_representation)

    return dataframe


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
