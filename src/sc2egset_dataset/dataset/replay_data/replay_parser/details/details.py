from typing import Any, Dict


class Details:
    """
    Data type containing some "details" information about an StarCraft II game.

    :param gameSpeed: Game speed setting as set in the game options.\
    Can be one of "slower", "slow", "normal", "fast", or "faster".\
    Typically competitive or ranked games are played on "faster" setting.\
    Additional information is available at: https://liquipedia.net/starcraft2/Game_Speed
    :type gameSpeed: str
    :param isBlizzardMap: Specifies if the map that was used\
    in the replay was approved and published by Blizzard (game publisher)
    :type isBlizzardMap: bool
    :param timeUTC: Denotes the time at which the game was started.
    :type timeUTC: str
    """

    # REVIEW: Doctests for this:
    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Details":
        """
        Static method returning initialized Details class from a dictionary.
        This helps with the original JSON parsing.

        :param d: Specifies a dictionary as available in the JSON file\
        that is a result of pre-processing some .SC2Replay file.
        :type d: Dict[str, Any]
        :return: Returns an initialized Details class.
        :rtype: Details

        **Correct Usage Examples:**

        Using from_dict factory method provides ease of use when parsing
        a replay pre-processed with SC2InfoExtractorGo_.
        This method requires a dictionary representation of data
        to be passed as a parameter because of the built-in json parser
        provided by the Python standard library.

        .. _SC2InfoExtractorGo: https://github.com/Kaszanas/SC2InfoExtractorGo

        >>> details_dict = {"gameSpeed": "Faster",
        ...                 "isBlizzardMap": True,
        ...                 "timeUTC": "2017-04-29T05:15:32.4903483+02:00"}
        >>> details_object = Details.from_dict(d=details_dict)
        >>> assert isinstance(details_object, Details)
        >>> assert details_object.gameSpeed == "Faster"
        >>> assert details_object.isBlizzardMap == True
        >>> assert details_object.timeUTC == "2017-04-29T05:15:32.4903483+02:00"
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
