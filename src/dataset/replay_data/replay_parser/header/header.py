from typing import Any, Dict

from src.dataset.replay_data.replay_parser.replay_field import SC2ReplayField


class Header(SC2ReplayField):
    """
    Header represents the replay header.

    :param elapsedGameLoops: Specifies how much game loops (game-engine ticks) the game lasted.
    :type elapsedGameLoops: int
    :param durationNanoseconds: Specifies how much nanoseconds the game lasted.
    :type durationNanoseconds: int
    :param durationSeconds: Specifies how much seconds the game lasted.
    :type durationSeconds: int
    :param version: Specifies the game version that was used to play the game.
    :type version: str
    """

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Header":
        return Header(
            elapsedGameLoops=d["elapsedGameLoops"],
            durationNanoseconds=d["durationNanoseconds"],
            durationSeconds=d["durationSeconds"],
            version=d["version"],
        )

    def __init__(
        self,
        elapsedGameLoops: int,
        durationNanoseconds: int,
        durationSeconds: int,
        version: str,
    ) -> None:
        self.elapsedGameLoops = elapsedGameLoops
        self.durationNanoseconds = durationNanoseconds
        self.durationSeconds = durationSeconds
        self.version = version

    def to_tensor(self):
        pass
