from typing import Dict, List

import numpy as np

from src.dataset.replay_data.replay_parser.tracker_events.tracker_event import (
    TrackerEvent,
)
from src.dataset.transforms.utils import filter_player_stats


def average_player_stats_to_row(
    tracker_events: List[TrackerEvent],
) -> Dict[str, List[float]]:
    """
    Exposes the logic of selecting and averaging PlayerStats events from within TrackerEvents list and returns a dictionary that can be treated as a pandas dataframe row.

    :param player_tracker_events: Specifies a list of TrackerEvents as parsed from original JSON files.
    :type player_tracker_events: List[TrackerEvent]
    :return: Returns a dictionary containing averaged features.
    :rtype: Dict[str, List[float]]
    """

    player_stats_dict = filter_player_stats(tracker_events=tracker_events)

    average_player_features = {}
    for playerID, list_of_events in player_stats_dict.items():
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
        average_player_features[playerID] = [
            item / len(list_of_events) for item in sum_of_features
        ]

    return average_player_features
