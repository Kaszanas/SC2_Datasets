from typing import Any, Dict
from src.dataset.replay_data.replay_parser.init_data.game_description import (
    GameDescription,
)


class InitData:

    """
    Data type containing some "init data" information about StarCraft II game.

    :param gameDescription: Specifies the object that contains list of parameters which
                            are describing the game
    :type gameDescription: GameDescription
    """

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "InitData":
        """
        Static method returning initialized InitData class from a dictionary. This helps with the original JSON parsing.

        :param d: Specifies a dictionary as available in the JSON file that is a result of pre-processing some .SC2Replay file.
        :type d: Dict[str, Any]
        :return: Returns an initialized InitData class.
        :rtype: InitData
        """
        return InitData(
            gameDescription=GameDescription.from_dict(d=d["gameDescription"])
        )

    def __init__(self, gameDescription: GameDescription) -> None:
        self.gameDescription = gameDescription
