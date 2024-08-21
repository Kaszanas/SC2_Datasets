from typing import Tuple

import torch

from sc2_datasets.replay_data.sc2_replay_data import SC2ReplayData
from sc2_datasets.transforms.utils import average_player_stats


def economy_average_vs_outcome(
    sc2_replay: SC2ReplayData,
) -> Tuple[torch.Tensor, int]:
    """
    Transforms the SC2ReplayData representation into averaged economy statistics
    and maps the winner and loser of the match.

    Parameters
    ----------
    sc2_replay : SC2ReplayData
        Specifies the parsed structure of a replay.

    Returns
    -------
    Tuple[torch.Tensor, torch.Tensor]
        Returns a tensor containing features and a target.

    Examples
    --------
    **Correct Usage Examples:**

    This method may help you to operate with data on the game replay.
    Obtains averaged ecomomy statistics.

    You should set sc2_replay parameter.

    The parameters should be set as in the example below.

    >>> economy_average_vs_outcome_object = economy_average_vs_outcome(
    ...        sc2_replay= sc2_replay: SC2ReplayData)

    >>> assert isinstance(sc2_replay, SC2ReplayData)

    **Incorrect Usage Examples:**

    >>> wrong_type_object = int(2)
    >>> economy_average_vs_outcome_object = economy_average_vs_outcome(
    ...        sc2_replay= wrong_type_object)
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) ...

    If you don't set parameters or paste incorect parameters' type.
    """

    average_player_features = average_player_stats(sc2_replay)
    feature_list = [
        player_features for player_features in average_player_features.values()
    ]

    # Creating feature tensor:
    feature_tensor = torch.tensor(feature_list, dtype=torch.float32)

    result_dict = {"Loss": 0, "Win": 1, "Victory": 1, "Defeat": 0}
    target = result_dict[sc2_replay.toonPlayerDescMap[0].toon_player_info.result]

    return feature_tensor, target
