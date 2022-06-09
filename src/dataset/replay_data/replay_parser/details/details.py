from typing import Any, Dict


class Details:
    """
    Data type containing some "details" information about an StarCraft II game.

    :param gameSpeed: Game speed setting as set in the game options. Can be one of "slower", "slow", "normal", "fast", or "faster". Typically competitive or ranked games are played on "faster" setting. Additional information is available at: https://liquipedia.net/starcraft2/Game_Speed
    :type gameSpeed: str
    :param isBlizzardMap: Specifies if the map that  was used in the replay was approved by Blizzard (game publisher)
    :type isBlizzardMap: bool
    :param timeUTC: Denotes the time at which the game was started.
    :type timeUTC: str
    """

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Details":
        """
        Static method returning initialized Details class from a dictionary. This helps with the original JSON parsing.

        :param d: Specifies a dictionary as available in the JSON file that is a result of pre-processing some .SC2Replay file.
        :type d: Dict[str, Any]
        :return: Returns an initialized Details class.
        :rtype: Details
        """
        return Details(
            gameSpeed=d["gameSpeed"],
            isBlizzardMap=d["isBlizzardMap"],
            timeUTC=d["timeUTC"],
        )

    def __init__(
        self,
        gameSpeed: str,
        isBlizzardMap: bool,
        timeUTC: str,
    ) -> None:
        self.gameSpeed = gameSpeed
        self.isBlizzardMap = isBlizzardMap
        self.timeUTC = timeUTC
