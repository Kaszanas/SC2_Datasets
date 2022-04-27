from concurrent.futures import ProcessPoolExecutor
from typing import List, Set, Tuple

from src.dataset.replay_data.sc2_replay_data import SC2ReplayData

from tqdm import tqdm

from src.dataset.utils.sc2_replay_file_info.sc2_replay_file_info import (
    SC2ReplayFileInfo,
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


def validate_replays_integrity(
    list_of_replays: List[SC2ReplayFileInfo],
    n_workers: int,
) -> Set[SC2ReplayFileInfo]:
    """
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


def validate_integrity_singleprocess(
    list_of_replays: List[SC2ReplayFileInfo],
) -> Set[SC2ReplayFileInfo]:
    """
    Exposes logif for single process integrity validation of a replay.

    :param list_of_replays: Specifies the SC2ReplayInfo information of the files that will be validated.
    :type list_of_replays: List[SC2ReplayFileInfo]
    :return: Returns a list of replays that did not pass the validation.
    :rtype: Set[SC2ReplayFileInfo]
    """
    return validate_chunk(list_of_replays)
