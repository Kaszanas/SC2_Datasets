from typing import Dict

# pylama:ignore=E501
from sc2_datasets.replay_parser.tracker_events.tracker_event import TrackerEvent
from sc2_datasets.replay_parser.tracker_events.events.player_stats.stats import Stats


class PlayerStats(TrackerEvent):
    """
    PlayerStats holds information about player economy

    :param id: Specifies the ID of an event which corresponds to its name.
    :type id: int
    :param loop: Specifies the time at which the event happened in gameloops.
    :type loop: int
    :param playerId: Specifies the id of a player to which this event pertains.
    :type playerId: int
    :param stats: Specifies a custom data type holding the statistics.
    :type stats: Stats
    """

    @staticmethod
    def from_dict(d: Dict) -> "PlayerStats":
        """
        Static method returning initialized PlayerStats class from a dictionary.
        This helps with the original JSON parsing.

        :param d: Specifies a dictionary as available in the JSON file that\
        is a result of pre-processing some .SC2Replay file.
        :type d: Dict
        :return: Returns an initialized PlayerStats class.
        :rtype: PlayerStats
        """
        return PlayerStats(
            id=d["id"],
            loop=d["loop"],
            playerId=d["playerId"],
            stats=Stats.from_dict(d=d["stats"]),
        )

    def __init__(
        self,
        id: int,
        loop: int,
        playerId: int,
        stats: Stats,
    ) -> None:
        self.id = id
        self.loop = loop
        self.playerId = playerId
        self.stats = stats
