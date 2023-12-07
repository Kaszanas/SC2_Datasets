from typing import Dict

from sc2_datasets.replay_parser.game_events.game_event import GameEvent
from sc2_datasets.replay_parser.game_events.events.nested.delta import Delta


class SelectionDelta(GameEvent):
    """
    SelectionDelta contains details about a player's selection during the game.

    Parameters
    ----------
    controlGroupId : int
        Specifies the event ID of the control group that was selected.
    delta : Delta
        Specifies the game loop number (game-engine tick) at which the event occurred.
    id : int
        Specifies the ID of an event corresponding to its name.
    loop : int
        Specifies the game loop number (game-engine tick) at which the event occurred.
    userid : int
        Specifies the ID number of the player who executed the selection option in the game.
    """

    @staticmethod
    def from_dict(d: Dict) -> "SelectionDelta":
        """
        Initializes a SelectionDelta class from a dictionary, aiding the original JSON parsing.

        Parameters
        ----------
        d : Dict
            A dictionary obtained from pre-processing an .SC2Replay file in JSON format.

        Returns
        -------
        SelectionDelta
            An initialized instance of the SelectionDelta class.
        """
        return SelectionDelta(
            controlGroupId=d["controlGroupId"],
            delta=Delta.from_dict(d=d["delta"]),
            id=d["id"],
            loop=d["loop"],
            userid=d["userid"]["userId"],
        )

    def __init__(
        self,
        controlGroupId: int,
        delta: Delta,
        id: int,
        loop: int,
        userid: int,
    ) -> None:
        self.controlGroupId = controlGroupId
        self.delta = delta
        self.id = id
        self.loop = loop
        self.userid = userid
