from typing import Dict

from sc2_datasets.replay_parser.tracker_events.tracker_event import TrackerEvent


class Upgrade(TrackerEvent):

    """
    Upgrade type containing some "details" information
    on which player is doing an upgrade, game loop, upgrade in game name etc.

    :param count: Specifies a number, highly likely this parameter serves\
    for adding value of upgrades to summary. Default value of the parameter is 1.
    :type count: int
    :param id: Specifies an event unique number
    :type id: int
    :param loop: Specifies a game loop when the upgrade was started in the game
    :type loop: int
    :param playerId: Specifies an id of the player who was doing the upgrade in the game
    :type playerId: int
    :param upgradeTypeName: Specifies a name that upgrade has in the game
    :type upgradeTypeName: str
    """

    @staticmethod
    def from_dict(d: Dict) -> "Upgrade":
        """
        Static method returning initialized Upgrade class from a dictionary.
        This helps with the original JSON parsing.

        :param d: Specifies a dictionary as available in the JSON file that\
        is a result of pre-processing some .SC2Replay file.
        :type d: Dict
        :return: Returns an initialized Upgrade class.
        :rtype: Upgrade
        """
        return Upgrade(
            count=d["count"],
            id=d["id"],
            loop=d["loop"],
            playerId=d["playerId"],
            upgradeTypeName=d["upgradeTypeName"],
        )

    def __init__(
        self,
        count: int,
        id: int,
        loop: int,
        playerId: int,
        upgradeTypeName: str,
    ) -> None:

        self.count = count
        self.id = id
        self.loop = loop
        self.playerId = playerId
        self.upgradeTypeName = upgradeTypeName
