from typing import Any, Dict


class Metadata:
    """
    Specifies a class which includes parameters about the game,
    like version, build, map, etc., the game was played.

    Parameters
    ----------
    baseBuild : str
        Specifies a build number of the game engine.
    dataBuild : str
        Specifies a number of the build.
    gameVersion : str
        Specifies a number of the game version when the game was played.
    mapName : str
        Specifies a name of the map on which the game was played.
    """

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Metadata":
        """
        Represents metadata extracted from a .SC2Replay file.

        Parameters
        ----------
        baseBuild : str
            Specifies a build number of the game engine.
        dataBuild : str
            Specifies a number of the build.
        gameVersion : str
            Specifies a number of game version when the game was played.
        mapName : str
            Specifies a name of the map on what the game was played.
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
