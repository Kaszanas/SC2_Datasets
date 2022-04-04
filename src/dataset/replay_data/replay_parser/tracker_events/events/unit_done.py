from typing import Dict

import torch
from src.dataset.replay_data.replay_parser.tracker_events.tracker_event import (
    TrackerEvent,
)

# TODO: Document the docstrings


class UnitDone(TrackerEvent):

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
    """

    @staticmethod
    def from_dict(d: Dict) -> "UnitDone":
        """
        _summary_

        :param d: _description_
        :type d: Dict
        :return: _description_
        :rtype: UnitDone
        """
        return UnitDone(
            id=d["id"],
            loop=d["loop"],
            unitTagIndex=d["unitTagIndex"],
            unitTagRecycle=d["unitTagRecycle"],
        )

    def __init__(
        self,
        id: int,
        loop: int,
        unitTagIndex: int,
        unitTagRecycle: int,
    ) -> None:

        self.id = id
        self.loop = loop
        self.unitTagIndex = unitTagIndex
        self.unitTagRecycle = unitTagRecycle

    def to_tensor(self) -> torch.Tensor:
        pass
