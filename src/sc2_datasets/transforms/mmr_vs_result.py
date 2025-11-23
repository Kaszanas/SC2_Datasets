from typing import Tuple

import torch

from sc2_datasets.replay_data.sc2_replay_data import SC2ReplayData
from sc2_datasets.transforms.utils import RESULT_DICT


def mmr_vs_result(sc2_replay: SC2ReplayData) -> Tuple[torch.Tensor, torch.Tensor]:
    """
    Changes representation from the parsed SC2ReplayData representation into
    PyTorch tensors for learning mmr vs result.

    Parameters
    ----------
    sc2_replay : SC2ReplayData
        Specifies the replay data instance.

    Returns
    -------
    Tuple[torch.Tensor, torch.Tensor]
        Returns a tensor representation for the task of trying to
        learn how mmr maps to the end result of a match.
    """
    feature_tensor = torch.tensor(
        [
            sc2_replay.toonPlayerDescMap[0].toon_player_info.APM,
            sc2_replay.toonPlayerDescMap[1].toon_player_info.APM,
        ],
        dtype=torch.float,
    )

    player_result = sc2_replay.toonPlayerDescMap[0].toon_player_info.result
    transformed_result = RESULT_DICT.get(player_result, -1)

    # Map result to label tensor
    label_tensor = torch.tensor(
        transformed_result,
        dtype=torch.int8,
    )

    return feature_tensor, label_tensor
