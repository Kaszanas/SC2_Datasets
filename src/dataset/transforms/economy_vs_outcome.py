from typing import Tuple
import numpy as np
import torch

from src.dataset.replay_data.sc2_replay_data import SC2ReplayData

from src.dataset.replay_data.replay_parser.tracker_events.events.player_stats.player_stats import (
    PlayerStats,
)

# REVIEW: Check this function and its application:
def economy_average_vs_outcome(
    sc2_replay: SC2ReplayData,
) -> Tuple[torch.Tensor, torch.Tensor]:
    """
    Transform that exposes logic for obtaining averaged economy statistics.

    :param sc2_replay: Specifies the parsed structure of a replay.
    :type sc2_replay: SC2ReplayData
    :return: Returns a tensor containing features and a target.
    :rtype: Tuple[torch.Tensor, torch.Tensor]
    """
    player_stats_events = []
    # Filter PlayerStats:
    for event in sc2_replay.trackerEvents:
        match event:
            case PlayerStats:
                player_stats_events.append(event)

    # Summing all of the features that are within Stats that is held in PlayerStats:
    sum_of_features = [player_stats_events[0].stats.__dict__.values()]
    for index, player_stats in enumerate(player_stats_events):
        if index == 0:
            continue
        sum_of_features = np.add(sum_of_features, player_stats.stats.__dict__.values())

    # Getting the average of the features:
    average_of_features = [item / len(player_stats_events) for item in sum_of_features]

    # Creating feature tensor:
    feature_tensor = torch.tensor(average_of_features)

    # REVIEW: Check if this is the correct way to initialize this type of tensor:
    result_dict = {"Loss": 0, "Win": 1}
    target_tensor = torch.tensor(
        result_dict[sc2_replay.toonPlayerDescMap[0].toon_player_info.result],
        dtype=torch.int8,
    )

    return feature_tensor, target_tensor
