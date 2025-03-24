from typing import Dict

from sc2_datasets.replay_parser.game_events.game_event import GameEvent


class GameUserLeave(GameEvent):
    """
    Represents information about a player leaving the game.

    Parameters
    ----------
    id : int
        The ID of the event corresponding to its name.
    leaveReason : int
        A number determining the reason for leaving (details unspecified).
    loop : int
        The game loop number (game-engine tick) when the event occurred.
    userid : int
        The ID number of the player who left the game.
    """

    @staticmethod
    def from_dict(d: Dict) -> "GameUserLeave":
        """
        Static method returning initialized GameUserLeave class from a dictionary.

        Parameters
        ----------
        d : Dict
            Specifies a dictionary as available in the JSON file
            that is a result of pre-processing some .SC2Replay file.

        Returns
        -------
        GameUserLeave
            Returns an initialized GameUserLeave class.
        """
        return GameUserLeave(
            id=d["id"],
            leaveReason=d["leaveReason"],
            loop=d["loop"],
            userid=d["userid"]["userId"],
        )

    def __init__(
        self,
        id: int,
        leaveReason: int,
        loop: int,
        userid: int,
    ) -> None:
        self.id = id
        self.leaveReason = leaveReason
        self.loop = loop
        self.userid = userid
