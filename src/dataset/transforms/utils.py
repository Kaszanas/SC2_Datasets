from typing import Dict, List
import functools

import numpy as np


from src.dataset.replay_data.replay_parser.tracker_events.events.player_stats.player_stats import (
    PlayerStats,
)
from src.dataset.replay_data.replay_parser.tracker_events.tracker_event import (
    TrackerEvent,
)
from src.dataset.replay_data.sc2_replay_data import SC2ReplayData


def filter_player_stats(
    tracker_events: List[TrackerEvent],
) -> Dict[str, List[PlayerStats]]:
    """
    Filters PlayerStats events and places them in lists based on the playerId

    :param player_tracker_events: Specifies a list of TrackerEvent instances as parsed from the original JSON files.
    :type player_tracker_events: List[TrackerEvent]
    :return: Returns a dictionary containing a mapping from playerId to the respective player stats.
    :rtype: Dict[str, List[PlayerStats]]
    """
    player_stats_events = {"1": [], "2": []}
    # Filter PlayerStats:
    for event in tracker_events:
        if type(event).__name__ == "PlayerStats":
            if event.playerId == 1:
                player_stats_events["1"].append(event)
            if event.playerId == 2:
                player_stats_events["2"].append(event)

    return player_stats_events


def average_player_stats(
    tracker_events: List[TrackerEvent],
) -> Dict[str, List[float]]:
    """
    Exposes the logic of selecting and averaging PlayerStats events from within TrackerEvents list.

    :param player_tracker_events: Specifies a list of TrackerEvents as parsed from original JSON files.
    :type player_tracker_events: List[TrackerEvent]
    :return: Returns a dictionary containing averaged features.
    :rtype: Dict[str, List[float]]
    """

    player_stats_dict = filter_player_stats(tracker_events=tracker_events)

    average_player_features = {}
    for key, list_of_events in player_stats_dict.items():
        # Summing all of the features that are within Stats that is held in PlayerStats:
        sum_of_features = list(list_of_events[0].stats.__dict__.values())
        for index, player_stats in enumerate(list_of_events):
            if index == 0:
                continue
            sum_of_features = np.add(
                sum_of_features, list(player_stats.stats.__dict__.values())
            )

        # TODO: Verify if this is not better than the above iterative approach to summing features:
        # sum_of_features = functools.reduce(
        #     np.add, [elem.stats.__dict__.values() for elem in list_of_events]
        # )

        # Getting the average of the features:
        average_player_features[key] = [
            item / len(list_of_events) for item in sum_of_features
        ]

    return average_player_features


def select_apm_1v1(sc2_replay: SC2ReplayData) -> Dict[str, int]:
    """
    Exposes logic for selecting APM from replay data.

    :return: Returns player id to APM mapping.
    :rtype: Dict[str, int]
    """

    # Initializing dictionary for holding APM:
    player_apm = {"1": 0, "2": 0}

    # Selecting from sc2_replay and placing it in the dictionary:
    for toon_desc_map in sc2_replay.toonPlayerDescMap:
        apm = toon_desc_map.toon_player_info.APM
        player_apm[toon_desc_map.toon_player_info.playerID] = apm

    return player_apm


def select_outcome_1v1(sc2_replay: SC2ReplayData) -> Dict[str, int]:
    """
    Exposes logic for selecting game outcome of a 1v1 game. Maps loss to 0, and win to 1

    :param sc2_replay: Specifies the replay that the outcome will be selected from.
    :type sc2_replay: SC2ReplayData
    :return: Returns a dictionary mapping loss to 0, and win to 1 for playerIDs
    :rtype: Dict[str, int]
    """

    player_outcome = {"1": 0, "2": 0}

    result_dict = {"Loss": 0, "Win": 1}
    for toon_desc_map in sc2_replay.toonPlayerDescMap:
        result = result_dict[toon_desc_map.toon_player_info.result]
        player_outcome[toon_desc_map.toon_player_info.playerID] = result

    return player_outcome
