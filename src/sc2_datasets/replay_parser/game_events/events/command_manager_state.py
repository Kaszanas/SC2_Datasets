from typing import Dict

from sc2_datasets.replay_parser.game_events.game_event import GameEvent


class CommandManagerState(GameEvent):
    """
    CommandManagerState type contains information about some states during
    the game e.g., time, player, etc.

    :param id: Specifies the ID of an event which corresponds to its name.
    :type id: int
    :param loop: Specifies the game loop number (game-engine tick)\
    at which the event occurred
    :type loop: int
    :param sequence: Highly likely this parameter specifies\
    an id parameter which sequence the player has made,\
    there is no specific information about this parameter
    :type sequence: int
    :param state: Highly likely this parameter specifies\
    an id parameter which state the player has made,\
    there is no specific information about this parameter
    :type state: int
    :param userid: Specifies id number of player who has managed the state,\
    example: in 1v1 game: [0,1]
    :type userid: int
    """

    @staticmethod
    def from_dict(d: Dict) -> "CommandManagerState":
        """
        Static method returning initialized CommandManagerState class from a dictionary.
        This helps with the original JSON parsing.

        :param d: Specifies a dictionary as available in the JSON file\
        that is a result of pre-processing some .SC2Replay file.
        :type d: Dict
        :return: Returns an initialized CommandManagerState class.
        :rtype: CommandManagerState
        """
        return CommandManagerState(
            id=d["id"],
            loop=d["loop"],
            sequence=d["sequence"],
            state=d["state"],
            userid=d["userid"]["userId"],
        )

    def __init__(
        self,
        id: int,
        loop: int,
        sequence: int,
        state: int,
        userid: int,
    ) -> None:
        self.id = id
        self.loop = loop
        self.sequence = sequence
        self.state = state
        self.userid = userid
