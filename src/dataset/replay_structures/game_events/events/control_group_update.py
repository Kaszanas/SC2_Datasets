from types import NoneType
from typing import Dict

from src.dataset.replay_structures.game_events.game_event import GameEvent

# TODO: Document the docstrings


class ControlGroupUpdate(GameEvent):
    """_summary_

    :param controlGroupIndex: _description_
    :type controlGroupIndex: int
    :param controlGroupUpdate: _description_
    :type controlGroupUpdate: int
    :param id: _description_
    :type id: int
    :param loop: _description_
    :type loop: int
    :param userid: _description_
    :type userid: int
    """

    @staticmethod
    def from_dict(d: Dict) -> "ControlGroupUpdate":
        """_summary_

        :param d: _description_
        :type d: Dict
        :return: _description_
        :rtype: ControlGroupUpdate
        """
        return ControlGroupUpdate(
            controlGroupIndex=d["controlGroupIndex"],
            controlGroupUpdate=d["controlGroupUpdate"],
            id=d["id"],
            loop=d["loop"],
            userid=d["userid"]["userId"],
        )

    def __init__(
        self,
        controlGroupIndex: int,
        controlGroupUpdate: int,
        id: int,
        loop: int,
        userid: int,
    ) -> None:

        self.controlGroupIndex = controlGroupIndex
        self.controlGroupUpdate = controlGroupUpdate
        self.id = id
        self.loop = loop
        self.userid = userid
