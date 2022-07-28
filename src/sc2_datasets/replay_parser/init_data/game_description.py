from typing import Any, Dict

from sc2_datasets.replay_parser.init_data.game_options import GameOptions


class GameDescription:
    """
    GameDescription specifies an information about some basic parameters
    of a StarCraft II replay.

    :param gameOptions: Specifies options in the game,\
    for example you can set: fog, random races, competitive, etc.
    :type gameOptions: GameOptions
    :param gameSpeed: Specifies the speed at which your game runs.\
    Enum: [Slower, Slow, Normal, Fast, Faster]. Default is Faster
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
        Static method returning initialized GameDescription class from a dictionary.
        This helps with the original JSON parsing.

        :param d: Specifies a dictionary as available in the JSON file that is\
        a result of pre-processing some .SC2Replay file.
        :type d: Dict[str, Any]
        :return: Returns an initialized GameDescription class.
        :rtype: GameDescription

        **Correct Usage Examples:**

        Using from_dict factory method provides ease of use when parsing
        a replay pre-processed with SC2InfoExtractorGo_

        This method requires a dictionary representation of data to be passed
        as a parameter because of the built in json parser provided by the Python standard library.

        _SC2InfoExtractorGo: https://github.com/Kaszanas/SC2InfoExtractorGo

        The use of this method is intended to get game description information
        from the game's json representation.

        >>> from sc2egset_dataset.dataset.replay_data.replay_parser.init_data.game_options import GameOptions  #noqa
        >>> game_options_object = {
        ...        "advancedSharedControl": False,
        ...        "amm": False,
        ...        "battleNet": False,
        ...        "clientDebugFlags": 265,
        ...        "competitive": False,
        ...        "cooperative": False,
        ...        "fog": 0,
        ...        "heroDuplicatesAllowed": True,
        ...        "lockTeams": True,
        ...        "noVictoryOrDefeat": False,
        ...        "observers": 0,
        ...        "practice": False,
        ...        "randomRaces": False,
        ...        "teamsTogether": False,
        ...        "userDifficulty": 0}
        ...
        >>> game_description_dict ={
        ...      "gameOptions": game_options_object,
        ...      "gameSpeed": "Faster",
        ...      "isBlizzardMap": True,
        ...      "mapAuthorName": "98-S2-1-26",
        ...      "mapFileSyncChecksum": 2133219109,
        ...      "mapSizeX": 144,
        ...      "mapSizeY": 160,
        ...      "maxPlayers": 2
        ...    }
        ...
        >>> game_description_object = GameDescription.from_dict(d=game_description_dict)
        ...
        >>> assert isinstance(game_description_object, GameDescription)
        >>> assert isinstance(game_description_object.gameOptions, GameOptions)
        >>> assert isinstance(game_description_object.gameSpeed, str)
        >>> assert isinstance(game_description_object.isBlizzardMap, bool)
        >>> assert isinstance(game_description_object.mapAuthorName, str)
        >>> assert isinstance(game_description_object.mapFileSyncChecksum, int)
        >>> assert isinstance(game_description_object.mapSizeX, int)
        >>> assert isinstance(game_description_object.mapSizeY, int)
        >>> assert isinstance(game_description_object.maxPlayers, int)
        ...
        >>> assert game_description_object.gameOptions == game_options_object
        >>> assert game_description_object.gameSpeed == "Faster"
        >>> assert game_description_object.isBlizzardMap == True
        >>> assert game_description_object.mapAuthorName == "98-S2-1-26"
        >>> assert game_description_object.mapFileSyncChecksum == 2133219109
        >>> assert game_description_object.mapSizeX == 144
        >>> assert game_description_object.mapSizeY == 160
        >>> assert game_description_object.maxPlayers == 2
        ...
        >>> assert game_description_object.mapFileSyncChecksum > 0
        >>> assert game_description_object.mapSizeX > 0
        >>> assert game_description_object.mapSizeY > 0
        >>> assert game_description_object.maxPlayers > 0

        **Incorrect Usage Examples:**

        >>> gameOptions_value_wrong = "False"
        >>> gameSpeed_value_wrong = True
        >>> isBlizzardMap_value_wrong = "wrong type"
        >>> mapAuthorName_value_wrong = int(2)
        >>> mapFileSyncChecksum_value_wrong = str(2)
        >>> mapSizeX_value_wrong = str(2)
        >>> mapSizeY_value_wrong = str(2)
        >>> maxPlayers_value_wrong = str(2)

        >>> GameDescription(
        ...    gameOptions=gameOptions_value_wrong,
        ...    gameSpeed=gameSpeed_value_wrong,
        ...    isBlizzardMap=isBlizzardMap_value_wrong,
        ...    mapAuthorName=mapAuthorName_value_wrong,
        ...    mapFileSyncChecksum=mapFileSyncChecksum_value_wrong,
        ...    mapSizeX=mapSizeX_value_wrong,
        ...    mapSizeY=mapSizeY_value_wrong,
        ...    maxPlayers=maxPlayers_value_wrong)
        Traceback (most recent call last):
        ...
        TypeError: unsupported operand type(s) ...
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
