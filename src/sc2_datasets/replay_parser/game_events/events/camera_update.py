from types import NoneType
from typing import Dict

from sc2_datasets.replay_parser.game_events.game_event import GameEvent
from sc2_datasets.replay_parser.game_events.events.nested.target_2d import Target2D


class CameraUpdate(GameEvent):
    """
    CameraUpdate represents the replay information
    about updated camera location in the game.

    :param distance: There is no valuable information about this parameter
    :type distance: NoneType | float | int
    :param follow: There is no valuable information about this parameter
    :type follow: bool
    :param id: There is no valuable information about this parameter
    :type id: int
    :param loop: Specifies the game loop number (game-engine tick)
    at which the event occurred
    :type loop: int
    :param pitch: Specifies angle in the vertical plane,
    vertical elevation of the camera.
    :type pitch: NoneType | float | int
    :param reason: There is no valuable information about this parameter
    :type reason: NoneType | str
    :param target: Specifies the Target class object which includes x and y coordinates,
    where the camera location was set
    :type target: Target
    :param userid: Specifies the id of the player who saved the camera location
    :type userid: int
    :param yaw: Specifies the angle in the horizontal plane of the camera
    :type yaw: NoneType | float | int
    """

    # REVIEW: Doctests here:
    @staticmethod
    def from_dict(d: Dict):
        """
        Static method returning initialized CameraUpdate class from a dictionary.
        This helps with the original JSON parsing.

        :param d: Specifies a dictionary as available in the JSON file\
        that is a result of pre-processing some .SC2Replay file.
        :type d: Dict
        :return: Returns an initialized CameraUpdate class.
        :rtype: CameraUpdate

        **Correct Usage Examples:**

        Using from_dict factory method provides ease of use when parsing
        a replay pre-processed with SC2InfoExtractorGo_.
        This method requires a dictionary representation
        of data to be passed as a parameter because
        of the built-in json parser provided by the Python standard library.

        .. _SC2InfoExtractorGo: https://github.com/Kaszanas/SC2InfoExtractorGo

        >>> from sc2egset_dataset.dataset.replay_data.replay_parser.game_events.events.nested.target_2d import Target2D  #noqa
        >>> camera_update_dict = {"distance": None,
        ...                       "follow": False,
        ...                       "id": 49,
        ...                       "loop": 136,
        ...                       "pitch": None,
        ...                       "reason": None,
        ...                       "target": {
        ...                           "x": 1.002,
        ...                           "y": 4.148},
        ...                       "userid": {"userId": 1},
        ...                       "yaw": None}
        >>> camera_update_object = CameraUpdate.from_dict(d=camera_update_dict)
        >>> assert isinstance(camera_update_object, CameraUpdate)
        >>> assert camera_update_object.distance == None
        >>> assert camera_update_object.follow == False
        >>> assert camera_update_object.id == 49
        >>> assert camera_update_object.loop == 136
        >>> assert camera_update_object.pitch == None
        >>> assert camera_update_object.reason == None
        >>> assert camera_update_object.target.x == 1.002
        >>> assert camera_update_object.target.y == 4.148
        >>> assert camera_update_object.userid == 1
        >>> assert camera_update_object.yaw == None
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
