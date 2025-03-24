import json
import logging
from pathlib import Path
from typing import Any, Dict

from sc2_datasets.replay_parser.details.details import Details
from sc2_datasets.replay_parser.game_events.game_events_parser import GameEventsParser
from sc2_datasets.replay_parser.header.header import Header
from sc2_datasets.replay_parser.init_data.init_data import InitData
from sc2_datasets.replay_parser.message_events.message_events_parser import (
    MessageEventsParser,
)
from sc2_datasets.replay_parser.metadata.metadata import Metadata
from sc2_datasets.replay_parser.toon_player_desc_map.toon_player_desc import (
    ToonPlayerDesc,
)
from sc2_datasets.replay_parser.tracker_events.tracker_events_parser import (
    TrackerEventsParser,
)


class SC2ReplayData:
    """
    Specifies a data type that holds information parsed from json representation of a replay.

    Parameters
    ----------
    loaded_replay_object : Any
        Specifies a parsed Python deserialized json object\
        loaded into memory
    """

    @staticmethod
    def from_file(replay_filepath: str) -> "SC2ReplayData":
        """
        Static method returning initialized SC2ReplayData class from a dictionary.
        This helps with the original JSON parsing.

        Parameters
        ----------
        replay_filepath : str
            Specifies a filepath to a JSON file containing data\
            from parsed .SC2Replay file.

        Returns
        -------
        SC2ReplayData
            Returns an initialized SC2ReplayData object.

        Examples
        -------
        The factory method ``from_file`` assists with initializing a ``SC2ReplayData`` class.
        All that is required is a known path to the file that should be parsed.

        >>> replay_data = SC2ReplayData.from_file("test/test_files/single_replay/test_replay.json")
        >>> assert isinstance(replay_data, SC2ReplayData)
        """

        replay_path = Path(replay_filepath).resolve()

        logging.info(f"Attempting to parse: {str(replay_path)}")
        with replay_path.open(mode="r", encoding="utf-8") as replay_file:
            loaded_data = json.load(replay_file)
            return SC2ReplayData(filepath=replay_path, loaded_replay_object=loaded_data)

    def __init__(self, filepath: Path, loaded_replay_object: Any) -> None:
        # Replay data must contain the path to the json it comes from
        # to allow for debugging:
        self._filepath = filepath

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

        Returns
        -------
        int
            Returns an int (hash) representation of the SC2ReplayData class.
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
    def filepath(self):
        return self._filepath

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
