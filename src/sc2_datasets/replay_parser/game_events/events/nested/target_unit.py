from sc2_datasets.replay_parser.game_events.events.nested.target_3d import Target3D


class TargetUnit:

    """
    Specifies which unit was targeted.
    We were not able to verify precise meaning of this data type.

    :param snapshotControlPlayerId: Most likely specifies which player had control over the unit.
    :type snapshotControlPlayerId: int
    :param snapshotPoint: Most likely specifies at which point the unit was targeted.
    :type snapshotPoint: Target3D
    :param snapshotUnitLink: This is an unknown parameter.
    :type snapshotUnitLink: int
    :param snapshotUpkeepPlayerId: Most likely specifies which of the players' supply was affected.
    :type snapshotUpkeepPlayerId: int
    :param tag: Most likely specifies a unit tag.
    :type tag: int
    :param targetUnitFlags: This is an unknown parameter.
    :type targetUnitFlags: int
    :param timer: This is an unknown parameter.
    :type timer: int
    """

    def __init__(
        self,
        snapshotControlPlayerId: int,
        snapshotPoint: Target3D,
        snapshotUnitLink: int,
        snapshotUpkeepPlayerId: int,
        tag: int,
        targetUnitFlags: int,
        timer: int,
    ) -> None:

        self.snapshotControlPlayerId = snapshotControlPlayerId
        self.snapshotPoint = snapshotPoint
        self.snapshotUnitLink = snapshotUnitLink
        self.snapshotUpkeepPlayerId = snapshotUpkeepPlayerId
        self.tag = tag
        self.targetUnitFlags = targetUnitFlags
        self.timer = timer
