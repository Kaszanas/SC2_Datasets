from typing import Dict
from src.dataset.replay_structures.tracker_events.tracker_event import TrackerEvent

# TODO: Document the docstrings


class UnitBorn(TrackerEvent):

    """
    _summary_

    :param controlPlayerId: _description_
    :type controlPlayerId: int
    :param id: _description_
    :type id: int
    :param loop: _description_
    :type loop: int
    :param unitTagIndex: _description_
    :type unitTagIndex: int
    :param unitTagRecycle: _description_
    :type unitTagRecycle: int
    :param unitTypeName: _description_
    :type unitTypeName: str
    :param upkeepPlayerId: _description_
    :type upkeepPlayerId: int
    :param x: _description_
    :type x: int
    :param y: _description_
    :type y: int
    """

    def from_dict(d: Dict) -> "UnitBorn":
        """
        _summary_

        :param d: _description_
        :type d: Dict
        :return: _description_
        :rtype: UnitBorn
        """
        return UnitBorn(
            controlPlayerId=d["controlPlayerId"],
            id=d["id"],
            loop=d["loop"],
            unitTagIndex=d["unitTagIndex"],
            unitTagRecycle=d["unitTagRecycle"],
            unitTypeName=d["unitTypeName"],
            upkeepPlayerId=d["upkeepPlayerId"],
            x=d["x"],
            y=d["y"],
        )

    def __init__(
        self,
        controlPlayerId: int,
        id: int,
        loop: int,
        unitTagIndex: int,
        unitTagRecycle: int,
        unitTypeName: str,
        upkeepPlayerId: int,
        x: int,
        y: int,
    ) -> None:
        """_summary_

        :param controlPlayerId: _description_
        :type controlPlayerId: int
        :param id: _description_
        :type id: int
        :param loop: _description_
        :type loop: int
        :param unitTagIndex: _description_
        :type unitTagIndex: int
        :param unitTagRecycle: _description_
        :type unitTagRecycle: int
        :param unitTypeName: _description_
        :type unitTypeName: str
        :param upkeepPlayerId: _description_
        :type upkeepPlayerId: int
        :param x: _description_
        :type x: int
        :param y: _description_
        :type y: int
        """
        self.controlPlayerId = controlPlayerId
        self.id = id
        self.loop = loop
        self.unitTagIndex = unitTagIndex
        self.unitTagRecycle = unitTagRecycle
        self.unitTypeName = unitTypeName
        self.upkeepPlayerId = upkeepPlayerId
        self.x = x
        self.y = y
