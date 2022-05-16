from pathlib import Path
from typing import List, Set, Tuple
from concurrent.futures import ProcessPoolExecutor
from tqdm import tqdm

from src.dataset.validators.validate_chunk import validate_chunk
from src.dataset.validators.validator_utils import (
    read_validation_file,
    save_validation_file,
)


def validate_integrity_mp(
    list_of_replays: List[str],
    n_workers: int,
) -> Tuple[Set[str], Set[str]]:
    """
    Exposes logic for multiprocess validation of the replays.
    Validates if the replay can be parsed by using SC2ReplayData by spawning multiple processes.

    :param list_of_replays: Specifies a list of replays.
    :type list_of_replays: List[str]
    :param n_workers: Specifies the number of workers (processes) that will be used for validating replays.
    :type n_workers: int
    :return: Returns a tuple that contains (validated replays, files to be skipped).
    :rtype: Tuple[Set[str], Set[str]]
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
        else:
            skip_files.add(sc2_file_info)

    return (validated, skip_files)


def validate_integrity_persist_mp(
    list_of_replays: List[str],
    n_workers: int,
    validation_file_path: Path = Path("validator_file.json"),
) -> Set[str]:
    """
    Exposes the logic for validating replays using multiple processes.
    This function uses a validation file that persists the files which were previously checked.

    :param list_of_replays: Specifies the list of replays that are supposed to be validated.
    :type list_of_replays: List[str]
    :param n_workers: Specifies the number of workers that will be used to validate the files.
    :type n_workers: int
    :param validation_file_path: Specifies the path to the validation file which will be read to obtain the
    :type validation_file_path: Path
    :return: Returns a set of files that should be skipped in further processing.
    :rtype: Set[str]
    """

    # Reading from a file:
    read_validated_files, read_skip_files = read_validation_file(
        path=validation_file_path
    )

    # Validate replays:
    files_to_validate = set(list_of_replays) - read_validated_files
    validated_files, skip_files = validate_integrity_mp(
        list_of_replays=list(files_to_validate), n_workers=n_workers
    )

    # Updating the sets of validated and skip_files:
    read_validated_files.update(validated_files)
    read_skip_files.update(skip_files)

    # Saving to a file:
    save_validation_file(
        validated_files=read_validated_files,
        skip_files=read_skip_files,
        path=validation_file_path,
    )

    return skip_files
