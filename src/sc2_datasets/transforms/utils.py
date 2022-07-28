from typing import Dict, List

import numpy as np

# pylama:ignore=E501
from sc2_datasets.replay_parser.tracker_events.events.player_stats.player_stats import (
    PlayerStats,
)
from sc2_datasets.replay_data.sc2_replay_data import SC2ReplayData


def filter_player_stats(
    sc2_replay: SC2ReplayData,
) -> Dict[str, List[PlayerStats]]:
    """
    Filters PlayerStats events and places them in lists based on the playerId

    :param sc2_replay: Specifies the replay that the outcome will be selected from.
    :type sc2_replay: SC2ReplayData
    :return: Returns a dictionary containing a mapping from playerId to the respective player stats.
    :rtype: Dict[str, List[PlayerStats]]

    **Correct Usage Examples:**

    The use of this method is intended to filter player's events from the game based on playerId

    You should set sc2_replay parameter.

    May help you in analysing on the dataset.

    The parameters should be set as in the example below.

    >>> filter_player_stats_object = filter_player_stats(
    ...        sc2_replay= sc2_replay: SC2ReplayData)

    >>> assert isinstance(sc2_replay, SC2ReplayData)

    **Incorrect Usage Examples:**

    >>> wrong_type_object = int(2)
    >>> filter_player_stats_object = filter_player_stats(
    ...        sc2_replay= wrong_type_object)
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) ...

    If you don't set parameters or paste incorect parameters' type.

    Will throw an exception if the player's id in the game is greater than 2.
    """

    player_stats_events = {"1": [], "2": []}
    # Filter PlayerStats:
    for event in sc2_replay.trackerEvents:
        if type(event).__name__ == "PlayerStats":
            if event.playerId == 1:
                player_stats_events["1"].append(event)
            elif event.playerId == 2:
                player_stats_events["2"].append(event)
            else:
                raise Exception("There are more than player in TrackerEvents!")

    return player_stats_events


def average_player_stats(
    sc2_replay: SC2ReplayData,
) -> Dict[str, List[float]]:
    """
    Exposes the logic of selecting and averaging PlayerStats events from within TrackerEvents list.

    :param sc2_replay: Specifies the replay that the outcome will be selected from.
    :type sc2_replay: SC2ReplayData
    :return: Returns a dictionary containing averaged features.
    :rtype: Dict[str, List[float]]

    **Correct Usage Examples:**

    The use of this method is intended to average stats of the player from the game.

    You should set sc2_replay parameter.

    The parameters should be set as in the example below.

    >>> average_player_stats_object = average_player_stats(
    ...        sc2_replay= sc2_replay: SC2ReplayData)

    >>> assert isinstance(sc2_replay, SC2ReplayData)

    **Incorrect Usage Examples:**

    >>> wrong_type_object = int(2)
    >>> average_player_stats_object = average_player_stats(
    ...        sc2_replay= wrong_type_object)
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) ...

    If you don't set parameters or paste incorect parameters' type.
    """

    player_stats_dict = filter_player_stats(sc2_replay=sc2_replay)

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

    :param sc2_replay: Specifies the replay that the outcome will be selected from.
    :type sc2_replay: SC2ReplayData
    :return: Returns player id to APM mapping.
    :rtype: Dict[str, int]

    **Correct Usage Examples:**

    The use of this method is intended to check the value
    of the correct APM from the selected replay.

    The parameters should be set as in the example below.

    >>> select_apm_1v1_object = select_apm_1v1(
    ...        sc2_replay= sc2_replay: SC2ReplayData)

    >>> assert isinstance(sc2_replay, SC2ReplayData)

    **Incorrect Usage Examples:**

    >>> wrong_type_object = int(2)
    >>> select_apm_1v1_object = select_apm_1v1(
    ...        sc2_replay= wrong_type_object)
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) ...

    If you don't set parameters or paste incorect parameters' type.

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

    **Correct Usage Examples:**

    The use of this method is intended to check logic value of the selected 1v1 game, lose or win

    You should set sc2_replay parameter.

    The parameters should be set as in the example below.

    >>> select_outcome_1v1_object = select_outcome_1v1(
    ...        sc2_replay= sc2_replay: SC2ReplayData)

    >>> assert isinstance(sc2_replay, SC2ReplayData)

    **Incorrect Usage Examples:**

    >>> wrong_type_object = int(2)
    >>> select_outcome_1v1_object = select_outcome_1v1(
    ...        sc2_replay= wrong_type_object)
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) ...

    If you don't set parameters or paste incorect parameters' type.
    """

    player_outcome = {"1": 0, "2": 0}

    result_dict = {"Loss": 0, "Win": 1}
    for toon_desc_map in sc2_replay.toonPlayerDescMap:
        result = result_dict[toon_desc_map.toon_player_info.result]
        player_outcome[toon_desc_map.toon_player_info.playerID] = result

    return player_outcome
