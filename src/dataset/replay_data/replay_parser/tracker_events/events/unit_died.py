from typing import Dict

from src.dataset.replay_data.replay_parser.tracker_events.tracker_event import (
    TrackerEvent,
)

# TODO: Document the docstrings


class UnitDied(TrackerEvent):

    """
    _summary_

    :param id: _description_
    :type id: int
    :param killerPlayerId: _description_
    :type killerPlayerId: int
    :param killerUnitTagIndex: _description_
    :type killerUnitTagIndex: int
    :param killerUnitTagRecycle: _description_
    :type killerUnitTagRecycle: int
    :param loop: _description_
    :type loop: int
    :param unitTagIndex: _description_
    :type unitTagIndex: int
    :param unitTagRecycle: _description_
    :type unitTagRecycle: int
    :param x: _description_
    :type x: int
    :param y: _description_
    :type y: int
    """

    def from_dict(d: Dict) -> "UnitDied":
        """
        _summary_

        :param d: _description_
        :type d: Dict
        :return: _description_
        :rtype: UnitDied
        """
        return UnitDied(
            id=d["id"],
            killerPlayerId=d["killerPlayerId"],
            killerUnitTagIndex=d["killerUnitTagIndex"],
            killerUnitTagRecycle=d["killerUnitTagRecycle"],
            loop=d["loop"],
            unitTagIndex=d["unitTagIndex"],
            unitTagRecycle=["unitTagRecycle"],
            x=d["x"],
            y=d["y"],
        )

    def __init__(
        self,
        id: int,
        killerPlayerId: int,
        killerUnitTagIndex: int,
        killerUnitTagRecycle: int,
        loop: int,
        unitTagIndex: int,
        unitTagRecycle: int,
        x: int,
        y: int,
    ) -> None:

        self.id = id
        self.killerPlayerId = killerPlayerId
        self.killerUnitTagIndex = killerUnitTagIndex
        self.killerUnitTagRecycle = killerUnitTagRecycle
        self.loop = loop
        self.unitTagIndex = unitTagIndex
        self.unitTagRecycle = unitTagRecycle
        self.x = x
        self.y = y
