from types import NoneType
from typing import Dict


from src.dataset.replay_data.replay_parser.game_events.game_event import GameEvent

# TODO: Can the sequence be an int here?
# Should this be encoded somehow if there is a NoneType detected?

# TODO: Document the docstrings


class Cmd(GameEvent):

    """_summary_

    :param id: _description_
    :type id: int
    :param loop: _description_
    :type loop: int
    :param otherUnit: _description_
    :type otherUnit: NoneType
    :param sequence: _description_
    :type sequence: int
    :param unitGroup: _description_
    :type unitGroup: NoneType | int
    :param userid: _description_
    :type userid: int
    """

    @staticmethod
    def from_dict(d: Dict) -> "Cmd":
        """_summary_

        :param d: _description_
        :type d: Dict
        :return: _description_
        :rtype: Cmd
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
