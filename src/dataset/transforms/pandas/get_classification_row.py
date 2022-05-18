from typing import Dict
from src.dataset.replay_data.sc2_replay_data import SC2ReplayData

from src.dataset.transforms.utils import (
    average_player_stats,
    select_apm_1v1,
    select_outcome,
)


def get_classification_row(sc2_replay: SC2ReplayData) -> Dict[str, int | float]:
    """
    Exposes logic for compising a row containing features for classification task.

    :param sc2_replay: Specifies the parsed structure of a replay.
    :type sc2_replay: SC2ReplayData
    :return: _description_
    :rtype: _type_
    """

    # Initializing a dict which will be used for the final dataframe:
    dataframe_row = {}

    # Select outcome:
    game_outcome = select_outcome(sc2_replay=sc2_replay)
    for player_id, outcome in game_outcome.items():
        if f"outcome_{player_id}" not in dataframe_row:
            dataframe_row[f"outcome_{player_id}"] = []
        dataframe_row[f"outcome_{player_id}"].append(outcome)

    # Selecting player APM:
    player_apm = select_apm_1v1(sc2_replay=sc2_replay)
    for player_id, apm in player_apm.items():
        if f"apm_{player_id}" not in dataframe_row:
            dataframe_row[f"apm_{player_id}"] = []
        dataframe_row[f"apm_{player_id}"].append(apm)

    # TODO: Select average PlayerStats
    player_stats = average_player_stats(tracker_events=sc2_replay.trackerEvents)

    # TODO: Return a dataframe
    # final_dataframe = pd.DataFrame().from_dict(data=dataframe_dict)

    return dataframe_row
