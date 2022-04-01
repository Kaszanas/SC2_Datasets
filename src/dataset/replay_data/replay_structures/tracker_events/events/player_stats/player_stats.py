from typing import Dict
from src.dataset.replay_structures.tracker_events.events.player_stats.stats import Stats
from src.dataset.replay_structures.tracker_events.tracker_event import TrackerEvent

# TODO: Document the docstrings


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
        _summary_

        :param d: _description_
        :type d: Dict
        :return: _description_
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
