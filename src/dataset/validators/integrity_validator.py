from concurrent.futures import ProcessPoolExecutor
from typing import List, Set, Tuple

from src.dataset.replay_data.sc2_replay_data import SC2ReplayData

from tqdm import tqdm

from src.dataset.utils.sc2_replay_file_info.sc2_replay_file_info import (
    SC2ReplayFileInfo,
)


def validate_chunk(
    list_of_replays: List[SC2ReplayFileInfo],
) -> Set[str]:
    """
    Attempts to parse a chunk of replays and validates the JSON structure using SC2ReplayData parser.

    :param list_of_replays: Specifies the list of replays that will be validated, first tuple element is the path, second tuple element is file.
    :type list_of_replays: List[Tuple[str, str]]
    :return: Returns a set of string of the incorrect files that need to be filtered out of the dataset.
    :rtype: Set[str]
    """
    result = set()
    for (path, file) in list_of_replays:
        try:
            replay_data = SC2ReplayData.from_file(
                replay_filepath=os.path.join(path, file)
            )
        except:
            result.add(file)

    return result


def validate_replays_integrity(
    list_of_replays: List[SC2ReplayFileInfo],
    n_workers: int,
) -> Set[str]:
    """
    Validates if the replay can be parsed by using SC2ReplayData by spawning multiple processes.

    :param list_of_replays: Specifies a list of replays. Contains directory and filename.
    :type list_of_replays: List[Tuple[str, str]]
    :param n_workers: _description_
    :type n_workers: int
    :return: _description_
    :rtype: Set[str]
    """

    chunksize = round(len(list_of_replays) / n_workers)

    # Iterate and verify:
    futures = []
    with ProcessPoolExecutor(n_workers) as exe:
        for index in tqdm(
            range(0, len(list_of_replays), chunksize),
            desc=f"Validating files: ",
        ):
            filenames = list_of_replays[index : (index + chunksize)]
            futures.append(exe.submit(validate_chunk, filenames))

    result = set()
    for future in futures:
        result.update(future.result())

    return result


def validate_integrity_singleprocess(list_of_replays: List[SC2ReplayFileInfo]):
    return validate_chunk(list_of_replays)
