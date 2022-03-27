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
