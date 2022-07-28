from pathlib import Path
from typing import List, Set, Tuple
from concurrent.futures import ProcessPoolExecutor
from tqdm import tqdm

import math

from sc2_datasets.validators.validate_chunk import validate_chunk

from sc2_datasets.validators.validator_utils import (
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

    :param list_of_replays: Specifies a list of replays that should be checked by the validator.
    :type list_of_replays: List[str]
    :param n_workers: Specifies the number of workers (processes)\
    that will be used for validating replays. Must be a positive int.
    :type n_workers: int
    :return: Returns a tuple that contains (all validated replays, files to be skipped).
    :rtype: Tuple[Set[str], Set[str]]

    **Correct Usage Examples:**

    Validators can be used to check if a file is correct before
    loading it for some modeling task. Below you will find a sample
    execution that should contain one correct file and one incorrect file.
    This results in the final tuple containing two sets.
    The first tuple denotes correctly validated files,
    whereas the second tuple denotes the files that should
    be skipped in modeling tasks.

    >>> validated_replays = validate_integrity_mp(
    ...                         list_of_replays=[
    ...                               "./test/test_files/single_replay/test_replay.json",
    ...                               "./test/test_files/single_replay/test_bit_flip_example.json"],
    ...                         n_workers=1)
    >>> assert len(validated_replays[0]) == 1
    >>> assert len(validated_replays[1]) == 1

    Example using more workers than replays:

    >>> validated_replays = validate_integrity_mp(
    ...                         list_of_replays=[
    ...                               "./test/test_files/single_replay/test_replay.json",
    ...                               "./test/test_files/single_replay/test_bit_flip_example.json"],
    ...                         n_workers=8)
    >>> assert len(validated_replays[0]) == 1
    >>> assert len(validated_replays[1]) == 1

    Example showing passing an empty list to the valdation function:

    >>> validated_replays = validate_integrity_mp(
    ...                         list_of_replays=[],
    ...                         n_workers=8)
    >>> assert len(validated_replays[0]) == 0
    >>> assert len(validated_replays[1]) == 0
    """

    if n_workers <= 0:
        raise Exception("Number of workers cannot be equal or less than zero!")

    if len(list_of_replays) == 0:
        return (set(), set())

    chunksize = math.ceil(len(list_of_replays) / n_workers)

    futures = []
    # Iterate and submit jobs to the ProcessPoolExecutor:
    with ProcessPoolExecutor(n_workers) as exe:
        for index in range(0, len(list_of_replays), chunksize):
            filenames = list_of_replays[index : (index + chunksize)]
            futures.append(exe.submit(validate_chunk, filenames))

    # Calculate results from futures:
    result = []
    for future in tqdm(futures, desc="Validating files: "):
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


# REVIEW: This function:
# TODO: Add temporary files to be used as a validator file:
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
    :param validation_file_path: Specifies the path to the validation\
    file which will be read to obtain the
    :type validation_file_path: Path
    :return: Returns a set of files that should be skipped in further processing.
    :rtype: Set[str]

    **Correct Usage Examples:**

    Persistent validators save the validation information to a specified filepath.
    Only the files that ought to be skipped are returned as a set from this function.

    >>> from pathlib import Path
    >>> replays_to_skip = validate_integrity_persist_mp(
    ...                         list_of_replays=[
    ...                               "test/test_files/single_replay/test_replay.json",
    ...                               "test/test_files/single_replay/test_bit_flip_example.json"],
    ...                         n_workers=1,
    ...                         validation_file_path=Path("validator_file.json"))
    >>> assert len(replays_to_skip) == 1
    """

    # Reading from a file:
    read_validated_files, read_skip_files = read_validation_file(
        path=validation_file_path
    )

    # Validate replays:
    files_to_validate = set(list_of_replays) - read_validated_files - read_skip_files
    validated_files = set()
    skip_files = set()
    if files_to_validate:
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

    return read_skip_files
