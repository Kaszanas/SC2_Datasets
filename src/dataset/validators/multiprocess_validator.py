from pathlib import Path
from typing import List, Set, Tuple
from concurrent.futures import ProcessPoolExecutor
from tqdm import tqdm

from src.dataset.utils.sc2_replay_file_info.sc2_replay_file_info import (
    SC2ReplayFileInfo,
)
from src.dataset.validators.integrity_validator import validate_chunk
from src.dataset.validators.validator_utils import (
    read_validation_file,
    save_validation_file,
)


# REVIEW: Verify this:
def validate_replays_integrity_mp(
    list_of_replays: List[SC2ReplayFileInfo],
    n_workers: int,
) -> Tuple[Set[SC2ReplayFileInfo], Set[SC2ReplayFileInfo]]:
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

    futures = []
    # Iterate and submit jobs to the ProcessPoolExecutor:
    with ProcessPoolExecutor(n_workers) as exe:
        for index in range(0, len(list_of_replays), chunksize):
            filenames = list_of_replays[index : (index + chunksize)]
            futures.append(exe.submit(validate_chunk, filenames))

    # Calculate results from futures:
    result = []
    for future in tqdm(futures, desc=f"Validating files: "):
        result.extend(future.result())

    # Convert result to two sets:
    validated = set()
    skip_files = set()
    for sc2_file_info, is_correct in result:
        if is_correct:
            validated.add(sc2_file_info)
        if not is_correct:
            skip_files.add(sc2_file_info)

    return (validated, skip_files)


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
    # TODO: Pass skip files here so that they can be expanded?
    validated_replays, skip_files = validate_replays_integrity_mp(
        list_of_replays=list(files_to_validate), n_workers=n_workers
    )

    # Save to a file:
    save_validation_file(
        validated_files=list(validated_replays),
        skip_files=skip_files,
        path=validation_file_path,
    )

    return skip_files
