from typing import Dict

from sc2_datasets.replay_parser.message_events.events.chat import Chat
from sc2_datasets.replay_parser.message_events.message_event import MessageEvent


class MessageEventsParser:
    @staticmethod
    def from_dict(d: Dict) -> MessageEvent:
        """
        Static method returning an initialized instance of MessageEvent class
        based on a dictionary input, aiding in the original JSON parsing.

        Parameters
        ----------
        d : Dict
            A dictionary holding translations of a phrase or sentence.

        Returns
        -------
        MessageEvent
            An implementation of an abstract method from the MessageEvent class.

        """
        type_name = d["evtTypeName"]
        match type_name:
            case Chat.__name__:
                return Chat.from_dict(d=d)
