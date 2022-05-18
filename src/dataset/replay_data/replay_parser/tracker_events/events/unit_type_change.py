from typing import Dict


from src.dataset.replay_data.replay_parser.tracker_events.tracker_event import (
    TrackerEvent,
)

# TODO: Document the docstrings


class UnitTypeChange(TrackerEvent):

    """
    _summary_

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
    """

    @staticmethod
    def from_dict(d: Dict) -> "UnitTypeChange":
        """_summary_

        :param d: _description_
        :type d: Dict
        :return: _description_
        :rtype: UnitTypeChange
        """
        return UnitTypeChange(
            id=d["id"],
            loop=d["loop"],
            unitTagIndex=d["unitTagIndex"],
            unitTagRecycle=d["unitTagRecycle"],
            unitTypeName=d["unitTypeName"],
        )

    def __init__(
        self,
        id: int,
        loop: int,
        unitTagIndex: int,
        unitTagRecycle: int,
        unitTypeName: str,
    ) -> None:

        self.id = id
        self.loop = loop
        self.unitTagIndex = unitTagIndex
        self.unitTagRecycle = unitTagRecycle
        self.unitTypeName = unitTypeName
