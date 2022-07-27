from typing import Any, List, Dict

import pandas as pd

from sc2_datasets.replay_data.sc2_replay_data import SC2ReplayData

from sc2_datasets.transforms.utils import filter_player_stats


# TODO: Document this:
# TODO: Consider renaming:
# REVIEW: Verify this code!
def playerstats_average_to_dict(sc2_replay: SC2ReplayData) -> Dict[str, float]:

    """
    Exposes a logic of converting a single list of TrackerEvents to a dictionary representation
    of the data that can be used to initialize a pandas DataFrame.

    :param sc2_replay: Specifies a dataframe that will be averaged.
    :type sc2_replay: SC2ReplayData
    :return: Returns a dictionary representation of the averaged values.
    :rtype: Dict[str, float]

    **Correct Usage Examples:**

    This method may help you to operate with data on the game replay.

    Can be used for converting average player statistics to the dictionary representation.

    Then you can use it for DataFrame initialization in pandas.

    You should set sc2_replay parameter.

    The parameters should be set as in the examples below.

    >>> playerstats_average_to_dict_object = playerstats_average_to_dict(
    ...        sc2_replay= sc2_replay: SC2ReplayData)

    >>> assert isinstance(sc2_replay, SC2ReplayData)

    **Incorrect Usage Examples:**

    >>> wrong_type_object = int(2)
    >>> playerstats_average_to_dict_object = playerstats_average_to_dict(
    ...        sc2_replay= wrong_type_object)
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) ...

    If you don't set parameters or paste incorect parameters' type.
    """

    final_dict_average = {}

    # Getting the dataframe representation from tracker events:
    playerID_df_repr = playerstats_to_dict(sc2_replay=sc2_replay)
    for playerID, df_repr in playerID_df_repr.items():
        # Initializing dataframe from dict:
        dataframe = pd.DataFrame.from_dict(df_repr)
        dict_average_repr = average_playerstats_dataframe(playerstats_df=dataframe)

        if playerID not in final_dict_average:
            final_dict_average[playerID] = dict_average_repr

    return final_dict_average


# REVIEW: This needs to be reviewed:
# TODO: Consider renaming:
def playerstats_to_dict(
    sc2_replay: SC2ReplayData,
    additional_data_dict: Dict[str, Dict[str, Any]] = {},
) -> Dict[str, Dict[str, List[Any]]]:
    """
    Exposes a logic of converting a single list of TrackerEvents to a dictionary representation
    of the data that can be used to initialize a pandas DataFrame.

    Example additional_data_dict:
    {"1": {
            "outcome": 1
          }
    "2": {
            "outcome": 0
         }
    }

    Example return:
    Without additional data:
    {"1": {"gameloop": [1,2],
           "army": [120, 250]},
     "2": {"gameloop": [1,2],
           "army: [50, 300]}
    }

    With additional data (1 denoting a victory, 0 denoting a loss):
    {"1": {"gameloop": [1,2],
           "army": [120, 250],
           "outcome": [1, 1]},
     "2": {"gameloop": [1,2],
           "army: [50, 300],
           "outcome": [0, 0]}
    }

    :param sc2_replay: Specifies a replay that will be used to obtain
    the list of TrackerEvents to be converted.
    :type sc2_replay: SC2ReplayData
    :return: Returns a dictionary of features with additional information
    repeated for all of the occurences of events.
    :rtype: Dict[str, Dict[str, List[Any]]]

    **Correct Usage Examples:**

    This method may help you to operate with data on the game replay.

    Can be used for converting list to the dictionary representation.

    Then you can use it for DataFrame initialization in pandas.

    You should set sc2_replay parameter.

    The parameters should be set as in the examples below.

    >>> playerstats_to_dict_object = playerstats_to_dict(
    ...        sc2_replay= sc2_replay:SC2ReplayData)

    >>> assert isinstance(sc2_replay, SC2ReplayData)


    Prameter named 'additional_data_dict' is optional, you can leave it blank.

    If you want to use this parameter, be sure that your parameter looks similar as in the example.

    >>> additional_data = {
    ...        "1": {"outcome": 1},
    ...        "2": {"outcome": 2},
    ...     }

    >>> playerstats_to_dict_object = playerstats_to_dict(
    ...        sc2_replay= sc2_replay: SC2ReplayData,
    ...        additional_data_dict = additional_data: Dict)

    >>> assert isinstance(sc2_replay, SC2ReplayData)
    >>> assert isinstance(additional_data_dict, Dict)

    **Incorrect Usage Examples:**

    >>> wrong_type_object = int(2)
    >>> playerstats_to_dict_object = playerstats_to_dict(
    ...        sc2_replay= sc2_replay,
    ...        additional_data_dict = wrong_type_object)
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) ...

    If you don't set parameters or paste incorect parameters' type.

    """

    dataframe_representation = {}
    player_stats_dict = filter_player_stats(sc2_replay=sc2_replay)
    for playerID, list_of_events in player_stats_dict.items():
        # Dataframe representation of playerID will be a dictionary
        # of feature name mapping to the value:
        if playerID not in dataframe_representation:
            dataframe_representation[playerID] = {}
        for event in list_of_events:
            # Adding gameloop information to the dict:
            if "gameloop" not in dataframe_representation[playerID]:
                dataframe_representation[playerID]["gameloop"] = []
            dataframe_representation[playerID]["gameloop"].append(event.loop)
            # Additional data needs to be added in case that there
            # can be some information that is constant throughout the game
            # This can be for example MMR of a player, APM of a player, outcome or other
            # Appending additional data:
            if additional_data_dict:
                additional_data = additional_data_dict[playerID]
                for key, additional_val in additional_data.items():
                    if key not in dataframe_representation[playerID]:
                        dataframe_representation[playerID][key] = []
                    dataframe_representation[playerID][key].append(additional_val)
            # Adding all features to the dict:
            for feature_name, feature_value in event.stats.__dict__.items():
                if feature_name not in dataframe_representation[playerID]:
                    dataframe_representation[playerID][feature_name] = []
                dataframe_representation[playerID][feature_name].append(feature_value)

    return dataframe_representation


# TODO: Consider renaming:
def average_playerstats_dataframe(playerstats_df: pd.DataFrame) -> Dict[str, float]:
    """
    Averages a game dataframe

    :param playerstats_df: Specifies a dataframe that will be averaged.
    :type playerstats_df: pd.DataFrame
    :return: Returns a dictionary representation of the averaged values.
    :rtype: Dict[str, float]

    **Correct Usage Examples:**

    This method may help you to operate with data on the game replay.
    Obtains averaged game dataframe information.

    You should set sc2_replay parameter.

    The parameters should be set as in the example below.

    >>> average_playerstats_dataframe_object = average_playerstats_dataframe(
    ...        playerstats_df= playerstats_df: pd.DataFrame)

    >>> assert isinstance(playerstats_df, pd.DataFrame)

    **Incorrect Usage Examples:**

    >>> wrong_type_object = int(2)
    >>> average_playerstats_dataframe_object = average_playerstats_dataframe(
    ...        playerstats_df= wrong_type_object)
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) ...

    If you don't set parameters or paste incorect parameters' type.

    """

    mean_playerstats = playerstats_df.mean().to_dict()

    return mean_playerstats
