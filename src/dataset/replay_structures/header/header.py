class Header:
    """
    Header represents the replay header.

    :param elapsed_game_loops: Specifies how much game loops (game-engine ticks) the game lasted.
    :type elapsed_game_loops: int
    :param duration_nanoseconds: Specifies how much nanoseconds the game lasted.
    :type duration_nanoseconds: int
    :param duration_seconds: Specifies how much seconds the game lasted.
    :type duration_seconds: int
    :param version: Specifies the game version that was used to play the game.
    :type version: str
    """

    def __init__(
        self,
        elapsed_game_loops: int,
        duration_nanoseconds: int,
        duration_seconds: int,
        version: str,
    ) -> None:
        self.elapsed_game_loops = elapsed_game_loops
        self.duration_nanoseconds = duration_nanoseconds
        self.duration_seconds = duration_seconds
        self.version = version

    @property
    def elapsed_game_loops(self):
        return self.elapsed_game_loops

    @property
    def elapsedGameLoops(self):
        return self.elapsed_game_loops

    @property
    def duration_nanoseconds(self):
        return self.duration_nanoseconds

    @property
    def durationNanoseconds(self):
        return self.duration_nanoseconds

    @property
    def duration_seconds(self):
        return self.duration_seconds

    @property
    def durationSeconds(self):
        return self.duration_seconds

    @property
    def version(self):
        return self.version
