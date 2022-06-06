from typing import Any, Dict

from src.dataset.replay_data.replay_parser.init_data.game_options import GameOptions


class GameDescription:
    """
    _summary_

    :param gameOptions: Specifies options in the game, for example you can set: fog, random races, competitive, etc.
    :type gameOptions: GameOptions
    :param gameSpeed: Specifies the speed at which your game runs. Enum: [Slower, Slow, Normal, Fast, Faster].
                      Default is Faster
    :type gameSpeed: str
    :param isBlizzardMap: Specifies if map have been created by Blizzard
    :type isBlizzardMap: bool
    :param mapAuthorName: Nickname or fullname of the map's author
    :type mapAuthorName: str
    :param mapFileSyncChecksum: Specifies the map file sync checksum
    :type mapFileSyncChecksum: int
    :param mapSizeX: X coordinate size of map in pixels.
    :type mapSizeX: int
    :param mapSizeY: Y coordinate size of map in pixels.
    :type mapSizeY: int
    :param maxPlayers: Specifies how many players can play on this map at once.
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
