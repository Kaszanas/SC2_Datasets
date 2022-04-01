import json
from typing import Any, Dict
from src.dataset.replay_structures.details.details import Details

from src.dataset.replay_structures.game_events.game_events_parser import (
    GameEventsParser,
)
from src.dataset.replay_structures.header.header import Header
from src.dataset.replay_structures.init_data.init_data import InitData
from src.dataset.replay_structures.message_events.message_events_parser import (
    MessageEventsParser,
)
from src.dataset.replay_structures.metadata.metadata import Metadata
from src.dataset.replay_structures.toon_player_desc_map.toon_player_desc_map import (
    ToonPlayerDesc,
)
from src.dataset.replay_structures.tracker_events.tracker_events_parser import (
    TrackerEventsParser,
)


class GameOptions:
    pass


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
        self._messageEvents = [
            MessageEventsParser.from_dict(d=event_dict)
            for event_dict in loaded_replay_object["messageEvents"]
        ]
        self._gameEvents = [
            GameEventsParser.from_dict(d=event_dict)
            for event_dict in loaded_replay_object["gameEvents"]
        ]
        self._trackerEvents = [
            TrackerEventsParser.from_dict(d=event_dict)
            for event_dict in loaded_replay_object["trackerEvents"]
        ]
        toon_player_desc_dict: Dict[str, Dict[str, Any]] = loaded_replay_object[
            "ToonPlayerDescMap"
        ]
        self._toonPlayerDescMap = [
            ToonPlayerDesc.from_dict(toon=toon, d=player_dict)
            for toon, player_dict in toon_player_desc_dict.items()
        ]

    @property
    def header(self):
        return self._header

    # @header.setter
    # def header(self, header):
    #     self._header = header

    # @property
    # def init_data(self):
    #     return self._init_data

    # @init_data.setter
    # def init_data(self, init_data):
    #     self._init_data = init_data

    @property
    def initData(self):
        return self._init_data
