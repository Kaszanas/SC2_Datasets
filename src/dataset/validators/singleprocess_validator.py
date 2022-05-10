# REVIEW: Verify this:
from pathlib import Path
from typing import List, Set
from src.dataset.utils.sc2_replay_file_info.sc2_replay_file_info import (
    SC2ReplayFileInfo,
)
from src.dataset.validators.integrity_validator import validate_chunk
from src.dataset.validators.validator_utils import (
    read_validation_file,
    save_validation_file,
)


def validate_integrity_persist_sp(
    list_of_replays: List[SC2ReplayFileInfo],
    validation_file_path: Path,
) -> Set[SC2ReplayFileInfo]:
    """
    Exposes the logic for validating replays using a single process.
    This function uses a validation file that persists the files which were previously checked.

    :param list_of_replays: Specifies the list of replays that are supposed to be validated.
    :type list_of_replays: List[SC2ReplayFileInfo]
    :param validation_file_path: Specifies the path to the validation file which will be read to obtain the
    :type validation_file_path: Path
    :return: Returns a set of files that should be skipped in further processing.
    :rtype: Set[SC2ReplayFileInfo]
    """

    # Try reading from a file:
    validated_files, skip_files = read_validation_file(path=validation_file_path)

    # Validate replays:
    files_to_validate = set(list_of_replays) - validated_files
    # TODO: Pass skip files here so that they can be expanded?
    skip_files = validate_integrity_sp(list_of_replays=list(files_to_validate))

    # Save to a file:
    save_validation_file(file_list=list(validated_replays), path=validation_file_path)

    return skip_files


def validate_integrity_sp(
    list_of_replays: List[SC2ReplayFileInfo],
) -> Set[SC2ReplayFileInfo]:
    """
    Exposes logic for single process integrity validation of a replay.

    :param list_of_replays: Specifies the SC2ReplayInfo information of the files that will be validated.
    :type list_of_replays: List[SC2ReplayFileInfo]
    :return: Returns a list of replays that did not pass the validation.
    :rtype: Set[SC2ReplayFileInfo]
    """

    # TODO: Convert this!
    validated_files = validate_chunk(list_of_replays=list_of_replays)

    return validated_files
