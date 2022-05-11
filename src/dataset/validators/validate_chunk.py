from typing import List, Tuple

from src.dataset.replay_data.sc2_replay_data import SC2ReplayData


from src.dataset.utils.sc2_replay_file_info.sc2_replay_file_info import (
    SC2ReplayFileInfo,
)


def validate_chunk(
    list_of_replays: List[SC2ReplayFileInfo],
) -> List[Tuple[SC2ReplayFileInfo, bool]]:
    """
    Attempts to parse a chunk of replays and validates the JSON structure using SC2ReplayData parser.

    :param list_of_replays: Specifies the list of replays that will be validated.
    :type list_of_replays: List[SC2ReplayFileInfo]
    :return: Returns a tuple of SC2ReplayFile info and a boolean denoting if the file should be skipped in final processing.
    :rtype: List[Tuple[SC2ReplayFileInfo, bool]]
    """
    validated_files = set()
    skip_files = set()
    for file_info in list_of_replays:
        try:
            validated_files.add(file_info)
            replay_data = SC2ReplayData.from_file(
                replay_filepath=file_info.get_full_path()
            )
        except:
            validated_files.add(file_info)
            skip_files.add(file_info)

    # If file is in validated and skip the its skip
    # if file is only in validated then it's fine:
    # only_correct = validated_files - skip_files

    result_list = []
    for file in list(validated_files):
        result_list.append((file, True))

    for file in list(skip_files):
        result_list.append((file, False))

    return result_list
