from typing import Any, Dict


class GameOptions:
    """
    _summary_

    :param advancedSharedControl: Specifies if advanced shared control is enabled
    :type advancedSharedControl: bool
    :param amm: Specifies if AMM (AutoMM - Automated Match Making) is enabled
    :type amm: bool
    :param battleNet: Specifies if game was played on Battle.net
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
        _summary_

        :param d: Describes a dictionary, it holds translations of a phrase or sentence
        :type d: Dict[str, Any]
        :return: Specifies a list of parameters about the game like a number of observers, fog of the game, if game was
                 competitive etc.
        :rtype: GameOptions
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
