from typing import Dict

from sc2_datasets.replay_parser.game_events.game_event import GameEvent
from sc2_datasets.replay_parser.game_events.events.nested.target_2d import Target2D


class CameraSave(GameEvent):
    """
    CameraSave represents the replay information about saved camera in the game.

    :param id: Highly likely this field specifies an id of CameraSave object,\
    many elements have the same id in
    :type id: int
    :param loop: Specifies the game loop number (game-engine tick)\
    at which the event occurred
    :type loop: int
    :param target: Specifies the Target class object which includes x and y coordinates,\
    where the camera location was set in the game
    :type target: Target
    :param userid: Specifies the id of the player who saved the camera location
    :type userid: int
    :param which: Specifies a hotkey [0-9] to which camera location was set
    :type which: int
    """

    # REVIEW: Doctests here:
    @staticmethod
    def from_dict(d: Dict) -> "CameraSave":
        """
        Static method returning initialized CameraSave class from a dictionary.
        This helps with the original JSON parsing.

        :param d: Specifies a dictionary as available in the JSON file\
        that is a result of pre-processing some .SC2Replay file.
        :type d: Dict
        :return: Returns an initialized CameraSave class.
        :rtype: CameraSave


        **Correct Usage Examples:**

        Using from_dict factory method provides ease of use when parsing
        a replay pre-processed with SC2InfoExtractorGo_.

        This method requires a dictionary representation
        of data to be passed as a parameter because of the built in json
        parser provided by the Python standard library.

        .. _SC2InfoExtractorGo: https://github.com/Kaszanas/SC2InfoExtractorGo

        >>> from sc2egset_dataset.dataset.replay_data.replay_parser.game_events.events.nested.target_2d import Target2D  #noqa
        >>> camera_save_dict = {"id": 5,
        ...                     "loop": 22,
        ...                     "target": {
        ...                        "x": 3.578125,
        ...                        "y": 0.742431640625},
        ...                     "userid": {
        ...                        "userId": 0},
        ...                     "which": 0}
        >>> camera_save_object = CameraSave.from_dict(d=camera_save_dict)
        >>> assert isinstance(camera_save_object, CameraSave)
        >>> assert camera_save_object.id == 5
        >>> assert camera_save_object.loop == 22
        >>> assert isinstance(camera_save_object.target, Target2D)
        >>> assert camera_save_object.target.x == 3.578125
        >>> assert camera_save_object.target.y == 0.742431640625
        >>> assert camera_save_object.userid == 0
        >>> assert camera_save_object.loop == 22
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
