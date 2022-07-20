import logging
from pathlib import Path
from typing import Set, Tuple

import json


# TODO: consider splitting file creation out from this method
def read_validation_file(
    path: Path,
) -> Tuple[Set[str], Set[str]]:
    """
    Attempts to read the validation file from a specified path

    :param path: Specifies the path that will be used to read the validation file.
    :type path: Path
    :return: Returns a list of files that were validated as ones that should be skipped.
    :rtype: List[str]

    **Correct Usage Examples:**

    This function is a helper that is required to have persistent validators which are
    able to skip the files that were previously processed.
    It is tasked with reading the validation file.
    Return of this function shoud contain information on which files were validated
    (all of the validated files), and which files ought to be skipped.

    >>> from pathlib import Path
    >>> validator_file_content = read_validation_file(path=Path("validator_file.json"))
    >>> assert len(validator_file_content[0]) == 2
    >>> assert len(validator_file_content[1]) == 1
    """

    if not path.is_file():
        with path.open(mode="w", encoding="utf-8") as input_file:
            # If there is no content in the file, initlialize empty lists and write them to file:
            initialize_content = {"validated_files": [], "skip_files": []}
            json.dump(initialize_content, input_file)

    validated_file_set = {}
    skip_file_set = {}
    # Reading the file:
    with path.open(mode="r", encoding="utf-8") as input_file:
        try:
            # Try reading the data from JSON:
            json_data = json.load(input_file)
            # Immediately converting the lists of strings denoting paths to sets:
            validated_file_set = set(json_data["validated_files"])
            skip_file_set = set(json_data["skip_files"])
        except Exception as e:
            logging.error("Error while parsing json!", exc_info=e)

    return (validated_file_set, skip_file_set)


def save_validation_file(
    validated_files: Set[str],
    skip_files: Set[str],
    path: Path = Path("validator_file.json"),
) -> None:
    """
    Attempts to save the validation file to a specified path

    :param validated_files: Specifies the list of replays that were verified\
    as ones that were processed.
    :type validated_files: Set[str]
    :param skip_files: Specifies the list of replays that were verified\
    as ones that should be skipped.
    :type skip_files: Set[str]
    :param path: Specifies the path to the file that will be saved,\
    Defaults to Path("validator_file.json")
    :type path: Path

    **Correct Usage Examples:**

    This function is a helper that is required to have persistent validators which are
    able to skip the files that were previously processed.
    It is tasked with saving the information that was processed
    by the validators so that future runs of the program can use this information.

    >>> from pathlib import Path
    >>> validated_files = {"validated_file_0.json", "validated_file_1.json"}
    >>> skip_files = {"validated_file_0.json"}
    >>> validator_file_content = save_validation_file(
    ...                                         validated_files=validated_files,
    ...                                         skip_files=skip_files)
    """

    # Gettings paths as posix to be able to serialize them:
    validated_file_list = [Path(file).as_posix() for file in validated_files]
    skip_file_list = [Path(file).as_posix() for file in skip_files]

    # Initializing the dict that will be serialized to a file:
    file_dict = {
        "validated_files": validated_file_list,
        "skip_files": skip_file_list,
    }
    with open(path, mode="w", encoding="utf-8") as output_file:
        json.dump(file_dict, output_file)
