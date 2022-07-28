from typing import Any, Dict


class Metadata:
    """
    Specifies a class which includes parameters about the game,
    like version, build, map etc. the game was played

    :param baseBuild: Specifies a build number of the game engine.
    :type baseBuild: str
    :param dataBuild: Specifies a number of the build
    :type dataBuild: str
    :param gameVersion: Specifies a number of game version when the game was played
    :type gameVersion: str
    :param mapName: Specifies a name of the mapa on what the game was played
    :type mapName: str
    """

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Metadata":
        """
        Static method returning initialized Metadata class from a dictionary.
        This helps with the original JSON parsing.

        :param d: Specifies a dictionary as available in the JSON file\
        that is a result of pre-processing some .SC2Replay file.
        :type d: Dict[str, Any]
        :return: Returns an initialized Metadata class.
        :rtype: Metadata
        """
        return Metadata(
            baseBuild=d["baseBuild"],
            dataBuild=d["dataBuild"],
            gameVersion=d["gameVersion"],
            mapName=d["mapName"],
        )

    def __init__(
        self,
        baseBuild: str,
        dataBuild: str,
        gameVersion: str,
        mapName: str,
    ) -> None:

        self.baseBuild = baseBuild
        self.dataBuild = dataBuild
        self.gameVersion = gameVersion
        self.mapName = mapName
