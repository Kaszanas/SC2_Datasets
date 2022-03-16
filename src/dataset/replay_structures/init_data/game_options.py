class GameOptions:

    """_summary_

    :param advanced_shared_control: _description_
    :type advanced_shared_control: bool
    :param auto_matchmaking: _description_
    :type auto_matchmaking: bool
    :param battle_net: _description_
    :type battle_net: bool
    :param build_coach_enabled: _description_
    :type build_coach_enabled: bool
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
    :type userDifficulty: int
    """

    def __init__(
        self,
        advanced_shared_control: bool,
        auto_matchmaking: bool,
        battle_net: bool,
        build_coach_enabled: bool,
        client_debug_flags: int,
        competitive: bool,
        cooperative: bool,
        fog: int,
        hero_duplicates_allowed: bool,
        lock_teams: bool,
        no_victory_or_defeat: bool,
        observers: int,
        practice: bool,
        random_races: bool,
        teams_together: bool,
        user_difficulty: int,
    ) -> None:
        self.advanced_shared_control = advanced_shared_control
        self.auto_matchmaking = auto_matchmaking
        self.battle_net = battle_net
        self.build_coach_enabled = build_coach_enabled
        self.client_debug_flags = client_debug_flags
        self.competitive = competitive
        self.cooperative = cooperative
        self.fog = fog
        self.hero_duplicates_allowed = hero_duplicates_allowed
        self.lock_teams = lock_teams
        self.no_victory_or_defeat = no_victory_or_defeat
        self.observers = observers
        self.practice = practice
        self.random_races = random_races
        self.teams_together = teams_together
        self.user_difficulty = user_difficulty

    @property
    def advanced_shared_control(self):
        return self.advanced_shared_control

    @property
    def advancedSharedControl(self):
        return self.advanced_shared_control

    @property
    def auto_matchmaking(self):
        return self.auto_matchmaking

    @property
    def autoMatchmaking(self):
        return self.auto_matchmaking

    @property
    def battle_net(self):
        return self.battle_net

    @property
    def battleNet(self):
        return self.battle_net

    @property
    def build_coach_enabled(self):
        return self.build_coach_enabled

    @property
    def buildCoachEnabled(self):
        return self.build_coach_enabled

    @property
    def client_debug_flags(self):
        return self.client_debug_flags

    @property
    def clientDebugFlags(self):
        return self.client_debug_flags

    @property
    def competitive(self):
        return self.competitive

    @property
    def cooperative(self):
        return self.cooperative

    @property
    def fog(self):
        return self.fog

    @property
    def hero_duplicates_allowed(self):
        return self.hero_duplicates_allowed

    @property
    def heroDuplicatesAllowed(self):
        return self.hero_duplicates_allowed

    @property
    def lock_teams(self):
        return self.lock_teams

    @property
    def lockTeams(self):
        return self.lock_teams

    @property
    def no_victory_or_defeat(self):
        return self.no_victory_or_defeat

    @property
    def noVictoryOrDefeat(self):
        return self.no_victory_or_defeat

    @property
    def observers(self):
        return self.observers

    @property
    def practice(self):
        return self.practice

    @property
    def random_races(self):
        return self.random_races

    @property
    def randomRaces(self):
        return self.random_races

    @property
    def teams_together(self):
        return self.teams_together

    @property
    def teamsTogether(self):
        return self.teams_together

    @property
    def user_difficulty(self):
        return self.user_difficulty

    @property
    def userDifficulty(self):
        return self.user_difficulty
