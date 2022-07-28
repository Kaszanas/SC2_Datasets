from typing import Dict

from sc2_datasets.replay_parser.game_events.game_event import GameEvent


class GameUserLeave(GameEvent):
    """
    GameUserLeave is information about a player leaving the game.

    :param id: Specifies the ID of an event which corresponds to its name.
    :type id: int
    :param leaveReason: Specifies a number which determinate leaving reason,\
    there are no more details
    :type leaveReason: int
    :param loop: Specifies the game loop number (game-engine tick)\
    at which the event occurred
    :type loop: int
    :param userid: Specifies id number of player who has left the game
    :type userid: int
    """

    @staticmethod
    def from_dict(d: Dict) -> "GameUserLeave":
        """
        Static method returning initialized GameUserLeave class from a dictionary.
        This helps with the original JSON parsing.

        :param d: Specifies a dictionary as available in the JSON file\
        that is a result of pre-processing some .SC2Replay file.
        :type d: Dict
        :return: Returns an initialized GameUserLeave class.
        :rtype: GameUserLeave
        """
        return GameUserLeave(
            id=d["id"],
            leaveReason=d["leaveReason"],
            loop=d["loop"],
            userid=d["userid"]["userId"],
        )

    def __init__(
        self,
        id: int,
        leaveReason: int,
        loop: int,
        userid: int,
    ) -> None:
        self.id = id
        self.leaveReason = leaveReason
        self.loop = loop
        self.userid = userid
