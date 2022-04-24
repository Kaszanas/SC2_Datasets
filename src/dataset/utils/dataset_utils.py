import json
import os

from concurrent.futures import ProcessPoolExecutor
from src.dataset.replay_data.sc2_replay_data import SC2ReplayData
from src.dataset.utils.zip_utils import unpack_zipfile
from tqdm import tqdm

from typing import Callable, Dict, List, Set, Tuple


def load_replaypack_information(
    replaypack_name: str, replaypack_path: str, unpack_n_workers: int
) -> Tuple[str, Dict[str, str], Dict[str, str]]:
    """
    Helper function that loads replaypack information from a standard directory structure.

    :param replaypack_name: Specifies the replaypack name that will be used as a subdirectory where replaypack .json files will be extracted.
    :type replaypack_name: str
    :param replaypack_path: Specifies the path to the extracted replaypack.
    :type replaypack_path: str
    :param unpack_n_workers: Specifies the number of workers that will be used for unpacking the archive.
    :type unpack_n_workers: int
    :return: Returns path to the directory that contains .json files with data extracted from replays,
            summary information that was generated when extracting the data from replays,
            mapping information that specifies what was the directory structure pre-extraction, and log file which contaions how many files were successfully extracted.
    :rtype: Tuple[str, Dict[str, str], Dict[str, str]]
    """

    replaypack_files = os.listdir(replaypack_path)
    # Initializing variables that should be returned:
    data_path = ""
    summary_content = {}
    mapping_content = {}
    processed_info = {}

    # Extracting the nested .zip files,
    # and loading replaypack information files:
    # REVIEW: Check the logic for unpacking and the loading of supplementary files:
    for file in replaypack_files:
        if file.endswith("_data.zip"):
            data_path = os.path.join(replaypack_path, replaypack_name + "_data")
            # Unpack the .zip archive only if it is not unpacked already:
            if not os.path.isdir(data_path):
                data_path = unpack_zipfile(
                    destination_dir=replaypack_path,
                    subdir=replaypack_name + "_data",
                    zip_path=os.path.join(replaypack_path, file),
                    n_workers=unpack_n_workers,
                )
        if file.endswith("_summary.json"):
            with open(os.path.join(replaypack_path, file)) as summary_file:
                summary_content = json.load(summary_file)
        if file.endswith("_mapping.json"):
            with open(os.path.join(replaypack_path, file)) as mapping_file:
                mapping_content = json.load(mapping_file)
        if file.endswith(".log") and not file.endswith("main_log.log"):
            with open(os.path.join(replaypack_path, file)) as processed_info_file:
                processed_info = json.load(processed_info_file)

    return (data_path, summary_content, mapping_content, processed_info)


def validate_chunk(
    list_of_replays: List[Tuple[str, str]],
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
    list_of_replays: List[Tuple[str, str]],
    n_workers: int,
) -> Set[str]:
    """
    _summary_

    :param list_of_replays: _description_
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
        result = result + future.result()

    return result


def validate_integrity_singleprocess(list_of_replays: List[Tuple[str, str]]):
    return validate_chunk(list_of_replays)
