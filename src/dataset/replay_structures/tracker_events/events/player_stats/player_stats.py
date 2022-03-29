from typing import Dict
from src.dataset.replay_structures.tracker_events.player_stats.stats import Stats


class PlayerStats:
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

    def __init__(self, id: int, loop: int, playerId: int, stats: Stats) -> None:
        self.id = id
        self.loop = loop
        self.playerId = playerId
        self.stats = stats
