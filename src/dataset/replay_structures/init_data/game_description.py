from typing import Any, Dict
from src.dataset.replay_structures.init_data.game_options import GameOptions


class GameDescription:

    """
    _summary_

    :param gameOptions: _description_
    :type gameOptions: GameOptions
    :param gameSpeed: _description_
    :type gameSpeed: str
    :param isBlizzardMap: _description_
    :type isBlizzardMap: bool
    :param mapAuthorName: _description_
    :type mapAuthorName: str
    :param mapFileSyncChecksum: _description_
    :type mapFileSyncChecksum: int
    :param mapSizeX: _description_
    :type mapSizeX: int
    :param mapSizeY: _description_
    :type mapSizeY: int
    :param maxPlayers: _description_
    :type maxPlayers: int
    """

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GameDescription":
        """
        _summary_

        :param d: _description_
        :type d: Dict[str, Any]
        :return: _description_
        :rtype: GameDescription
        """
        return GameDescription(
            gameOptions=GameOptions.from_dict(d=d["gameOptions"]),
            gameSpeed=d["gameSpeed"],
            isBlizzardMap=d["isBlizzardMap"],
            mapAuthorName=d["mapAuthorName"],
            mapFileSyncChecksum=d["mapFileSyncChecksum"],
            mapSizeX=d["mapSizeX"],
            mapSizeY=d["mapSizeY"],
            maxPlayers=d["maxPlayers"],
        )

    def __init__(
        self,
        gameOptions: GameOptions,
        gameSpeed: str,
        isBlizzardMap: bool,
        mapAuthorName: str,
        mapFileSyncChecksum: int,
        mapSizeX: int,
        mapSizeY: int,
        maxPlayers: int,
    ) -> None:

        self.gameOptions = gameOptions
        self.gameSpeed = gameSpeed
        self.isBlizzardMap = isBlizzardMap
        self.mapAuthorName = mapAuthorName
        self.mapFileSyncChecksum = mapFileSyncChecksum
        self.mapSizeX = mapSizeX
        self.mapSizeY = mapSizeY
        self.maxPlayers = maxPlayers
