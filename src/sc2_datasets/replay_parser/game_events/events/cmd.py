from types import NoneType
from typing import Dict

from sc2_datasets.replay_parser.game_events.game_event import GameEvent


# TODO: Can the sequence be an int here?
# Should this be encoded somehow if there is a NoneType detected?


class Cmd(GameEvent):
    """
    Cmd contains specific details about command interface events.

    Parameters
    ----------
    id : int
        Specifies the ID of an event corresponding to its name.
    loop : int
        Specifies the game loop number (game-engine tick) at which the event occurred.
    otherUnit : NoneType
        Specific information unavailable about this parameter.
    sequence : int
        Likely specifies an ID parameter representing\
        the sequence the user typed in the console.
        Specific information about this parameter is unavailable.
    unitGroup : NoneType or int
        Specific information unavailable about this parameter.
    userid : int
        Likely specifies the user's ID using the interface.
        Specific information about this parameter is unavailable.

    """

    @staticmethod
    def from_dict(d: Dict) -> "Cmd":
        """
        Static method returning an initialized Cmd class from a dictionary.
        This aids in parsing the original JSON.

        Parameters
        ----------
        d : Dict
            Dictionary available in the JSON file, typically a result\
            of pre-processing an .SC2Replay file.

        Returns
        -------
        Cmd
            Initialized Cmd class.

        """
        return Cmd(
            id=d["id"],
            loop=d["loop"],
            otherUnit=d["otherUnit"],
            sequence=d["sequence"],
            unitGroup=d["unitGroup"],
            userid=d["userid"]["userId"],
        )

    def __init__(
        self,
        id: int,
        loop: int,
        otherUnit: NoneType,
        sequence: int,
        unitGroup: NoneType | int,
        userid: int,
    ) -> None:
        self.id = id
        self.loop = loop
        self.otherUnit = otherUnit
        self.sequence = sequence
        self.unitGroup = unitGroup
        self.userid = userid
