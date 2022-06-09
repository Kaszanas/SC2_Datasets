from typing import Dict


from src.dataset.replay_data.replay_parser.message_events.message_event import (
    MessageEvent,
)


class Chat(MessageEvent):

    """
    Chat holds information about messages between players during the game

    :param id: Specifies id of the chat event
    :type id: int
    :param loop: Specifies game loop number when the event occurred
    :type loop: int
    :param recipient: Specifies the message recipient of the event
    :type recipient: int
    :param string: Specifies the message in the chat event
    :type string: str
    :param userid: Specifies user id causing the event
    :type userid: int
    """

    @staticmethod
    def from_dict(d: Dict) -> "Chat":
        """
        Static method returning initialized Chat class from a dictionary. This helps with the original JSON parsing.

        :param d: Specifies a dictionary, it holds translations of a phrase or sentence.
        :type d: Dict
        :return: Specifies a list of chat parameters like a user id, recipient etc.
        :rtype: Chat
        """
        return Chat(
            id=d["id"],
            loop=d["loop"],
            recipient=d["recipient"],
            string=d["string"],
            userid=d["userid"]["userId"],
        )

    def __init__(
        self,
        id: int,
        loop: int,
        recipient: int,
        string: str,
        userid: int,
    ) -> None:

        self.id = id
        self.loop = loop
        self.recipient = recipient
        self.string = string
        self.userid = userid
