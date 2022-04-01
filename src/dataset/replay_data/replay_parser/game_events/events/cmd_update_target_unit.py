from typing import Dict
from src.dataset.replay_structures.game_events.events.nested.target_unit import (
    TargetUnit,
)
from src.dataset.replay_structures.game_events.game_event import GameEvent

# TODO: Document the docstrings


class CmdUpdateTargetUnit(GameEvent):

    """
    _summary_

    :param id: _description_
    :type id: int
    :param loop: _description_
    :type loop: int
    :param target: _description_
    :type target: TargetUnit
    :param userid: _description_
    :type userid: int
    """

    @staticmethod
    def from_dict(d: Dict) -> "CmdUpdateTargetUnit":
        """
        _summary_

        :param d: _description_
        :type d: Dict
        :return: _description_
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
