from typing import Dict

import pandas as pd

from sc2_datasets.replay_data.sc2_replay_data import SC2ReplayData

from sc2_datasets.transforms.pandas.player_stats_to_dict import (
    playerstats_average_to_dict,
)
from sc2_datasets.transforms.utils import select_apm_1v1, select_outcome_1v1


# REVIEW: Verify this:
def avg_playerstats_pd_dict_transform(
    sc2_replay: SC2ReplayData,
) -> Dict[str, int | float]:
    """
    Exposes logic for composing a row containing features for classification task.

    :param sc2_replay: Specifies the parsed structure of a replay.
    :type sc2_replay: SC2ReplayData
    :return: Returns a dictionary representation of the averaged values.
    :rtype: Dict[str, float]

    **Correct Usage Examples:**

    This method may help you to transforming reply to the dict type.

    You should set sc2_replay parameter.

    The parameters should be set as in the example below.

    >>> avg_playerstats_pd_dict_transform_object = avg_playerstats_pd_dict_transform(
    ...        sc2_replay= sc2_replay: SC2ReplayData)

    >>> assert isinstance(sc2_replay, SC2ReplayData)

    **Incorrect Usage Examples:**

    >>> wrong_type_object = int(2)
    >>> avg_playerstats_pd_dict_transform_object = avg_playerstats_pd_dict_transform(
    ...        sc2_replay= wrong_type_object)
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) ...

    If you don't set parameters or paste incorect parameters' type.
    """

    # Select average PlayerStats
    player_stats_dict = playerstats_average_to_dict(sc2_replay=sc2_replay)
    dataframe = pd.DataFrame(player_stats_dict)

    # Select outcome and add to dataframe column:
    game_outcome = select_outcome_1v1(sc2_replay=sc2_replay)
    for player_id, outcome in game_outcome.items():
        dataframe[f"outcome_{player_id}"] = outcome

    # Select APM and add to dataframe column:
    player_apm = select_apm_1v1(sc2_replay=sc2_replay)
    for player_id, apm in player_apm.items():
        dataframe[f"apm_{player_id}"] = apm

    final_dict = dataframe.to_dict()

    return final_dict
