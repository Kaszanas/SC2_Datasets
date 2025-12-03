from dataclasses import dataclass

from sc2_datasets.replay_parser.tracker_events.events.player_stats.stats import Stats

# pylama:ignore=E501
from sc2_datasets.replay_parser.tracker_events.tracker_event import TrackerEvent


@dataclass
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

    id: int
    loop: int
    playerId: int
    stats: Stats

    @staticmethod
    def from_dict(d: dict) -> "PlayerStats":
        """
        Static method returning initialized PlayerStats class from a dictionary.
        This helps with the original JSON parsing.

        Parameters
        ----------
        d : dict
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
