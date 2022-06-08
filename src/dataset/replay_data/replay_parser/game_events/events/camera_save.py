from typing import Dict

from src.dataset.replay_data.replay_parser.game_events.events.nested.target_2d import (
    Target2D,
)
from src.dataset.replay_data.replay_parser.game_events.game_event import GameEvent


class CameraSave(GameEvent):
    """
    CameraSave represents the replay information about saved camera in the game.

    :param id: Highly likely this field specifies an id of CameraSave object, many elements have the same id in
    :type id: int
    :param loop: Specifies the game loop number (game-engine tick) when at which the event occurred
    :type loop: int
    :param target: Specifies the Target class object which includes x and y coordinates, where the camera location was set in the game
    :type target: Target
    :param userid: Specifies the id of the player who saved the camera location
    :type userid: int
    :param which: Specifies a hotkey [0-9] to which camera location was set
    :type which: int
    """

    @staticmethod
    def from_dict(d: Dict) -> "CameraSave":
        """
        Static method returning initialized CameraSave class from a dictionary. This helps with the original JSON parsing.

        :param d: Specifies a dictionary as available in the JSON file that is a result of pre-processing some .SC2Replay file.
        :type d: Dict
        :return: Returns an initialized CameraSave class.
        :rtype: CameraSave
        """
        return CameraSave(
            id=d["id"],
            loop=d["loop"],
            target=Target2D(x=d["target"]["x"], y=d["target"]["y"]),
            userid=d["userid"]["userId"],
            which=d["which"],
        )

    def __init__(
        self,
        id: int,
        loop: int,
        target: Target2D,
        userid: int,
        which: int,
    ) -> None:
        self.id = id
        self.loop = loop
        self.target = target
        self.userid = userid
        self.which = which
