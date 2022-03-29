from dataset.replay_structures.init_data.game_options import GameOptions


class GameDescription:
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
