from typing import Tuple
import torch

from src.dataset.replay_data.sc2_replay_data import SC2ReplayData

from src.dataset.replay_data.replay_parser.tracker_events.events.player_stats.player_stats import (
    PlayerStats,
)


def economy_average_vs_outcome(
    sc2_replay: SC2ReplayData,
) -> Tuple[torch.Tensor, torch.Tensor]:

    player_stats_events = []
    # Filter PlayerStats
    for event in sc2_replay.trackerEvents:
        match event:
            case PlayerStats:
                player_stats_events.append(event)

    # TODO: Create feature tensor
    feature_tensor = []

    # REVIEW: Check if this is the correct way to initialize this type of tensor:
    result_dict = {"Loss": 0, "Win": 1}
    target_tensor = torch.tensor(
        result_dict[sc2_replay.toonPlayerDescMap[0].toon_player_info.result],
        dtype=torch.int8,
    )

    return feature_tensor, target_tensor
