from typing import Dict

from src.dataset.replay_data.replay_parser.game_events.events.nested.target_3d import (
    Target3D,
)
from src.dataset.replay_data.replay_parser.game_events.game_event import GameEvent


# TODO: Document the docstrings


class CmdUpdateTargetPoint(GameEvent):
    """
    _summary_

    :param id: _description_
    :type id: int
    :param loop: _description_
    :type loop: int
    :param target: _description_
    :type target: Target3D
    :param userid: _description_
    :type userid: int
    """

    @staticmethod
    def from_dict(d: Dict) -> "CmdUpdateTargetPoint":
        """
        _summary_

        :param d: _description_
        :type d: Dict
        :return: _description_
        :rtype: CmdUpdateTargetPoint
        """
        return CmdUpdateTargetPoint(
            id=d["id"],
            loop=d["loop"],
            target=Target3D(x=d["target"]["x"], y=d["target"]["y"], z=d["target"]["z"]),
            userid=d["userid"]["userId"],
        )

    def __init__(
        self,
        id: int,
        loop: int,
        target: Target3D,
        userid: int,
    ) -> None:
        self.id = id
        self.loop = loop
        self.target = target
        self.userid = userid
