from typing import Dict

from src.dataset.replay_data.replay_parser.game_events.events.nested.target_2d import (
    Target2D,
)
from src.dataset.replay_data.replay_parser.game_events.game_event import GameEvent


# TODO: Document the docstrings
class CameraSave(GameEvent):
    """
    _summary_

    :param id: _description_
    :type id: int
    :param loop: _description_
    :type loop: int
    :param target: _description_
    :type target: Target
    :param userid: _description_
    :type userid: int
    :param which: _description_
    :type which: int
    """

    @staticmethod
    def from_dict(d: Dict) -> "CameraSave":
        """
        _summary_

        :param d: _description_
        :type d: Dict
        :return: _description_
        :rtype: CameraSave
        """
        return CameraSave(
            id=d["id"],
            loop=d["loop"],
            target=Target2D(x=d["target"]["x"], y=d["target"]["y"]),
            userid=d["userid"]["userId"],
            which=d["which"],
        )

    def __init__(
        self,
        id: int,
        loop: int,
        target: Target2D,
        userid: int,
        which: int,
    ) -> None:
        self.id = id
        self.loop = loop
        self.target = target
        self.userid = userid
        self.which = which
