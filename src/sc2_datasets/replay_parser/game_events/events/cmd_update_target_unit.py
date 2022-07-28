from typing import Dict

from sc2_datasets.replay_parser.game_events.game_event import GameEvent
from sc2_datasets.replay_parser.game_events.events.nested.target_unit import TargetUnit


class CmdUpdateTargetUnit(GameEvent):
    """
    Data type containing information about command update issued to some target unit.

    :param id: Specifies the event ID that should directly map\
    to the event name which is denoted by the class.
    :type id: int
    :param loop: Specifies the time in gameloop units when the event happened.
    :type loop: int
    :param target: Most likely specifies a target unit which receivedr the command.
    :type target: TargetUnit
    :param userid: Most likely specifies the user id that issued the command.
    :type userid: int
    """

    @staticmethod
    def from_dict(d: Dict) -> "CmdUpdateTargetUnit":
        """
        Static method returning initialized CmdUpdateTargetUnit class from a dictionary.
        This helps with the original JSON parsing.

        :param d: Specifies a dictionary as available in the JSON file\
        that is a result of pre-processing some .SC2Replay file.
        :type d: Dict
        :return: Returns an initialized CmdUpdateTargetUnit class.
        :rtype: CmdUpdateTargetUnit
        """
        return CmdUpdateTargetUnit(
            id=d["id"],
            loop=d["loop"],
            target=d["target"],
            userid=d["userid"]["userId"],
        )

    def __init__(
        self,
        id: int,
        loop: int,
        target: TargetUnit,
        userid: int,
    ) -> None:
        self.id = id
        self.loop = loop
        self.target = target
        self.userid = userid
