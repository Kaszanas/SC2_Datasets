from typing import Dict
from src.dataset.replay_data.replay_parser.message_events.events.chat import Chat
from src.dataset.replay_data.replay_parser.message_events.message_event import (
    MessageEvent,
)


class MessageEventsParser:
    @staticmethod
    def from_dict(d: Dict) -> MessageEvent:
        """
        _summary_

        :param d: Specifies a dictionary, it holds translations of a phrase or sentence.
        :type d: Dict
        :return: Specifies an implementation of an abstract method from MessageEvent class
        :rtype: MessageEvent
        """
        type_name = d["evtTypeName"]
        match type_name:
            case Chat.__name__:
                return Chat.from_dict(d=d)
