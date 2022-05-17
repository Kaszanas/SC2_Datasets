from typing import List, Tuple

from src.dataset.replay_data.sc2_replay_data import SC2ReplayData


# TODO: Verify if it is possible to return two sets:
def validate_chunk(
    list_of_replays: List[str],
) -> List[Tuple[str, bool]]:
    """
    Attempts to parse a chunk of replays and validates the JSON structure using SC2ReplayData parser.

    :param list_of_replays: Specifies the list of replays that will be validated.
    :type list_of_replays: List[str]
    :return: Returns a tuple of SC2ReplayFile info and a boolean denoting if the file should be skipped in final processing.
    :rtype: List[Tuple[str, bool]]
    """

    # Initializing sets:
    validated_files = set()
    skip_files = set()

    for file_path in list_of_replays:
        # We are keeping track of all of the files that are validated:
        validated_files.add(file_path)
        try:
            # Trying to parse the SC2 replay:
            replay_data = SC2ReplayData.from_file(replay_filepath=file_path)
        except:
            # If the file cannot be parsed it is added to files that should be skipped:
            skip_files.add(file_path)

    result = []
    # Converting the sets to a single result list:
    for file in validated_files:
        result.append((file, True))
    for file in skip_files:
        result.append((file, False))

    return result
