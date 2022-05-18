from src.dataset.replay_data.replay_parser.game_events.events.nested.target_3d import (
    Target3D,
)


class TargetUnit:

    """
    _summary_

    :param snapshotControlPlayerId: _description_
    :type snapshotControlPlayerId: int
    :param snapshotPoint: _description_
    :type snapshotPoint: Target3D
    :param snapshotUnitLink: _description_
    :type snapshotUnitLink: int
    :param snapshotUpkeepPlayerId: _description_
    :type snapshotUpkeepPlayerId: int
    :param tag: _description_
    :type tag: int
    :param targetUnitFlags: _description_
    :type targetUnitFlags: int
    :param timer: _description_
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
