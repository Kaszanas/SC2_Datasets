from typing import Dict
from src.dataset.replay_structures.message_events.message_event import MessageEvent


class MessageEventParser:
    @staticmethod
    def from_dict(d: Dict) -> MessageEvent:
        type_name = dict["evtTypeName"]
        if type_name == CameraSave.__name__:
            pass
