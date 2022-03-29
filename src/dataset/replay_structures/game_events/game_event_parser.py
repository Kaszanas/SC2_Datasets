#  { event["evtTypeName"] for event in json_obj["gameEvents"]}
#
# event_type_to_example = {}
# for event in json_obj["gameEvents"]:
#     if event["evtTypeName"] not in event_type_to_example:
#         event_type_to_example[event["evtTypeName"]] = event


# Abstract game event type. Needs to support at least the following:
# {'UserOptions', 'CameraUpdate', 'ControlGroupUpdate', 'GameUserLeave', 'CommandManagerState', 'CameraSave', 'CmdUpdateTargetPoint', 'CmdUpdateTargetUnit', 'Cmd', 'SelectionDelta'}
from typing import Dict
from src.dataset.replay_structures.game_events.game_event import GameEvent

from src.dataset.replay_structures.game_events.events.camera_save import CameraSave


class GameEventParser:
    @staticmethod
    def from_dict(dict: Dict) -> GameEvent:
        type_name = dict["evtTypeName"]
        if type_name == CameraSave.__name__:
            pass
