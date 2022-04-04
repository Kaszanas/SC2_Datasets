from typing import Dict

import torch
from src.dataset.replay_data.replay_parser.game_events.game_event import GameEvent

# TODO: Document the docstrings


class GameUserLeave(GameEvent):
    """
    _summary_

    :param id: _description_
    :type id: int
    :param leaveReason: _description_
    :type leaveReason: int
    :param loop: _description_
    :type loop: int
    :param userid: _description_
    :type userid: int
    """

    @staticmethod
    def from_dict(d: Dict) -> "GameUserLeave":
        """_summary_

        :param d: _description_
        :type d: Dict
        :return: _description_
        :rtype: GameUserLeave
        """
        return GameUserLeave(
            id=d["id"],
            leaveReason=d["leaveReason"],
            loop=d["loop"],
            userid=d["userid"]["userId"],
        )

    def __init__(
        self,
        id: int,
        leaveReason: int,
        loop: int,
        userid: int,
    ) -> None:

        self.id = id
        self.leaveReason = leaveReason
        self.loop = loop
        self.userid = userid

    def to_tensor(self) -> torch.Tensor:
        pass
