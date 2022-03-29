from typing import Dict
from src.dataset.replay_structures.tracker_events.tracker_event import TrackerEvent


class TrackerEventParser:
    @staticmethod
    def from_dict(dict: Dict) -> TrackerEvent:
        type_name = dict["evtTypeName"]
        if type_name == CameraSave.__name__:
            pass
