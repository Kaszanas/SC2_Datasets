import json
import logging
from typing import Any, Dict


from sc2_datasets.replay_parser.game_events.game_events_parser import GameEventsParser

from sc2_datasets.replay_parser.details.details import Details
from sc2_datasets.replay_parser.header.header import Header
from sc2_datasets.replay_parser.init_data.init_data import InitData
from sc2_datasets.replay_parser.metadata.metadata import Metadata

from sc2_datasets.replay_parser.message_events.message_events_parser import (
    MessageEventsParser,
)

from sc2_datasets.replay_parser.toon_player_desc_map.toon_player_desc import (
    ToonPlayerDesc,
)

from sc2_datasets.replay_parser.tracker_events.tracker_events_parser import (
    TrackerEventsParser,
)


class SC2ReplayData:
    """
    Specifies a data type that holds information parsed from json representation of a replay.

    :param loaded_replay_object: Specifies a parsed Python deserialized json object\
    loaded into memory
    :type loaded_replay_object: Any
    """

    # REVIEW: Doctests, and commented out code:
    @staticmethod
    def from_file(replay_filepath: str) -> "SC2ReplayData":
        """
        Static method returning initialized SC2ReplayData class from a dictionary.
        This helps with the original JSON parsing.

        :param replay_filepath: Specifies a dictionary as available\
        in the JSON file that is a result of pre-processing some .SC2Replay file.
        :type replay_filepath: str
        :return: Returns an initialized SC2ReplayData object
        :rtype: SC2ReplayData

        **Correct Usage Examples:**

        The factory method ``from_file`` assists with initializing a ``SC2ReplayData`` class.
        All that is required is a known path to the file that should be parsed.

        >>> replay_data = SC2ReplayData.from_file("test/test_files/single_replay/test_replay.json")
        >>> assert isinstance(replay_data, SC2ReplayData)
        """
        logging.info(f"\nAttempting to parse: {replay_filepath}")
        with open(replay_filepath, encoding="utf-8") as replay_file:
            # try:
            loaded_data = json.load(replay_file)
            # except UnicodeDecodeError as exc:
            #     logging.error(
            #         f"UnicodeDecodeError was raised for file {replay_filepath}",
            #         exc_info=True,
            #     )
            # except json.decoder.JSONDecodeError as exc:
            #     logging.error(
            #         f"JSONDecodeError was raised for file {replay_filepath}",
            #         exc_info=True,
            #     )
            return SC2ReplayData(loaded_replay_object=loaded_data)

    def __init__(self, loaded_replay_object: Any) -> None:

        self._header = Header.from_dict(d=loaded_replay_object["header"])
        self._initData = InitData.from_dict(d=loaded_replay_object["initData"])
        self._details = Details.from_dict(d=loaded_replay_object["details"])
        self._metadata = Metadata.from_dict(d=loaded_replay_object["metadata"])
        # TODO: We might want this to be a IterableDataset using PyTorch class:
        self._messageEvents = []
        if loaded_replay_object["messageEvents"]:
            for event_dict in loaded_replay_object["messageEvents"]:
                self._messageEvents.append(MessageEventsParser.from_dict(d=event_dict))
        # TODO: We might want this to be a IterableDataset using PyTorch class:
        self._gameEvents = []
        if loaded_replay_object["gameEvents"]:
            for event_dict in loaded_replay_object["gameEvents"]:
                self._gameEvents.append(GameEventsParser.from_dict(d=event_dict))
        # TODO: We might want this to be a IterableDataset using PyTorch class:
        self._trackerEvents = []
        if loaded_replay_object["trackerEvents"]:
            for event_dict in loaded_replay_object["trackerEvents"]:
                self._trackerEvents.append(TrackerEventsParser.from_dict(d=event_dict))
        # TODO: We might want this to be a IterableDataset using PyTorch class:
        toon_player_desc_dict: Dict[str, Dict[str, Any]] = loaded_replay_object[
            "ToonPlayerDescMap"
        ]
        self._toonPlayerDescMap = [
            ToonPlayerDesc.from_dict(toon=toon, d=player_dict)
            for toon, player_dict in toon_player_desc_dict.items()
        ]

        self._gameEventsErr: bool = loaded_replay_object["gameEventsErr"]
        self._messageEventsErr: bool = loaded_replay_object["messageEventsErr"]
        self._trackerEventsErr: bool = loaded_replay_object["trackerEvtsErr"]

    # REVIEW: Should the __hash__ be tested?
    def __hash__(self) -> int:
        """
        Custom hashing function based on the fields that were read from replay.
        This hashing function returns a result of hash() call
        on a tuple constructed as follows:
        (game_duration_loops, game_time_utc, game_map, game_version,
        player_toon_map_len, player_tuple_toon,)

        :return: Returns an int (hash) representation of the SC2ReplayData class.
        :rtype: int
        """

        game_duration_loops = self.header.elapsedGameLoops
        game_time_utc = self.details.timeUTC
        game_map = self.metadata.mapName
        game_version = self.metadata.gameVersion
        player_toon_map_len = len(self.toonPlayerDescMap)
        player_tuple_toon = tuple(toon.toon for toon in self.toonPlayerDescMap)

        return hash(
            (
                game_duration_loops,
                game_time_utc,
                game_map,
                game_version,
                player_toon_map_len,
                player_tuple_toon,
            )
        )

    # REVIEW: Should the properties be documented?
    @property
    def initData(self):
        return self._initData

    @property
    def header(self):
        return self._header

    @property
    def details(self):
        return self._details

    @property
    def metadata(self):
        return self._metadata

    @property
    def messageEvents(self):
        return self._messageEvents

    @property
    def gameEvents(self):
        return self._gameEvents

    @property
    def trackerEvents(self):
        return self._trackerEvents

    @property
    def toonPlayerDescMap(self):
        return self._toonPlayerDescMap
