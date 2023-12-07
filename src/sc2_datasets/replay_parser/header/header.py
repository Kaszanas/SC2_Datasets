from typing import Any, Dict


class Header:
    """
    Class representing the parameters of a replay header.

    Parameters
    ----------
    elapsedGameLoops : int
        The duration of the game in game loops (game-engine ticks).

    version : str
        The game version used by players during the game.
    """

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Header":
        """
        Static method returning an initialized Header class from a provided dictionary.
        This method assists in parsing the original JSON representation of a .SC2Replay file.

        Parameters
        ----------
        d : Dict[str, Any]
            A dictionary representing the data available in the JSON file, obtained
            from preprocessing some .SC2Replay file.

        Returns
        -------
        Header
            An initialized instance of the Header class.

        Examples
        --------
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
