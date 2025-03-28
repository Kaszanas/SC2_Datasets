import json
import os
from pathlib import Path
from typing import Dict, List, Tuple

from sc2_datasets.utils.zip_utils import unpack_zipfile


def load_replaypack_information(
    replaypack_path: Path,
) -> Tuple[List[Dict], Dict, Dict, Dict]:
    """
    Helper function that loads replaypack information from a standard directory structure.

    Parameters
    ----------
    replaypack_name : str
        Specifies the replaypack name that will be used\
        as a subdirectory where replaypack .json files will be extracted.
    replaypack_path : str
        Specifies the path to the extracted replaypack.

    Returns
    -------
    Tuple[List[Dict], Dict, Dict, Dict]
        Returns loaded summary information that\
        was generated when extracting the data from replays,\
        mapping information that specifies what was the directory\
        structure pre-extraction, and log file which contaions\
        how many files were successfully extracted.

    Examples
    --------
    The use of this method is intended to download a .zip replaypack
    of SC2 games and unpack the downloaded files
    to the folder.

    May help you to download and unpack downloaded files.

    The parameters should be set as in the example below.

    >>> from pathlib import Path
    >>> load_replaypack_information_object = load_replaypack_information(
    ...        replaypack_name="replaypack_name",
    ...        replaypack_path=Path("replaypack_path"),
    ...    )

    >>> assert isinstance(replaypack_name, str)
    >>> assert isinstance(replaypack_path, Path)
    """

    replaypack_files = list(replaypack_path.iterdir())
    # Initializing variables that should be returned:
    replaypack_main_log_obj_list = []
    replaypack_processed_failed = {}
    replaypack_dir_mapping = {}
    replaypack_summary = {}

    # Extracting the nested .zip files,
    # and loading replaypack information files:
    for file in replaypack_files:
        filename = file.name
        if filename.endswith("_main_log.log"):
            main_log_filepath = Path(replaypack_path, file).resolve()
            with main_log_filepath.open(encoding="utf-8") as main_log_file:
                # Reading the lines of the log file and parsing them:
                for line in main_log_file.readlines():
                    log_object = json.loads(line)
                    replaypack_main_log_obj_list.append(log_object)
        if filename.endswith("_processed_failed.log"):
            processed_files_filepath = Path(replaypack_path, file).resolve()
            with processed_files_filepath.open(encoding="utf-8") as processed_files:
                replaypack_processed_failed = json.load(processed_files)
        if filename.endswith("_processed_mapping.json"):
            mapping_file_filepath = Path(replaypack_path, file).resolve()
            with mapping_file_filepath.open(encoding="utf-8") as mapping_file:
                replaypack_dir_mapping = json.load(mapping_file)
        if filename.endswith("_summary.json"):
            summary_file_filepath = Path(replaypack_path, file).resolve()
            with summary_file_filepath.open(encoding="utf-8") as summary_file:
                replaypack_summary = json.load(summary_file)

    return (
        replaypack_main_log_obj_list,
        replaypack_processed_failed,
        replaypack_dir_mapping,
        replaypack_summary,
    )
