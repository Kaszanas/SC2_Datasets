from typing import Tuple
import torch

from sc2_datasets.replay_data.sc2_replay_data import SC2ReplayData


def mmr_vs_result(sc2_replay: SC2ReplayData) -> Tuple[torch.Tensor, torch.Tensor]:
    """
    _summary_

    :param sc2_replay: _description_
    :type sc2_replay: SC2ReplayData
    :return: _description_
    :rtype: Tuple[torch.Tensor, torch.Tensor]
    """
    feature_tensor = torch.tensor(
        [
            sc2_replay.toonPlayerDescMap[0].toon_player_info.APM,
            sc2_replay.toonPlayerDescMap[1].toon_player_info.APM,
        ],
        dtype=torch.float,
    )

    result_dict = {"Loss": 0, "Win": 1}
    label_tensor = torch.tensor(
        result_dict[sc2_replay.toonPlayerDescMap[0].toon_player_info.result],
        dtype=torch.int8,
    )

    return feature_tensor, label_tensor
