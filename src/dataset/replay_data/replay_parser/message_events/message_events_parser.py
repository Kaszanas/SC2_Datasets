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

        :param d: _description_
        :type d: Dict
        :return: _description_
        :rtype: MessageEvent
        """
        type_name = d["evtTypeName"]
        match type_name:
            case Chat.__name__:
                return Chat.from_dict(d=d)
