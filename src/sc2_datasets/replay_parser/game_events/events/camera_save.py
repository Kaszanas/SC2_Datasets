from typing import Dict

from sc2_datasets.replay_parser.game_events.events.nested.target_2d import Target2D
from sc2_datasets.replay_parser.game_events.game_event import GameEvent


class CameraSave(GameEvent):
    """
    CameraSave represents replay information regarding a saved camera location within the game.

    Parameters
    ----------
    id : int
        Identifier for the CameraSave object. Multiple elements may share the same ID.
    loop : int
        Game loop number (game-engine tick) when the event occurred.
    target : Target
        Target class object containing x and y coordinates where the camera location was set in the game.
    userid : int
        ID of the player who saved the camera location.
    which : int
        Hotkey [0-9] to which the camera location was set.
    """

    # REVIEW: Doctests here:
    @staticmethod
    def from_dict(d: Dict) -> "CameraSave":
        """
        Static method returning an initialized CameraSave class from a dictionary.
        Helps with the original JSON parsing.

        Parameters
        ----------
        d : Dict
            Dictionary from the pre-processed .SC2Replay file in JSON format.

        Returns
        -------
        CameraSave
            Initialized CameraSave class object.


        Examples
        --------
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
