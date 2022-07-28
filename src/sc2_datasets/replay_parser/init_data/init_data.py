from typing import Any, Dict

from sc2_datasets.replay_parser.init_data.game_description import GameDescription


class InitData:

    """
    Data type containing some "init data" information about StarCraft II game.

    :param gameDescription: Specifies the object that contains list
    of parameters which are describing the game
    :type gameDescription: GameDescription
    """

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "InitData":
        """
        Static method returning initialized InitData class from a dictionary.
        This helps with the original JSON parsing.

        :param d: Specifies a dictionary as available in the JSON file\
        that is a result of pre-processing some .SC2Replay file.
        :type d: Dict[str, Any]
        :return: Returns an initialized InitData class.
        :rtype: InitData

        **Correct Usage Examples:**

        Using from_dict factory method provides ease of use when parsing a replay pre-processed with SC2InfoExtractorGo_

        This method requires a dictionary representation of data to be passed as a parameter because of the built in json parser provided by the Python standard library.

        _SC2InfoExtractorGo: https://github.com/Kaszanas/SC2InfoExtractorGo

        The use of this method is intended to get initialization information from the game's json representation.

        >>> from sc2egset_dataset.dataset.replay_data.replay_parser.init_data.game_options import GameOptions
        >>> from sc2egset_dataset.dataset.replay_data.replay_parser.init_data.game_description import GameDescription # noqa
        >>> gameDescription_dict ={
        ...      "gameOptions": {
        ...        "advancedSharedControl": False,
        ...        "amm": False,
        ...        "battleNet": True,
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
        ...        "userDifficulty": 0
        ...      },
        ...      "gameSpeed": "Faster",
        ...      "isBlizzardMap": True,
        ...      "mapAuthorName": "98-S2-1-26",
        ...      "mapFileSyncChecksum": 2133219109,
        ...      "mapSizeX": 144,
        ...      "mapSizeY": 160,
        ...      "maxPlayers": 2
        ...    }
        ...  }
        ...
        >>> init_data_object = InitData.from_dict(d=gameDescription_dict)
        ...
        >>> assert isinstance(init_data_object, InitData)
        >>> assert isinstance(init_data_object.gameDescription, GameDescription)
        >>> assert isinstance(init_data_object.gameDescription.gameOptions, GameOptions)
        ...
        >>> assert isinstance(init_data_object.gameDescription.gameOptions.advancedSharedControl, bool)
        >>> assert isinstance(init_data_object.gameDescription.gameOptions.amm, bool)
        >>> assert isinstance(init_data_object.gameDescription.gameOptions.battleNet, bool)
        >>> assert isinstance(init_data_object.gameDescription.gameOptions.clientDebugFlags, int)
        >>> assert isinstance(init_data_object.gameDescription.gameOptions.competitive, bool)
        >>> assert isinstance(init_data_object.gameDescription.gameOptions.cooperative, bool)
        >>> assert isinstance(init_data_object.gameDescription.gameOptions.fog, int)
        >>> assert isinstance(init_data_object.gameDescription.gameOptions.heroDuplicatesAllowed, bool)
        >>> assert isinstance(init_data_object.gameDescription.gameOptions.lockTeams, bool)
        >>> assert isinstance(init_data_object.gameDescription.gameOptions.noVictoryOrDefeat, bool)
        >>> assert isinstance(init_data_object.gameDescription.gameOptions.observers, int)
        >>> assert isinstance(init_data_object.gameDescription.gameOptions.practice, bool)
        >>> assert isinstance(init_data_object.gameDescription.gameOptions.randomRaces, bool)
        >>> assert isinstance(init_data_object.gameDescription.gameOptions.teamsTogether, bool)
        >>> assert isinstance(init_data_object.gameDescription.gameOptions.userDifficulty, int)
        ...
        >>> assert init_data_object.gameDescription.gameOptions.advancedSharedControl == False
        >>> assert init_data_object.gameDescription.gameOptions.amm == False
        >>> assert init_data_object.gameDescription.gameOptions.battleNet == False
        >>> assert init_data_object.gameDescription.gameOptions.clientDebugFlags == 265
        >>> assert init_data_object.gameDescription.gameOptions.competitive == False
        >>> assert init_data_object.gameDescription.gameOptions.cooperative == False
        >>> assert init_data_object.gameDescription.gameOptions.fog == 0
        >>> assert init_data_object.gameDescription.gameOptions.heroDuplicatesAllowed == True
        >>> assert init_data_object.gameDescription.gameOptions.lockTeams == True
        >>> assert init_data_object.gameDescription.gameOptions.noVictoryOrDefeat == False
        >>> assert init_data_object.gameDescription.gameOptions.observers == 0
        >>> assert init_data_object.gameDescription.gameOptions.practice == False
        >>> assert init_data_object.gameDescription.gameOptions.randomRaces == False
        >>> assert init_data_object.gameDescription.gameOptions.teamsTogether == False
        >>> assert init_data_object.gameDescription.gameOptions.userDifficulty == 0
        ...
        >>> assert init_data_object.gameDescription.gameOptions.clientDebugFlags >= 0
        >>> assert init_data_object.gameDescription.gameOptions.fog >= 0
        >>> assert init_data_object.gameDescription.gameOptions.observers >= 0
        >>> assert init_data_object.gameDescription.gameOptions.userDifficulty >= 0
        ...
        >>> assert isinstance(init_data_object.gameDescription.gameSpeed, str)
        >>> assert isinstance(init_data_object.gameDescription.isBlizzardMap, bool)
        >>> assert isinstance(init_data_object.gameDescription.mapAuthorName, str)
        >>> assert isinstance(init_data_object.gameDescription.mapFileSyncChecksum, int)
        >>> assert isinstance(init_data_object.gameDescription.mapSizeX, int)
        >>> assert isinstance(init_data_object.gameDescription.mapSizeY, int)
        >>> assert isinstance(init_data_object.gameDescription.maxPlayers, int)
        >>> assert isinstance(init_data_object.gameDescription.maxPlayers, int)
        ...
        >>> assert init_data_object.gameDescription.gameSpeed == "Faster"
        >>> assert init_data_object.gameDescription.isBlizzardMap == True
        >>> assert init_data_object.gameDescription.mapAuthorName == "98-S2-1-26"
        >>> assert init_data_object.gameDescription.mapFileSyncChecksum == 2133219109
        >>> assert init_data_object.gameDescription.mapSizeX == 144
        >>> assert init_data_object.gameDescription.mapSizeY == 160
        >>> assert init_data_object.gameDescription.maxPlayers == 2
        ...
        >>> assert init_data_object.gameDescription.mapFileSyncChecksum > 0
        >>> assert init_data_object.gameDescription.mapSizeX > 0
        >>> assert init_data_object.gameDescription.mapSizeY > 0
        >>> assert init_data_object.gameDescription.maxPlayers > 0

        **Incorrect Usage Examples:**

        >>> gameDescription_wrong = False
        >>> InitData(
        ...    gameDescription=gameDescription_wrong)
        Traceback (most recent call last):
        ...
        TypeError: unsupported operand type(s) ...

        """

        return InitData(
            gameDescription=GameDescription.from_dict(d=d["gameDescription"])
        )

    def __init__(self, gameDescription: GameDescription) -> None:
        self.gameDescription = gameDescription
