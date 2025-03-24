from typing import Any, Dict


class GameOptions:
    """
    Represents game options within the replay.

    Parameters
    ----------
    advancedSharedControl : bool
        Indicates if advanced shared control is enabled.
    amm : bool
        Indicates if AutoMM (Automated Match Making) is enabled.
    battleNet : bool
        Indicates if the game was played on Battle.net.
    clientDebugFlags : int
        Specifies the client debug flag.
    competitive : bool
        Indicates whether the game was ranked or unranked.
    cooperative : bool
        Indicates if the game was cooperative.
    fog : int
        Specifies the fog value in the game.
    heroDuplicatesAllowed : bool
        Indicates if heroes can be duplicated.
    lockTeams : bool
        Indicates if teams are locked.
    noVictoryOrDefeat : bool
        Indicates if there is no victory or defeat.
    observers : int
        Specifies the count of observers watching the game.
    practice : bool
        Indicates if the game was a practice match.
    randomRaces : bool
        Indicates if random races are allowed in the game.
    teamsTogether : bool
        Indicates if teams of players are together in the game.
    userDifficulty : bool
        Indicates the user's difficulty level in the game.
    """

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "GameOptions":
        """
        Static method that initializes a GameOptions class from a provided dictionary.

        Parameters
        ----------
        d : Dict[str, Any]
            A dictionary containing information about the game, such as observer count, fog status,
            competitive mode, etc. It holds translations of phrases or sentences.

        Returns
        -------
        GameOptions
            An initialized instance of the GameOptions class based on the provided dictionary.

        Examples
        --------
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
