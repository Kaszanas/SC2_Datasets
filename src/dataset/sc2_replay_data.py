import json
from typing import Any
from src.dataset.replay_structures.details.details import Details

from src.dataset.replay_structures.game_events.game_events_parser import (
    GameEventsParser,
)
from src.dataset.replay_structures.header.header import Header
from src.dataset.replay_structures.init_data.init_data import InitData
from src.dataset.replay_structures.message_events.message_events_parser import (
    MessageEventsParser,
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
        self._init_data = InitData.from_dict(d=loaded_replay_object["initData"])
        self._details = Details.from_dict(d=loaded_replay_object["details"])
        self._metadata = ""
        self._game_events = [
            GameEventsParser.from_dict(d=event_dict)
            for event_dict in loaded_replay_object["gameEvents"]
        ]
        self._message_events = [
            MessageEventsParser.from_dict(d=event_dict)
            for event_dict in loaded_replay_object["messageEvents"]
        ]
        self._tracker_events = [
            TrackerEventsParser.from_dict(d=event_dict)
            for event_dict in loaded_replay_object["trackerEvents"]
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
