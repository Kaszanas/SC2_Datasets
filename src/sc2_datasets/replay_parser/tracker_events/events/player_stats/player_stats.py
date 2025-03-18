from typing import Dict

from sc2_datasets.replay_parser.tracker_events.events.player_stats.stats import Stats

# pylama:ignore=E501
from sc2_datasets.replay_parser.tracker_events.tracker_event import TrackerEvent


class PlayerStats(TrackerEvent):
    """
    PlayerStats holds information about player economy

    Parameters
    ----------
    id : int
        Specifies the ID of an event which corresponds to its name.
    loop : int
        Specifies the time at which the event happened in gameloops.
    playerId : int
        Specifies the id of a player to which this event pertains.
    stats : Stats
        Specifies a custom data type holding the statistics.
    """

    @staticmethod
    def from_dict(d: Dict) -> "PlayerStats":
        """
        Static method returning initialized PlayerStats class from a dictionary.
        This helps with the original JSON parsing.

        Parameters
        ----------
        d : Dict
            Specifies a dictionary as available in the JSON file that
            is a result of pre-processing some .SC2Replay file.

        Returns
        -------
        PlayerStats
            Returns an initialized PlayerStats class.
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
