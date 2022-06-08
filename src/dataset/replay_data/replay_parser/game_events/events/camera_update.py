from types import NoneType
from typing import Dict

from src.dataset.replay_data.replay_parser.game_events.events.nested.target_2d import (
    Target2D,
)
from src.dataset.replay_data.replay_parser.game_events.game_event import GameEvent


# TODO: There are some null values in the data
# it needs to be verified if such null values are a problem for later calculations with the dataset?
# Should this be encoded somehow?
# TODO: Document the docstrings
class CameraUpdate(GameEvent):
    """
    CameraUpdate represents the replay information about updated camera location in the game.

    :param distance: There is no valuable information about this parameter
    :type distance: NoneType | float | int
    :param follow: There is no valuable information about this parameter
    :type follow: bool
    :param id: There is no valuable information about this parameter
    :type id: int
    :param loop: There is no valuable information about this parameter
    :type loop: int
    :param pitch: Specifies angle in the vertical plane, vertical elevation of the camera.
    :type pitch: NoneType | float | int
    :param reason: There is no valuable information about this parameter
    :type reason: NoneType | str
    :param target: Specifies the Target class object which includes x and y coordinates, where the camera location was set
    :type target: Target
    :param userid: Specifies the id of the player who saved the camera location
    :type userid: int
    :param yaw: Specifies the angle in the horizontal plane of the camera
    :type yaw: NoneType | float | int
    """

    @staticmethod
    def from_dict(d: Dict):
        """
        Static method returning initialized CameraUpdate class from a dictionary. This helps with the original JSON parsing.

        :param d: Specifies a dictionary as available in the JSON file that is a result of pre-processing some .SC2Replay file.
        :type d: Dict
        :return: Returns an initialized CameraUpdate class.
        :rtype: CameraUpdate
        """
        return CameraUpdate(
            distance=d["distance"],
            follow=d["follow"],
            id=d["id"],
            loop=d["loop"],
            pitch=d["pitch"],
            reason=d["reason"],
            target=Target2D(x=d["target"]["x"], y=d["target"]["y"]),
            userid=d["userid"]["userId"],
            yaw=d["yaw"],
        )

    def __init__(
        self,
        distance: NoneType | float | int,
        follow: bool,
        id: int,
        loop: int,
        pitch: NoneType | float | int,
        reason: NoneType | str,
        target: Target2D,
        userid: int,
        yaw: NoneType | float | int,
    ) -> None:
        self.distance = distance
        self.follow = follow
        self.id = id
        self.loop = loop
        self.pitch = pitch
        self.reason = reason
        self.target = target
        self.userid = userid
        self.yaw = yaw
