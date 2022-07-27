from typing import Dict

from sc2_datasets.replay_parser.game_events.game_event import GameEvent


class ControlGroupUpdate(GameEvent):
    """
    ControlGroupUpdate is containing some "details" information about
    updates and changes player's control groups in the game.

    :param controlGroupIndex: Highly likely this parameter specifies\
    an id parameter which control group has selected by the player in the game
    :type controlGroupIndex: int
    :param controlGroupUpdate: Highly likely this parameter specifies\
    an id parameter which control group has changed by the player in the game
    :type controlGroupUpdate: int
    :param id: Specifies the ID of an event which corresponds to its name.
    :type id: int
    :param loop: Specifies the game loop number (game-engine tick)\
    at which the event occurred
    :type loop: int
    :param userid: Specifies id number of player who has updated the group control the game
    :type userid: int
    """

    @staticmethod
    def from_dict(d: Dict) -> "ControlGroupUpdate":
        """
        Static method returning initialized ControlGroupUpdate class from a dictionary.
        This helps with the original JSON parsing.

        :param d: Specifies a dictionary as available in the JSON file\
        that is a result of pre-processing some .SC2Replay file.
        :type d: Dict
        :return: Returns an initialized ControlGroupUpdate class.
        :rtype: ControlGroupUpdate
        """
        return ControlGroupUpdate(
            controlGroupIndex=d["controlGroupIndex"],
            controlGroupUpdate=d["controlGroupUpdate"],
            id=d["id"],
            loop=d["loop"],
            userid=d["userid"]["userId"],
        )

    def __init__(
        self,
        controlGroupIndex: int,
        controlGroupUpdate: int,
        id: int,
        loop: int,
        userid: int,
    ) -> None:
        self.controlGroupIndex = controlGroupIndex
        self.controlGroupUpdate = controlGroupUpdate
        self.id = id
        self.loop = loop
        self.userid = userid
