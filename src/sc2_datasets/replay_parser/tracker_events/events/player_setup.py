from typing import Dict

from sc2_datasets.replay_parser.tracker_events.tracker_event import TrackerEvent


class PlayerSetup(TrackerEvent):

    """
    Data type that denotes a player setup event which is available in tracker events.
    It contains basic information mapping userId to playerId to slotId.

    Parameters
    ----------
    id : int
        Highly likely this field specifies an id of the PlayerSetup object.
    loop : int
        Specifies the time (in gameloop units) at which the event happened.
    playerId : int
        Specifies an id of the player in the game, in 1v1 game [1,2].
    slotId : int
        Specifies an id of the starting location.
    type : int
        There is no valuable information about this parameter.
    userId : int
        Specifies the setup user id for the player.
    """

    @staticmethod
    def from_dict(d: Dict) -> "PlayerSetup":
        """
        Static method returning initialized PlayerSetup class from a dictionary.
        This helps with the original JSON parsing.

        Parameters
        ----------
        d : Dict
            Specifies a dictionary as available in the JSON file
            that is a result of pre-processing some .SC2Replay file.

        Returns
        -------
        PlayerSetup
            Returns an initialized PlayerSetup class.
        """
        return PlayerSetup(
            id=d["id"],
            loop=d["loop"],
            playerId=d["playerId"],
            slotId=d["slotId"],
            type=d["type"],
            userId=d["userId"],
        )

    def __init__(
        self,
        id: int,
        loop: int,
        playerId: int,
        slotId: int,
        type: int,
        userId: int,
    ) -> None:
        self.id = id
        self.loop = loop
        self.playerId = playerId
        self.slotId = slotId
        self.type = type
        self.userId = userId
