from typing import Dict, List

from src.dataset.replay_data.replay_parser.tracker_events.tracker_event import (
    TrackerEvent,
)

# TODO: Document the docstrings


class UnitPositions(TrackerEvent):

    """_summary_

    :param firstUnitIndex: _description_
    :type firstUnitIndex: int
    :param id: _description_
    :type id: int
    :param items: _description_
    :type items: List[int]
    :param loop: _description_
    :type loop: int
    """

    def from_dict(d: Dict) -> "UnitPositions":
        """
        _summary_

        :param d: _description_
        :type d: Dict
        :return: _description_
        :rtype: UnitPositions
        """
        return UnitPositions(
            firstUnitIndex=d["firstUnitIndex"],
            id=d["id"],
            items=d["items"],
            loop=d["loop"],
        )

    def __init__(
        self,
        firstUnitIndex: int,
        id: int,
        items: List[int],
        loop: int,
    ) -> None:

        self.firstUnitIndex = firstUnitIndex
        self.id = id
        self.items = items
        self.loop = loop
