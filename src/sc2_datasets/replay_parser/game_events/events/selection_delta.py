from typing import Dict

from sc2_datasets.replay_parser.game_events.game_event import GameEvent
from sc2_datasets.replay_parser.game_events.events.nested.delta import Delta


class SelectionDelta(GameEvent):
    """
    SelectionDelta is containing some "details" information
    about player's selection during the game

    :param controlGroupId: Specifies the event id of the control group,\
    which has been selected
    :type controlGroupId: int
    :param delta: Specifies the game loop number (game-engine tick)\
    at which the event occurred
    :type delta: Delta
    :param id: Specifies the ID of an event which corresponds to its name.
    :type id: int
    :param loop: Specifies the game loop number (game-engine tick)\
    at which the event occurred
    :type loop: int
    :param userid: Specifies id number of player who has done selection option in the game
    :type userid: int
    """

    @staticmethod
    def from_dict(d: Dict) -> "SelectionDelta":
        """
        Static method returning initialized SelectionDelta class from a dictionary.
        This helps with the original JSON parsing.

        :param d: Specifies a dictionary as available in the JSON file that\
        is a result of pre-processing some .SC2Replay file.
        :type d: Dict
        :return: Returns an initialized SelectionDelta class.
        :rtype: SelectionDelta
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
