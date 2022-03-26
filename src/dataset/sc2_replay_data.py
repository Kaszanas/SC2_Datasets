import json
from typing import Any


#  { event["evtTypeName"] for event in json_obj["gameEvents"]}
#
# event_type_to_example = {}
# for event in json_obj["gameEvents"]:
#     if event["evtTypeName"] not in event_type_to_example:
#         event_type_to_example[event["evtTypeName"]] = event


# Abstract game event type. Needs to support at least the following:
# {'UserOptions', 'CameraUpdate', 'ControlGroupUpdate', 'GameUserLeave', 'CommandManagerState', 'CameraSave', 'CmdUpdateTargetPoint', 'CmdUpdateTargetUnit', 'Cmd', 'SelectionDelta'}
class GameEvent:
    @staticmethod
    def from_dict(d) -> "GameEvent":
        type_name = d["evtTypeName"]


class GameOptions:
    pass


class SC2ReplayData:
    @staticmethod
    def from_file(replay_filepath: str) -> "SC2ReplayData":
        with open(replay_filepath) as replay_file:
            return SC2ReplayData(json.load(replay_file))

    def __init__(self, loaded_replay_object: Any) -> None:

        unique_names = set()
        for event in loaded_replay_object["gameEvents"]:
            unique_names.add(event["evtTypeName"])

        print(unique_names)

        self._header = loaded_replay_object["header"]
        self._init_data = loaded_replay_object["initData"]
        self._game_events = [
            GameEvent.from_dict(event) for event in loaded_replay_object["gameEvents"]
        ]

        # TODO: Check what are the unique game events that can occur
        # And create serialization classes for them so that the json can be parsed.

    @property
    def header(self):
        return self._header

    # @header.setter
    # def header(self, header):
    #     self._header = header

    @property
    def init_data(self):
        return self._init_data

    # @init_data.setter
    # def init_data(self, init_data):
    #     self._init_data = init_data

    @property
    def initData(self):
        return self._init_data
