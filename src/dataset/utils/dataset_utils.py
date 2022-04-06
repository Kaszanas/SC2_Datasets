import json
import os
from typing import Dict, Tuple
from src.dataset.utils.zip_utils import unpack_zipfile


def load_replaypack_information(
    replaypack_name: str, replaypack_path: str
) -> Tuple[str, Dict[str, str], Dict[str, str]]:
    """
    Helper function that loads replaypack information from a standard directory structure.

    :param replaypack_name: Specifies the replaypack name that will be used as a subdirectory where replaypack .json files will be extracted.
    :type replaypack_name: str
    :param replaypack_path: Specifies the path to the extracted replaypack.
    :type replaypack_path: str
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
    for file in replaypack_files:
        if file.endswith("_data.zip"):
            data_path = os.path.join(replaypack_path, replaypack_name + "_data")
            # Unpack the .zip archive only if it is not unpacked already:
            if not os.path.isdir(data_path):
                data_path = unpack_zipfile(
                    destination_dir=replaypack_path,
                    subdir=replaypack_name + "_data",
                    zip_path=os.path.join(replaypack_path, file),
                )
        # TODO: ADD THE LOADING LOGIC
        if file.endswith("_summary.json"):
            with open(file) as summary_file:
                summary_content = json.load(summary_file)
        if file.endswith("_mapping.json"):
            with open(file) as mapping_file:
                mapping_content = json.load(mapping_file)
        if file.endswith(".log") and not file.endswith("main_log.log"):
            processed_info = ""

    return (data_path, summary_content, mapping_content, processed_info)
