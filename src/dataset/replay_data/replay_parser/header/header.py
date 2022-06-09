from typing import Any, Dict


class Header:
    """
    Header represents the replay header parameters representation.

    :param elapsedGameLoops: Specifies how much game loops (game-engine ticks) the game lasted.
    :type elapsedGameLoops: int
    :param version: Specifies the game version that players have used to play the game.
    :type version: str
    """

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Header":
        """
        Static method returning initialized Header class from a dictionary. This helps with the original JSON parsing.

        :param d: Specifies a dictionary as available in the JSON file that is a result of pre-processing some .SC2Replay file.
        :type d: Dict[str, Any]
        :return: Returns an initialized Header class.
        :rtype: Header
        """
        return Header(
            elapsedGameLoops=d["elapsedGameLoops"],
            version=d["version"],
        )

    def __init__(
        self,
        elapsedGameLoops: int,
        version: str,
    ) -> None:
        self.elapsedGameLoops = elapsedGameLoops
        self.version = version
