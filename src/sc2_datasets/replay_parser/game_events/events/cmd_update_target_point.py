from typing import Dict

from sc2_datasets.replay_parser.game_events.game_event import GameEvent
from sc2_datasets.replay_parser.game_events.events.nested.target_3d import Target3D


class CmdUpdateTargetPoint(GameEvent):
    """
    Data type containing information about a command update issued to a target point.

    Parameters
    ----------
    id : int
        Specifies the event ID directly mapping to the class's event name.
    loop : int
        Time in gameloop units when the event occurred.
    target : Target3D
        Specifies a 3D target where the command was issued.
    userid : int
        Specifies the user ID that issued the command.
    """

    @staticmethod
    def from_dict(d: Dict) -> "CmdUpdateTargetPoint":
        """
        Static method returning an initialized CmdUpdateTargetPoint class from a dictionary.
        This helps with the original JSON parsing.

        Parameters
        ----------
        d : Dict
            Dictionary available in the JSON file after pre-processing some .SC2Replay file.

        Returns
        -------
        CmdUpdateTargetPoint
            Initialized CmdUpdateTargetPoint class.
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
