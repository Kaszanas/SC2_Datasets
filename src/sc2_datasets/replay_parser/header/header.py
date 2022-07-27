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
        Static method returning initialized Header class from a dictionary.
        This helps with the original JSON parsing.

        :param d: Specifies a dictionary as available in the JSON file\
        that is a result of pre-processing some .SC2Replay file.
        :type d: Dict[str, Any]
        :return: Returns an initialized Header class.
        :rtype: Header

        **Correct Usage Examples:**

        Using from_dict factory method provides ease of use when parsing
        a replay pre-processed with SC2InfoExtractorGo_

        This method requires a dictionary representation of data
        to be passed as a parameter because of the built in json parser provided
        by the Python standard library.

        _SC2InfoExtractorGo: https://github.com/Kaszanas/SC2InfoExtractorGo

        The use of this method is intended to get header information from
        the game's json representation.

        >>> elapsedGameLoops = 10000
        >>> version = "3.12.0.51702"
        >>> Header(
        ...    elapsedGameLoops=d["elapsedGameLoops"],
        ...    version=d["version"])

        >>> assert isinstance(elapsedGameLoops, int)
        >>> assert elapsedGameLoops > 0
        >>> assert isinstance(version, str)

        **Incorrect Usage Examples:**

        >>> elapsedGameLoops_wrong = "text"
        >>> version_wrong = int(2)
        >>> Header(
        ...    elapsedGameLoops=elapsedGameLoops_wrong,
        ...    version=version_wrong)
        Traceback (most recent call last):
        ...
        TypeError: unsupported operand type(s) ...

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
