from typing import Dict

from src.dataset.replay_data.replay_parser.tracker_events.tracker_event import (
    TrackerEvent,
)

# TODO: Document the docstrings


class UnitOwnerChange(TrackerEvent):
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
    :param upkeepPlayerId: _description_
    :type upkeepPlayerId: int
    """

    def from_dict(d: Dict[str, int]) -> "UnitOwnerChange":
        """
        _summary_

        :param d: _description_
        :type d: Dict
        :return: _description_
        :rtype: UnitOwnerChange
        """
        return UnitOwnerChange(
            controlPlayerId=d["controlPlayerId"],
            id=d["id"],
            loop=d["loop"],
            unitTagIndex=d["unitTagIndex"],
            unitTagRecycle=d["unitTagRecycle"],
            upkeepPlayerId=d["upkeepPlayerId"],
        )

    def __init__(
        self,
        controlPlayerId: int,
        id: int,
        loop: int,
        unitTagIndex: int,
        unitTagRecycle: int,
        upkeepPlayerId: int,
    ) -> None:

        self.controlPlayerId = controlPlayerId
        self.id = id
        self.loop = loop
        self.unitTagIndex = unitTagIndex
        self.unitTagRecycle = unitTagRecycle
        self.upkeepPlayerId = upkeepPlayerId
