from typing import Dict

from sc2_datasets.replay_parser.message_events.message_event import MessageEvent


class Chat(MessageEvent):

    """
    Chat holds information about messages exchanged between players during the game.

    Parameters
    ----------
    id : int
        Specifies the ID of the chat event.
    loop : int
        Specifies the game loop number when the event occurred.
    recipient : int
        Specifies the recipient of the message in the event.
    string : str
        Specifies the message content in the chat event.
    userid : int
        Specifies the user ID causing the event.
    """

    @staticmethod
    def from_dict(d: Dict) -> "Chat":
        """
        Static method that returns an initialized Chat class based on a supplied dictionary.
        This method aids in parsing the original JSON data.

        Parameters
        ----------
        d : Dict
            A dictionary holding translations of a phrase or sentence.

        Returns
        -------
        Chat
            A list of chat parameters including user ID, recipient, etc.

        Examples
        --------
        **Correct Usage Examples:**

        Using from_dict factory method provides ease of use when parsing
        a replay pre-processed with SC2InfoExtractorGo_

        This method requires a dictionary representation of data to be passed
        as a parameter because of the built in json
        parser provided by the Python standard library.

        _SC2InfoExtractorGo: https://github.com/Kaszanas/SC2InfoExtractorGo

        The use of this method is intended to get chat information
        from the game's json representation.

        >>> chat_dict ={
        ...      "id": 0,
        ...      "loop": 185,
        ...      "recipient": 0,
        ...      "string": "gl hf",
        ...      "userid": {
        ...             "userId": 1}
        ...      }
        ...
        >>> chat_object = Chat.from_dict(d=chat_dict)
        ...
        >>> assert isinstance(chat_object, Chat)
        >>> assert isinstance(chat_object.id, int)
        >>> assert isinstance(chat_object.loop, int)
        >>> assert isinstance(chat_object.recipient, int)
        >>> assert isinstance(chat_object.string, str)
        >>> assert isinstance(chat_object.userid, int)
        ...
        >>> assert chat_object.id == 0
        >>> assert chat_object.loop == 185
        >>> assert chat_object.recipient == 0
        >>> assert chat_object.string == "gl hf"
        >>> assert chat_object.userid == 1
        ...
        >>> assert chat_object.id >= 0
        >>> assert chat_object.loop >= 0
        >>> assert chat_object.recipient >= 0
        >>> assert chat_object.userid >= 0

        **Incorrect Usage Examples:**

        >>> gameOptions_value_wrong = "False"
        >>> gameSpeed_value_wrong = True
        >>> isBlizzardMap_value_wrong = "wrong type"
        >>> mapAuthorName_value_wrong = int(2)
        >>> mapFileSyncChecksum_value_wrong = str(2)
        >>> mapSizeX_value_wrong = str(2)
        >>> mapSizeY_value_wrong = str(2)
        >>> maxPlayers_value_wrong = str(2)

        >>> GameDescription(
        ...    gameOptions=gameOptions_value_wrong,
        ...    gameSpeed=gameSpeed_value_wrong,
        ...    isBlizzardMap=isBlizzardMap_value_wrong,
        ...    mapAuthorName=mapAuthorName_value_wrong,
        ...    mapFileSyncChecksum=mapFileSyncChecksum_value_wrong,
        ...    mapSizeX=mapSizeX_value_wrong,
        ...    mapSizeY=mapSizeY_value_wrong,
        ...    maxPlayers=maxPlayers_value_wrong)
        Traceback (most recent call last):
        ...
        TypeError: unsupported operand type(s) ...
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
