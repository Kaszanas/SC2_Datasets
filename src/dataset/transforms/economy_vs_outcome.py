from typing import Dict, List, Tuple

import functools
import numpy as np
import torch

from src.dataset.replay_data.replay_parser.tracker_events.tracker_event import (
    TrackerEvent,
)

from src.dataset.replay_data.sc2_replay_data import SC2ReplayData

from src.dataset.replay_data.replay_parser.tracker_events.events.player_stats.player_stats import (
    PlayerStats,
)


def filter_player_stats(
    player_tracker_events: List[TrackerEvent],
) -> Dict[str, List[PlayerStats]]:
    """
    _summary_

    :param player_tracker_events: _description_
    :type player_tracker_events: List[TrackerEvent]
    :return: _description_
    :rtype: Dict[str, List[PlayerStats]]
    """
    player_stats_events = {"1": [], "2": []}
    # Filter PlayerStats:
    for event in player_tracker_events:
        if type(event).__name__ == "PlayerStats":
            if event.playerId == 1:
                player_stats_events["1"].append(event)
            if event.playerId == 2:
                player_stats_events["2"].append(event)

    return player_stats_events


def average_player_stats(
    player_tracker_events: List[TrackerEvent],
) -> Dict[str, List[float]]:
    """
    _summary_

    :param player_tracker_events: _description_
    :type player_tracker_events: List[TrackerEvent]
    :return: _description_
    :rtype: Dict[str, List[float]]
    """

    player_stats_dict = filter_player_stats(player_tracker_events=player_tracker_events)

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


def economy_average_vs_outcome(
    sc2_replay: SC2ReplayData,
) -> Tuple[torch.Tensor, int]:
    """
    Transform that exposes logic for obtaining averaged economy statistics.

    :param sc2_replay: Specifies the parsed structure of a replay.
    :type sc2_replay: SC2ReplayData
    :return: Returns a tensor containing features and a target.
    :rtype: Tuple[torch.Tensor, torch.Tensor]
    """

    average_player_features = average_player_stats(
        player_tracker_events=sc2_replay.trackerEvents
    )
    feature_list = [
        player_features for player_features in average_player_features.values()
    ]

    # Creating feature tensor:
    feature_tensor = torch.tensor(feature_list, dtype=torch.float32)

    result_dict = {"Loss": 0, "Win": 1}
    target = result_dict[sc2_replay.toonPlayerDescMap[0].toon_player_info.result]

    return feature_tensor, target
