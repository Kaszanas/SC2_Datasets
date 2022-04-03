from typing import Dict

import torch
from src.dataset.replay_data.replay_parser.game_events.game_event import GameEvent

# TODO: Document the docstrings


class CommandManagerState(GameEvent):
    """_summary_

    :param id: _description_
    :type id: int
    :param loop: _description_
    :type loop: int
    :param sequence: _description_
    :type sequence: int
    :param state: _description_
    :type state: int
    :param userid: _description_
    :type userid: int
    """

    @staticmethod
    def from_dict(d: Dict) -> "CommandManagerState":
        """_summary_

        :param d: _description_
        :type d: Dict
        :return: _description_
        :rtype: CommandManagerState
        """
        return CommandManagerState(
            id=d["id"],
            loop=d["loop"],
            sequence=d["sequence"],
            state=d["state"],
            userid=d["userid"]["userId"],
        )

    def __init__(
        self,
        id: int,
        loop: int,
        sequence: int,
        state: int,
        userid: int,
    ) -> None:

        self.id = id
        self.loop = loop
        self.sequence = sequence
        self.state = state
        self.userid = userid

    def to_tensor(self) -> torch.Tensor:
        return super().to_tensor()
