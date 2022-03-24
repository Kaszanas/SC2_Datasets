import os
from typing import Dict, Tuple
from dataset.utils.zip_utils import unpack_zipfile


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
    data_path = ""
    summary_content = {}
    mapping_content = {}
    processed_info = {}

    for file in replaypack_files:
        if file.endswith("_data.zip"):
            data_path = unpack_zipfile(
                destination_dir=replaypack_path,
                subdir=replaypack_name + "_data",
                zip_path=file,
            )
        # TODO: ADD THE LOADING LOGIC
        if file.endswith("_summary.json"):
            summary_content = ""
        if file.endswith("_mapping.json"):
            mapping_content = ""
        if file.endswith(".log") and not file.endswith("main_log.log"):
            processed_info = ""

    return (data_path, summary_content, mapping_content, processed_info)
