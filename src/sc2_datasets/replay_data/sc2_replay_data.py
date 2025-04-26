import json
import logging
from dataclasses import dataclass, field
from pathlib import Path

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


@dataclass
class SC2ReplayData:
    filepath: Path
    header: Header
    initData: InitData
    details: Details
    metadata: Metadata
    messageEvents: list = field(default_factory=list)
    gameEvents: list = field(default_factory=list)
    trackerEvents: list = field(default_factory=list)
    toonPlayerDescMap: list = field(default_factory=list)
    gameEventsErr: bool = False
    messageEventsErr: bool = False
    trackerEventsErr: bool = False

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
            return SC2ReplayData(
                filepath=replay_path,
                header=Header.from_dict(d=loaded_data["header"]),
                initData=InitData.from_dict(d=loaded_data["initData"]),
                details=Details.from_dict(d=loaded_data["details"]),
                metadata=Metadata.from_dict(d=loaded_data["metadata"]),
                messageEvents=[
                    MessageEventsParser.from_dict(d=event_dict)
                    for event_dict in loaded_data.get("messageEvents", [])
                ],
                gameEvents=[
                    GameEventsParser.from_dict(d=event_dict)
                    for event_dict in loaded_data.get("gameEvents", [])
                ],
                trackerEvents=[
                    TrackerEventsParser.from_dict(d=event_dict)
                    for event_dict in loaded_data.get("trackerEvents", [])
                ],
                toonPlayerDescMap=[
                    ToonPlayerDesc.from_dict(toon=toon, d=player_dict)
                    for toon, player_dict in loaded_data.get(
                        "ToonPlayerDescMap", {}
                    ).items()
                ],
                gameEventsErr=loaded_data.get("gameEventsErr", False),
                messageEventsErr=loaded_data.get("messageEventsErr", False),
                trackerEventsErr=loaded_data.get("trackerEvtsErr", False),
            )

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
