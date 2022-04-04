from typing import Any, Dict
from src.dataset.replay_data.replay_parser.init_data.game_description import (
    GameDescription,
)


class InitData:

    """
    _summary_

    :param gameDescription: _description_
    :type gameDescription: GameDescription
    """

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "InitData":
        """
        _summary_

        :param d: _description_
        :type d: Dict[str, Any]
        :return: _description_
        :rtype: InitData
        """
        return InitData(
            gameDescription=GameDescription.from_dict(d=d["gameDescription"])
        )

    def __init__(self, gameDescription: GameDescription) -> None:

        self.gameDescription = gameDescription
