from typing import Dict, List
import pandas as pd
from IPython.display import display


def groupby_fields_mean(
    data: pd.DataFrame,
    fields: List[str],
    unique_field: str = "game_hash",
) -> Dict[str, pd.DataFrame]:
    """
    Helper function exposing logic for performing multiple groupby operations on a pandas dataframe.
    Returns a result as a dictionary.

    Example output:
    {
        "field1": pd.DataFrame,
        "field2": pd.DataFrame
    }

    :param data: Specifies the dataframe that is the input data which will be used for the groupby operation.
    :type data: pd.DataFrame
    :param fields: Specifies the columns that will act as a single groupby items.
    :type fields: List[str]
    :param fields: Specifies Specifies which columns should be dropped.
    :type fields: List[str]
    :param unique_field: Specifies one unique field which will be duplicate for both of the players, defaults to "game_hash"
    :type unique_field: str, optional
    :return: Returns a mapping of field name to result grouped dictionary.
    :rtype: Dict[str, pd.DataFrame]
    """

    result_dict = {}
    for field in fields:

        # Group the data by fields and reset index:
        grouped_data = data.groupby([unique_field, field]).mean()
        grouped_data = grouped_data.reset_index()

        # Add to result:
        result_dict[field] = grouped_data

    return result_dict
