from types import NoneType
from typing import Dict

import torch

from src.dataset.replay_data.replay_parser.game_events.events.nested.target_2d import (
    Target2D,
)
from src.dataset.replay_data.replay_parser.game_events.game_event import GameEvent


# TODO: There are some null values in the data
# it needs to be verified if such null values are a problem for later calculations with the dataset?
# Should this be encoded somehow?
# TODO: Document the docstrings


class CameraUpdate(GameEvent):

    """_summary_

    :param distance: _description_
    :type distance: NoneType | float | int
    :param follow: _description_
    :type follow: bool
    :param id: _description_
    :type id: int
    :param loop: _description_
    :type loop: int
    :param pitch: _description_
    :type pitch: NoneType | float | int
    :param reason: _description_
    :type reason: NoneType | str
    :param target: _description_
    :type target: Target
    :param userid: _description_
    :type userid: int
    :param yaw: _description_
    :type yaw: NoneType | float | int
    """

    @staticmethod
    def from_dict(d: Dict):
        """
        _summary_

        :param d: _description_
        :type d: Dict
        :return: _description_
        :rtype: _type_
        """
        return CameraUpdate(
            distance=d["distance"],
            follow=d["follow"],
            id=d["id"],
            loop=d["loop"],
            pitch=d["pitch"],
            reason=d["reason"],
            target=Target2D(x=d["target"]["x"], y=d["target"]["y"]),
            userid=d["userid"]["userId"],
            yaw=d["yaw"],
        )

    def __init__(
        self,
        distance: NoneType | float | int,
        follow: bool,
        id: int,
        loop: int,
        pitch: NoneType | float | int,
        reason: NoneType | str,
        target: Target2D,
        userid: int,
        yaw: NoneType | float | int,
    ) -> None:

        self.distance = distance
        self.follow = follow
        self.id = id
        self.loop = loop
        self.pitch = pitch
        self.reason = reason
        self.target = target
        self.userid = userid
        self.yaw = yaw

    def to_tensor(self) -> torch.Tensor:
        pass
