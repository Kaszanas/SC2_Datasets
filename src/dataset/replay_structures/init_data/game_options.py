class GameOptions:

    """_summary_

    :param advancedSharedControl: _description_
    :type advancedSharedControl: bool
    :param amm: _description_
    :type amm: bool
    :param battleNet: _description_
    :type battleNet: bool
    :param clientDebugFlags: _description_
    :type clientDebugFlags: int
    :param competitive: _description_
    :type competitive: bool
    :param cooperative: _description_
    :type cooperative: bool
    :param fog: _description_
    :type fog: int
    :param heroDuplicatesAllowed: _description_
    :type heroDuplicatesAllowed: bool
    :param lockTeams: _description_
    :type lockTeams: bool
    :param noVictoryOrDefeat: _description_
    :type noVictoryOrDefeat: bool
    :param observers: _description_
    :type observers: int
    :param practice: _description_
    :type practice: bool
    :param randomRaces: _description_
    :type randomRaces: bool
    :param teamsTogether: _description_
    :type teamsTogether: bool
    :param userDifficulty: _description_
    :type userDifficulty: bool
    """

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
