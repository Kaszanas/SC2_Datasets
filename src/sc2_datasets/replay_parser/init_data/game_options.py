from typing import Any, Dict


class GameOptions:
    """
    GameOptions represents the replay game options

    :param advancedSharedControl: Specifies if advanced shared control is enabled
    :type advancedSharedControl: bool
    :param amm: Specifies if AMM (AutoMM - Automated Match Making) is enabled
    :type amm: bool
    :param battleNet: Specifies if game has been played on Battle.net
    :type battleNet: bool
    :param clientDebugFlags: Specifies the client debug flag
    :type clientDebugFlags: int
    :param competitive: It means either ranked or unranked,
    :type competitive: bool
    :param cooperative: Specifies if game was cooperative
    :type cooperative: bool
    :param fog: Specifies the value of fog in the game
    :type fog: int
    :param heroDuplicatesAllowed: Specifies if hero can be duplicated
    :type heroDuplicatesAllowed: bool
    :param lockTeams: Specifies if teams are locked
    :type lockTeams: bool
    :param noVictoryOrDefeat: There is no information about this parameter
    :type noVictoryOrDefeat: bool
    :param observers: Specifies count of observers watching the game
    :type observers: int
    :param practice: There is no information about this parameter
    :type practice: bool
    :param randomRaces: Specifies if random races are in the game
    :type randomRaces: bool
    :param teamsTogether: Specifies if teams of players are in the game
    :type teamsTogether: bool
    :param userDifficulty: There is no information about this parameter
    :type userDifficulty: bool
    """

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GameOptions":
        """
        Static method returning initialized GameOptions class from a dictionary.
        This helps with the original JSON parsing.

        :param d: Describes a dictionary, it holds translations of a phrase or sentence
        :type d: Dict[str, Any]
        :return: Specifies a list of parameters about the game like\
        a number of observers, fog of the game, if the game was competitive etc.
        :rtype: GameOptions

        **Correct Usage Examples:**

        Using from_dict factory method provides ease of use when parsing
        a replay pre-processed with SC2InfoExtractorGo_

        This method requires a dictionary representation of data to be passed
        as a parameter because of the built
        in json parser provided by the Python standard library.

        _SC2InfoExtractorGo: https://github.com/Kaszanas/SC2InfoExtractorGo

        The use of this method is intended to get game options information
        from the game's json representation.

        >>> game_options_dict = {
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
        >>> game_options_object = GameOptions.from_dict(d=game_options_dict)
        ...
        >>> assert isinstance(game_options_object, GameOptions)
        >>> assert isinstance(game_options_object.advancedSharedControl, bool)
        >>> assert isinstance(game_options_object.amm, bool)
        >>> assert isinstance(game_options_object.battleNet, bool)
        >>> assert isinstance(game_options_object.clientDebugFlags, int)
        >>> assert isinstance(game_options_object.competitive, bool)
        >>> assert isinstance(game_options_object.cooperative, bool)
        >>> assert isinstance(game_options_object.fog, int)
        >>> assert isinstance(game_options_object.heroDuplicatesAllowed, bool)
        >>> assert isinstance(game_options_object.lockTeams, bool)
        >>> assert isinstance(game_options_object.noVictoryOrDefeat, bool)
        >>> assert isinstance(game_options_object.observers, int)
        >>> assert isinstance(game_options_object.practice, bool)
        >>> assert isinstance(game_options_object.randomRaces, bool)
        >>> assert isinstance(game_options_object.teamsTogether, bool)
        >>> assert isinstance(game_options_object.userDifficulty, int)
        ...
        >>> assert game_options_object.advancedSharedControl == False
        >>> assert game_options_object.amm == False
        >>> assert game_options_object.battleNet == False
        >>> assert game_options_object.clientDebugFlags == 265
        >>> assert game_options_object.competitive == False
        >>> assert game_options_object.cooperative == False
        >>> assert game_options_object.fog == 0
        >>> assert game_options_object.heroDuplicatesAllowed == True
        >>> assert game_options_object.lockTeams == True
        >>> assert game_options_object.noVictoryOrDefeat == False
        >>> assert game_options_object.observers == 0
        >>> assert game_options_object.practice == False
        >>> assert game_options_object.randomRaces == False
        >>> assert game_options_object.teamsTogether == False
        >>> assert game_options_object.userDifficulty == 0
        ...
        >>> assert game_options_object.clientDebugFlags >= 0
        >>> assert game_options_object.fog >= 0
        >>> assert game_options_object.observers >= 0
        >>> assert game_options_object.userDifficulty >= 0

        **Incorrect Usage Examples:**

        >>> advancedSharedControl_wrong = "False"
        >>> amm_wrong = True
        >>> battleNet_wrong = "wrong type"
        >>> clientDebugFlags_wrong = int(2)
        >>> competitive_wrong = str(2)
        >>> cooperative_wrong = str(2)
        >>> fog_wrong = str(2)
        >>> heroDuplicatesAllowed_wrong = str(2)
        >>> lockTeams_wrong = str(2)
        >>> noVictoryOrDefeat_wrong = str(2)
        >>> observers_wrong = str(2)
        >>> practice_wrong = str(2)
        >>> randomRaces_wrong = str(2)
        >>> teamsTogether_wrong = str(2)
        >>> userDifficulty_wrong = str(2)

        >>> GameOptions(
        ...    advancedSharedControl=advancedSharedControl_wrong,
        ...    amm=amm_wrong,
        ...    battleNet=battleNet_wrong,
        ...    clientDebugFlags=clientDebugFlags_wrong,
        ...    competitive=competitive_wrong,
        ...    cooperative=cooperative_wrong,
        ...    fog=fog_wrong,
        ...    heroDuplicatesAllowed=heroDuplicatesAllowed_wrong,
        ...    lockTeams=lockTeams_wrong,
        ...    noVictoryOrDefeat=observers_wrong,
        ...    observers=practice_wrong,
        ...    practice=practice_wrong,
        ...    randomRaces=randomRaces_wrong,
        ...    teamsTogether=teamsTogether_wrong,
        ...    userDifficulty=userDifficulty_wrong)
        Traceback (most recent call last):
        ...
        TypeError: unsupported operand type(s) ...

        """

        return GameOptions(
            advancedSharedControl=d["advancedSharedControl"],
            amm=d["amm"],
            battleNet=d["battleNet"],
            clientDebugFlags=d["clientDebugFlags"],
            competitive=d["competitive"],
            cooperative=d["cooperative"],
            fog=d["fog"],
            heroDuplicatesAllowed=d["heroDuplicatesAllowed"],
            lockTeams=d["lockTeams"],
            noVictoryOrDefeat=d["noVictoryOrDefeat"],
            observers=d["observers"],
            practice=d["practice"],
            randomRaces=d["randomRaces"],
            teamsTogether=d["teamsTogether"],
            userDifficulty=d["userDifficulty"],
        )

    def __init__(
        self,
        advancedSharedControl: bool,
        amm: bool,
        battleNet: bool,
        clientDebugFlags: int,
        competitive: bool,
        cooperative: bool,
        fog: int,
        heroDuplicatesAllowed: bool,
        lockTeams: bool,
        noVictoryOrDefeat: bool,
        observers: int,
        practice: bool,
        randomRaces: bool,
        teamsTogether: bool,
        userDifficulty: bool,
    ) -> None:
        self.advancedSharedControl = advancedSharedControl
        self.amm = amm
        self.battleNet = battleNet
        self.clientDebugFlags = clientDebugFlags
        self.competitive = competitive
        self.cooperative = cooperative
        self.fog = fog
        self.heroDuplicatesAllowed = heroDuplicatesAllowed
        self.lockTeams = lockTeams
        self.noVictoryOrDefeat = noVictoryOrDefeat
        self.observers = observers
        self.practice = practice
        self.randomRaces = randomRaces
        self.teamsTogether = teamsTogether
        self.userDifficulty = userDifficulty
