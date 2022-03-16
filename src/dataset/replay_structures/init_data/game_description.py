from dataset.replay_structures.init_data.game_options import GameOptions


class GameDescription:
    """_summary_

    :param game_options: _description_
    :type game_options: GameOptions
    :param game_speed: _description_
    :type game_speed: str
    :param is_blizzard_map: _description_
    :type is_blizzard_map: bool
    :param map_author_name: _description_
    :type map_author_name: str
    :param map_file_sync_checksum: _description_
    :type map_file_sync_checksum: int
    :param map_size_x: _description_
    :type map_size_x: int
    :param map_size_y: _description_
    :type map_size_y: int
    :param max_players: _description_
    :type max_players: int
    """

    def __init__(
        self,
        game_options: GameOptions,
        game_speed: str,
        is_blizzard_map: bool,
        map_author_name: str,
        map_file_sync_checksum: int,
        map_size_x: int,
        map_size_y: int,
        max_players: int,
    ) -> None:

        self.game_options = game_options
        self.game_speed = game_speed
        self.is_blizzard_map = is_blizzard_map
        self.map_author_name = map_author_name
        self.map_file_sync_checksum = map_file_sync_checksum
        self.map_size_x = map_size_x
        self.map_size_y = map_size_y
        self.max_players = max_players

    @property
    def game_options(self):
        return self.game_options

    @property
    def gameOptions(self):
        return self.game_options

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
    def map_author_name(self):
        return self.map_author_name

    @property
    def mapAuthorName(self):
        return self.map_author_name

    @property
    def map_file_sync_checksum(self):
        return self.map_file_sync_checksum

    @property
    def mapFileSyncChecksum(self):
        return self.map_file_sync_checksum

    @property
    def map_size_x(self):
        return self.map_size_x

    @property
    def mapSizeX(self):
        return self.map_size_x

    @property
    def map_size_y(self):
        return self.map_size_y

    @property
    def mapSizeY(self):
        return self.map_size_y

    @property
    def max_players(self):
        return self.max_players

    @property
    def maxPlayers(self):
        return self.max_players
