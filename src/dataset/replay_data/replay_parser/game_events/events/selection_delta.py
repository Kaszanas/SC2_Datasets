from typing import Dict

import torch
from src.dataset.replay_data.replay_parser.game_events.events.nested.delta import Delta
from src.dataset.replay_data.replay_parser.game_events.game_event import GameEvent

# TODO: Document the docstrings


class SelectionDelta(GameEvent):

    """
    _summary_

    :param controlGroupId: _description_
    :type controlGroupId: int
    :param delta: _description_
    :type delta: Delta
    :param id: _description_
    :type id: int
    :param loop: _description_
    :type loop: int
    :param userid: _description_
    :type userid: int
    """

    @staticmethod
    def from_dict(d: Dict) -> "SelectionDelta":
        """
        _summary_

        :param d: _description_
        :type d: Dict
        :return: _description_
        :rtype: SelectionDelta
        """
        return SelectionDelta(
            controlGroupId=d["controlGroupId"],
            delta=Delta.from_dict(d=d["delta"]),
            id=d["id"],
            loop=d["loop"],
            userid=d["userid"]["userId"],
        )

    def __init__(
        self,
        controlGroupId: int,
        delta: Delta,
        id: int,
        loop: int,
        userid: int,
    ) -> None:

        self.controlGroupId = controlGroupId
        self.delta = delta
        self.id = id
        self.loop = loop
        self.userid = userid

    def to_tensor(self) -> torch.Tensor:
        pass
