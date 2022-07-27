from typing import Dict

from sc2_datasets.replay_parser.game_events.game_event import GameEvent
from sc2_datasets.replay_parser.game_events.events.nested.target_3d import Target3D


class CmdUpdateTargetPoint(GameEvent):
    """
    Data type containing information about command update issued to some target point.

    :param id: Specifies the event ID that should directly map\
    to the event name which is denoted by the class.
    :type id: int
    :param loop: Specifies the time in gameloop units when the event happened.
    :type loop: int
    :param target: Most likely specifies a 3D target where the command was issued.
    :type target: Target3D
    :param userid: Most likely specifies the user id that issued the command.
    :type userid: int
    """

    @staticmethod
    def from_dict(d: Dict) -> "CmdUpdateTargetPoint":
        """
        Static method returning initialized CmdUpdateTargetPoint class from a dictionary.
        This helps with the original JSON parsing.

        :param d: Specifies a dictionary as available in the JSON file\
        that is a result of pre-processing some .SC2Replay file.
        :type d: Dict
        :return: Returns an initialized CmdUpdateTargetPoint class.
        :rtype: CmdUpdateTargetPoint
        """
        return CmdUpdateTargetPoint(
            id=d["id"],
            loop=d["loop"],
            target=Target3D(x=d["target"]["x"], y=d["target"]["y"], z=d["target"]["z"]),
            userid=d["userid"]["userId"],
        )

    def __init__(
        self,
        id: int,
        loop: int,
        target: Target3D,
        userid: int,
    ) -> None:
        self.id = id
        self.loop = loop
        self.target = target
        self.userid = userid
