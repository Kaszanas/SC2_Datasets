class Metadata:
    """_summary_

    :param base_build: _description_
    :type base_build: str
    :param data_build: _description_
    :type data_build: str
    :param duration_seconds: _description_
    :type duration_seconds: int
    :param game_version: _description_
    :type game_version: str
    :param map_name: _description_
    :type map_name: str
    """

    def __init__(
        self,
        base_build: str,
        data_build: str,
        duration_seconds: int,
        game_version: str,
        map_name: str,
    ) -> None:
        self.baseBuild = base_build
        self.dataBuild = data_build
        self.durationSeconds = duration_seconds
        self.gameVersion = game_version
        self.mapName = map_name

    @property
    def base_build(self):
        return self.base_build

    @property
    def baseBuild(self):
        return self.baseBuild

    @property
    def data_build(self):
        return self.data_build

    @property
    def dataBuild(self):
        return self.dataBuild

    @property
    def duration_seconds(self):
        return self.duration_seconds

    @property
    def durationSeconds(self):
        return self.durationSeconds

    @property
    def game_version(self):
        return self.game_version

    @property
    def gameVersion(self):
        return self.gameVersion

    @property
    def map_name(self):
        return self.map_name

    @property
    def mapName(self):
        return self.mapName
