class Details:
    """_summary_

    :param game_speed: _description_
    :type game_speed: str
    :param is_blizzard_map: _description_
    :type is_blizzard_map: bool
    :param time_utc: _description_
    :type time_utc: str
    """

    def __init__(self, game_speed: str, is_blizzard_map: bool, time_utc: str) -> None:
        self.game_speed = game_speed
        self.is_blizzard_map = is_blizzard_map
        self.time_utc = time_utc

    @property
    def game_speed(self):
        return self.game_speed

    @property
    def gameSpeed(self):
        return self.game_speed

    @property
    def is_blizzard_map(self):
        return self.is_blizzard_map

    @property
    def isBlizzardMap(self):
        return self.is_blizzard_map

    @property
    def time_utc(self):
        return self.time_utc

    @property
    def timeUTC(self):
        return self.time_utc
