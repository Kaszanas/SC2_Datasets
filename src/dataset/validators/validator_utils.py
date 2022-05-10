from pathlib import Path
from typing import List, Set, Tuple

from src.dataset.utils.sc2_replay_file_info.sc2_replay_file_info import (
    SC2ReplayFileInfo,
)


import json

# REVIEW: Verify this:
def read_validation_file(
    path: Path,
) -> Tuple[Set[SC2ReplayFileInfo], Set[SC2ReplayFileInfo]]:
    """
    Attempts to read the validation file from a specified path

    :param path: Specifies the path that will be used to read the validation file.
    :type path: Path
    :return: Returns a list of files that were validated as ones that should be skipped.
    :rtype: List[SC2ReplayFileInfo]
    """

    # Reading the file:
    with path.open(mode="r") as input_file:
        json_data = json.load(input_file)

        validated_file_list = json_data["validated_files"]
        skip_file_list = json_data["skip_files"]

    # REVIEW: This is memory inefficient for sure:
    # Converting filepaths to SC2ReplayFileInfo:
    skip_file_str_to_paths = [Path(i_file) for i_file in skip_file_list]
    skip_file_list = [
        SC2ReplayFileInfo(directory=i_path.parent, filename=i_path.name)
        for i_path in skip_file_str_to_paths
    ]

    # REVIEW: This is probably inefficient too:
    return set(validated_file_list), set(skip_file_list)


# REVIEW: Verify this:
def save_validation_file(
    file_set: Set[SC2ReplayFileInfo],
    skip_files: Set[SC2ReplayFileInfo],
    path: Path = Path("validator_file.json"),
) -> None:
    """
    Attempts to save the validation file to a specified path

    :param path: Specifies the path to the file that will be saved.
    :type path: Path
    :param file_list: Specifies the list of replays that were verified as ones that should be skipped, Defaults to Path("validator_file.json").
    :type file_list: List[SC2ReplayFileInfo]
    """

    file_list = list(file_set)
    # Converting incorrect files to Paths:
    path_file_list = [Path(file.get_full_path()) for file in file_list]
    # Initializing the dict that will be serialized to a file:
    file_dict = {
        "validated_files": list(path_file_list),
        "skip_files": list(skip_files),
    }
    with path.open(mode="w") as output_file:
        json.dump(file_dict, output_file)
