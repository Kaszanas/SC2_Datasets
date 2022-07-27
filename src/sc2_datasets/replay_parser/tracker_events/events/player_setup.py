from typing import Dict

from sc2_datasets.replay_parser.tracker_events.tracker_event import TrackerEvent


class PlayerSetup(TrackerEvent):

    """
    Data type that denotes a player setup event which is available in tracker events.
    It contains basic information mapping userId to playerId to slotId.

    :param id: Highly likely this field specifies an id of the PlayerSetup object
    :type id: int
    :param loop: Specifies the time (in gameloop units) at which the event happened.
    :type loop: int
    :param playerId: Specifies an id of the player in the game, in 1v1 game [1,2]
    :type playerId: int
    :param slotId: Specifies an id of the starting location;
    :type slotId: int
    :param type: There is no valuable information about this parameter
    :type type: int
    :param userId: Specifies the setup user id for the player
    :type userId: int
    """

    @staticmethod
    def from_dict(d: Dict) -> "PlayerSetup":
        """
        Static method returning initialized PlayerSetup class from a dictionary.
        This helps with the original JSON parsing.

        :param d: Specifies a dictionary as available in the JSON file\
        that is a result of pre-processing some .SC2Replay file.
        :type d: Dict
        :return: Returns an initialized PlayerSetup class.
        :rtype: PlayerSetup
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
