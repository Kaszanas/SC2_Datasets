from pathlib import Path
from typing import List, Set, Tuple

from sc2_datasets.validators.validate_chunk import validate_chunk
from sc2_datasets.validators.validator_utils import (
    read_validation_file,
    save_validation_file,
)


# REVIEW: This function:
# TODO: Add temporary files to be used as a validator file:
def validate_integrity_persist_sp(
    list_of_replays: List[str],
    validation_file_path: Path,
) -> Set[str]:
    """
    Exposes the logic for validating replays using a single process.
    This function uses a validation file that persists the files which were previously checked.

    :param list_of_replays: Specifies the list of replays that are supposed to be validated.
    :type list_of_replays: List[str]
    :param validation_file_path: Specifies the path to the validation file\
    which will be read to obtain the
    :type validation_file_path: Path
    :return: Returns a set of files that should be skipped in further processing.
    :rtype: Set[str]

    **Correct Usage Examples:**

    Persistent validators save the validation information to a specified filepath.
    Only the files that ought to be skipped are returned as a set from this function.

    >>> from pathlib import Path
    >>> replays_to_skip = validate_integrity_persist_sp(
    ...                         list_of_replays=[
    ...                               "test/test_files/single_replay/test_replay.json",
    ...                               "test/test_files/single_replay/test_bit_flip_example.json"],
    ...                         validation_file_path=Path("validator_file.json"))
    >>> assert len(replays_to_skip) == 1
    """

    # Reading from a file:
    read_validated_files, read_skip_files = read_validation_file(
        path=validation_file_path
    )

    # Validate only the files we haven't already validated:
    files_to_validate = set(list_of_replays) - read_validated_files - read_skip_files
    # TODO: Consider changing the input param to set
    # Perform the validation:
    validated_files, skip_files = validate_integrity_sp(
        list_of_replays=list(files_to_validate)
    )

    # Updating the sets of validated and skip_files:
    read_validated_files.update(validated_files)
    read_skip_files.update(skip_files)

    # Save to a file:
    save_validation_file(
        validated_files=read_validated_files,
        skip_files=read_skip_files,
        path=validation_file_path,
    )

    return read_skip_files


def validate_integrity_sp(
    list_of_replays: List[str],
) -> Tuple[Set[str], Set[str]]:
    """
    Exposes logic for single process integrity validation of a replay.

    :param list_of_replays: Specifies the SC2ReplayInfo information\
    of the files that will be validated.
    :type list_of_replays: List[str]
    :return: Returns a tuple that contains (validated replays, files to be skipped).
    :rtype: Tuple[Set[str], Set[str]]

    **Correct Usage Examples:**

    Validators can be used to check if a file is correct before loading it for some modeling task.
    Below you will find a sample execution which
    should contain one correct file and one incorrect file.
    This results in the final tuple containing two sets.
    The first tuple denotes correctly validated files,
    whereas the second tuple denotes the files that should be skipped in modeling tasks.

    >>> validated_replays = validate_integrity_sp(
    ...                         list_of_replays=[
    ...                               "./test/test_files/single_replay/test_replay.json",
    ...                               "./test/test_files/single_replay/test_bit_flip_example.json"])
    >>> assert len(validated_replays[0]) == 2
    >>> assert len(validated_replays[1]) == 1
    """

    # TODO: Convert this!
    validated_files = validate_chunk(list_of_replays=list_of_replays)

    # REVIEW: revisit
    # Convert result to two sets:
    validated = set()
    skip_files = set()
    for sc2_file_info, is_correct in validated_files:
        if is_correct:
            validated.add(sc2_file_info)
        else:
            skip_files.add(sc2_file_info)

    return (validated, skip_files)
