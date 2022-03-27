from typing import Dict
from src.dataset.replay_structures.tracker_events.player_stats.stats import Stats


class PlayerStats:
    def __init__(self, id: int, loop: int, playerId: int, stats: Stats) -> None:
        self.id = id
        self.loop = loop
        self.playerId = playerId
        self.stats = stats
