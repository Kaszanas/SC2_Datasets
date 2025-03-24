from typing import Dict

from sc2_datasets.replay_parser.game_events.game_event import GameEvent


class CommandManagerState(GameEvent):
    """
    CommandManagerState type contains information about some states during the game, like time, player, etc.

    Parameters
    ----------
    id : int
        Specifies the ID of an event corresponding to its name.
    loop : int
        Specifies the game loop number (game-engine tick) at which the event occurred.
    sequence : int
        Highly likely specifies an ID parameter indicating the sequence made by the player.
    state : int
        Highly likely specifies an ID parameter indicating the state made by the player.
    userid : int
        Specifies the ID number of the player who managed the state. For example, in a 1v1 game: [0,1].
    """

    @staticmethod
    def from_dict(d: Dict) -> "CommandManagerState":
        """
        Static method returning initialized CommandManagerState class from a dictionary.
        This helps with the original JSON parsing.

        Parameters
        ----------
        d : Dict
            Specifies a dictionary as available in the JSON file that\
            is a result of pre-processing some .SC2Replay file.

        Returns
        -------
        CommandManagerState
            An initialized CommandManagerState class.

        """
        return CommandManagerState(
            id=d["id"],
            loop=d["loop"],
            sequence=d["sequence"],
            state=d["state"],
            userid=d["userid"]["userId"],
        )

    def __init__(
        self,
        id: int,
        loop: int,
        sequence: int,
        state: int,
        userid: int,
    ) -> None:
        self.id = id
        self.loop = loop
        self.sequence = sequence
        self.state = state
        self.userid = userid
