from typing import Dict
from src.dataset.replay_structures.tracker_events.events.player_setup import PlayerSetup
from src.dataset.replay_structures.tracker_events.events.player_stats.player_stats import (
    PlayerStats,
)
from src.dataset.replay_structures.tracker_events.events.unit_born import UnitBorn
from src.dataset.replay_structures.tracker_events.events.unit_died import UnitDied
from src.dataset.replay_structures.tracker_events.events.unit_done import UnitDone
from src.dataset.replay_structures.tracker_events.events.unit_init import UnitInit
from src.dataset.replay_structures.tracker_events.events.unit_owner_change import (
    UnitOwnerChange,
)
from src.dataset.replay_structures.tracker_events.events.unit_positions import (
    UnitPositions,
)
from src.dataset.replay_structures.tracker_events.events.unit_type_change import (
    UnitTypeChange,
)
from src.dataset.replay_structures.tracker_events.events.upgrade import Upgrade
from src.dataset.replay_structures.tracker_events.tracker_event import TrackerEvent

# TODO: from_dict documentation


class TrackerEventsParser:
    @staticmethod
    def from_dict(d: Dict) -> TrackerEvent:
        """
        _summary_

        :param d: _description_
        :type d: Dict
        :return: _description_
        :rtype: TrackerEvent
        """
        type_name = d["evtTypeName"]

        match type_name:
            case PlayerStats.__name__:
                return PlayerStats.from_dict(d=d)
            case PlayerSetup.__name__:
                return PlayerSetup.from_dict(d=d)
            case UnitBorn.__name__:
                return UnitBorn.from_dict(d=d)
            case UnitDied.__name__:
                return UnitDied.from_dict(d=d)
            case UnitDone.__name__:
                return UnitDone.from_dict(d=d)
            case UnitInit.__name__:
                return UnitInit.from_dict(d=d)
            case UnitOwnerChange.__name__:
                return UnitOwnerChange.from_dict(d=d)
            case UnitPositions.__name__:
                return UnitPositions.from_dict(d=d)
            case UnitTypeChange.__name__:
                return UnitTypeChange.from_dict(d=d)
            case Upgrade.__name__:
                return Upgrade.from_dict(d=d)
