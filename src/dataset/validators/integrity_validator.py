from concurrent.futures import ProcessPoolExecutor
from typing import List, Set

from pathlib import Path

from tqdm import tqdm
from src.dataset.replay_data.sc2_replay_data import SC2ReplayData


from src.dataset.utils.sc2_replay_file_info.sc2_replay_file_info import (
    SC2ReplayFileInfo,
)
from src.dataset.validators.validator_utils import (
    read_validation_file,
    save_validation_file,
)


def validate_chunk(
    list_of_replays: List[SC2ReplayFileInfo],
) -> Set[SC2ReplayFileInfo]:
    """
    Attempts to parse a chunk of replays and validates the JSON structure using SC2ReplayData parser.

    :param list_of_replays: Specifies the list of replays that will be validated.
    :type list_of_replays: List[SC2ReplayFileInfo]
    :return: Returns a set of string of the incorrect files that need to be filtered out of the dataset.
    :rtype: Set[SC2ReplayFileInfo]
    """
    result = set()
    for file_info in list_of_replays:
        try:
            replay_data = SC2ReplayData.from_file(
                replay_filepath=file_info.get_full_path()
            )
        except:
            result.add(file_info)

    return result


# REVIEW: Verify this:
def validate_replays_integrity_mp(
    list_of_replays: List[SC2ReplayFileInfo],
    n_workers: int,
) -> Set[SC2ReplayFileInfo]:
    """
    Exposes logic for multiprocess validation of the replays.
    Validates if the replay can be parsed by using SC2ReplayData by spawning multiple processes.

    :param list_of_replays: Specifies a list of replays in a form of SC2ReplayFileInfo.
    :type list_of_replays: List[SC2ReplayFileInfo]
    :param n_workers: Specifies the number of workers (processes) that will be used for validating replays.
    :type n_workers: int
    :return: Returns a list of replays that did not pass the validation.
    :rtype: Set[str]
    """

    chunksize = round(len(list_of_replays) / n_workers)

    # Iterate and verify:
    futures = []
    with ProcessPoolExecutor(n_workers) as exe:
        for index in range(0, len(list_of_replays), chunksize):
            filenames = list_of_replays[index : (index + chunksize)]
            futures.append(exe.submit(validate_chunk, filenames))

    result = set()
    for future in tqdm(futures, desc=f"Validating files: "):
        result.update(future.result())

    return result


# REVIEW: Verify this:
def validate_integrity_persist_mp(
    list_of_replays: List[SC2ReplayFileInfo],
    n_workers: int,
    validation_file_path: Path("validator_file.json"),
) -> Set[SC2ReplayFileInfo]:
    """
    Exposes the logic for validating replays using multiple processes.
    This function uses a validation file that persists the files which were previously checked.

    :param list_of_replays: Specifies the list of replays that are supposed to be validated.
    :type list_of_replays: List[SC2ReplayFileInfo]
    :param n_workers: Specifies the number of workers that will be used to validate the files.
    :type n_workers: int
    :param validation_file_path: Specifies the path to the validation file which will be read to obtain the
    :type validation_file_path: Path
    :return: Returns a set of files that should be skipped in further processing.
    :rtype: Set[SC2ReplayFileInfo]
    """
    # Try reading from a file:
    validated_files, skip_files = read_validation_file(path=validation_file_path)

    # Validate replays:
    files_to_validate = set(list_of_replays) - validated_files
    validated_replays = validate_replays_integrity_mp(
        list_of_replays=list(files_to_validate), n_workers=n_workers
    )

    # TODO: Pass skip files here so that they can be expanded?
    # Save to a file:
    save_validation_file(file_list=list(validated_replays), path=validation_file_path)

    return validated_replays


# REVIEW: Verify this:
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
    validated_replays = validate_integrity_sp(list_of_replays=list(files_to_validate))

    # Save to a file:
    save_validation_file(file_list=list(validated_replays), path=validation_file_path)

    return validated_replays


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
    return validate_chunk(list_of_replays)
