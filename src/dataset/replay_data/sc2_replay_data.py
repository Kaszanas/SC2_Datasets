import json
from typing import Any, Dict
from src.dataset.replay_data.replay_parser.details.details import Details

from src.dataset.replay_data.replay_parser.game_events.game_events_parser import (
    GameEventsParser,
)
from src.dataset.replay_data.replay_parser.header.header import Header
from src.dataset.replay_data.replay_parser.init_data.init_data import InitData
from src.dataset.replay_data.replay_parser.message_events.message_events_parser import (
    MessageEventsParser,
)
from src.dataset.replay_data.replay_parser.metadata.metadata import Metadata
from src.dataset.replay_data.replay_parser.toon_player_desc_map.toon_player_desc import (
    ToonPlayerDesc,
)
from src.dataset.replay_data.replay_parser.tracker_events.tracker_events_parser import (
    TrackerEventsParser,
)


class SC2ReplayData:
    @staticmethod
    def from_file(replay_filepath: str) -> "SC2ReplayData":
        with open(replay_filepath) as replay_file:
            return SC2ReplayData(json.load(replay_file))

    def __init__(self, loaded_replay_object: Any) -> None:

        # unique_names = set()
        # for event in loaded_replay_object["gameEvents"]:
        #     unique_names.add(event["evtTypeName"])

        # print(unique_names)

        self._header = Header.from_dict(d=loaded_replay_object["header"])
        self._initData = InitData.from_dict(d=loaded_replay_object["initData"])
        self._details = Details.from_dict(d=loaded_replay_object["details"])
        self._metadata = Metadata.from_dict(d=loaded_replay_object["metadata"])
        # TODO: We might want this to be a IterableDataset using PyTorch class:
        self._messageEvents = [
            MessageEventsParser.from_dict(d=event_dict)
            for event_dict in loaded_replay_object["messageEvents"]
        ]
        # TODO: We might want this to be a IterableDataset using PyTorch class:
        self._gameEvents = [
            GameEventsParser.from_dict(d=event_dict)
            for event_dict in loaded_replay_object["gameEvents"]
        ]
        # TODO: We might want this to be a IterableDataset using PyTorch class:
        self._trackerEvents = [
            TrackerEventsParser.from_dict(d=event_dict)
            for event_dict in loaded_replay_object["trackerEvents"]
        ]
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

    @property
    def initData(self):
        return self._init_data

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
