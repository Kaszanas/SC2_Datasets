from dataclasses import dataclass

from sc2_datasets.replay_parser.game_events.events.nested.target_3d import Target3D


@dataclass
class TargetUnit:
    """
    Specifies information about a targeted unit, although the precise meaning of this data type isn't verified.

    Parameters
    ----------
    snapshotControlPlayerId : int
        Specifies which player had control over the unit.
    snapshotPoint : Target3D
        Specifies the point at which the unit was targeted.
    snapshotUnitLink : int
        An unknown parameter.
    snapshotUpkeepPlayerId : int
        Specifies which player's supply was affected.
    tag : int
        Specifies a unit tag.
    targetUnitFlags : int
        An unknown parameter.
    timer : int
        An unknown parameter.
    """

    snapshotControlPlayerId: int
    snapshotPoint: Target3D
    snapshotUnitLink: int
    snapshotUpkeepPlayerId: int
    tag: int
    targetUnitFlags: int
    timer: int
