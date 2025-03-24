from typing import Dict

from sc2_datasets.replay_parser.game_events.events.nested.target_unit import TargetUnit
from sc2_datasets.replay_parser.game_events.game_event import GameEvent


class CmdUpdateTargetUnit(GameEvent):
    """
    Data type containing information about a command update issued to a specific target unit.

    Parameters
    ----------
    id : int
        Event ID mapping to the event name represented by the class.
    loop : int
        Time in gameloop units when the event occurred.
    target : TargetUnit
        Specifies the target unit that received the command.
    userid : int
        Specifies the user ID that issued the command.
    """

    @staticmethod
    def from_dict(d: Dict) -> "CmdUpdateTargetUnit":
        """
        Static method returning an initialized CmdUpdateTargetUnit class from a dictionary.
        This aids in the original JSON parsing.

        Parameters
        ----------
        d : Dict
            Dictionary available in the JSON file resulting from preprocessing an .SC2Replay file.

        Returns
        -------
        CmdUpdateTargetUnit
            Initialized CmdUpdateTargetUnit class.
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
