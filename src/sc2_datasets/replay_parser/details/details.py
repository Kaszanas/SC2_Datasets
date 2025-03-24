from typing import Any, Dict


class Details:
    """
    Data type containing details about a StarCraft II game.

    Parameters
    ----------
    gameSpeed : str
        Game speed setting as configured in the game options.
        Can be "slower", "slow", "normal", "fast", or "faster".
        Typically, competitive or ranked games are played on "faster".
        Additional information: https://liquipedia.net/starcraft2/Game_Speed
    isBlizzardMap : bool
        Specifies if the map used in the replay was approved and published by Blizzard (the game publisher).
    timeUTC : str
        Denotes the time at which the game was started in Coordinated Universal Time.
    """

    # REVIEW: Doctests for this:
    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Details":
        """
        Static method returning an initialized Details class from a dictionary.
        This aids in the original JSON parsing.

        Parameters
        ----------
        d : Dict[str, Any]
            Dictionary obtained from pre-processing an .SC2Replay file in JSON format.

        Returns
        -------
        Details
            Initialized Details class instance.


        Examples
        --------
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
