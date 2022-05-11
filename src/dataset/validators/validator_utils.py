from pathlib import Path
from typing import Set, Tuple

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
    with path.open(mode="w+", encoding="utf-8") as input_file:
        try:
            # Try reading the data from JSON:
            json_data = json.load(input_file)
            validated_file_list = json_data["validated_files"]
            skip_file_list = json_data["skip_files"]
        except:
            # If there is no content in the file, initlialize empty lists and write them to file:
            initialize_content = {"validated_files": [], "skip_files": []}
            json.dump(initialize_content, input_file)
            validated_file_list = []
            skip_file_list = []

    # REVIEW: This is memory inefficient for sure:
    # Converting filepaths to SC2ReplayFileInfo:
    skip_file_str_to_paths = [Path(i_file) for i_file in skip_file_list]
    skip_file_list = [
        SC2ReplayFileInfo(directory=i_path.parent, filename=i_path.name)
        for i_path in skip_file_str_to_paths
    ]

    # REVIEW: This is probably inefficient too:
    return (set(validated_file_list), set(skip_file_list))


# REVIEW: Verify this:
def save_validation_file(
    validated_files: Set[SC2ReplayFileInfo],
    skip_files: Set[SC2ReplayFileInfo],
    path: Path = Path("validator_file.json"),
) -> None:
    """
    Attempts to save the validation file to a specified path

    :param validated_files: Specifies the list of replays that were verified as ones that were processed.
    :type validated_files: Set[SC2ReplayFileInfo]
    :param skip_files: Specifies the list of replays that were verified as ones that should be skipped.
    :type skip_files: Set[SC2ReplayFileInfo]
    :param path: Specifies the path to the file that will be saved, Defaults to Path("validator_file.json")
    :type path: Path
    """

    # Converting incorrect files to Paths:
    validated_file_list = [
        Path(file.get_full_path()).as_posix() for file in list(validated_files)
    ]
    skip_file_list = [
        Path(file.get_full_path()).as_posix() for file in list(skip_files)
    ]
    # Initializing the dict that will be serialized to a file:
    file_dict = {
        "validated_files": validated_file_list,
        "skip_files": skip_file_list,
    }
    with open(path, mode="w", encoding="utf-8") as output_file:
        print(output_file)
        json.dump(file_dict, output_file)
