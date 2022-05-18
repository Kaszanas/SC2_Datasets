from typing import Dict

from src.dataset.replay_data.replay_parser.tracker_events.tracker_event import (
    TrackerEvent,
)

# TODO: Document the docstrings


class Upgrade(TrackerEvent):

    """
    _summary_

    :param count: _description_
    :type count: int
    :param id: _description_
    :type id: int
    :param loop: _description_
    :type loop: int
    :param playerId: _description_
    :type playerId: int
    :param upgradeTypeName: _description_
    :type upgradeTypeName: str
    """

    @staticmethod
    def from_dict(d: Dict) -> "Upgrade":
        """
        _summary_

        :param d: _description_
        :type d: Dict
        :return: _description_
        :rtype: Upgrade
        """
        return Upgrade(
            count=d["count"],
            id=d["id"],
            loop=d["loop"],
            playerId=d["playerId"],
            upgradeTypeName=d["upgradeTypeName"],
        )

    def __init__(
        self,
        count: int,
        id: int,
        loop: int,
        playerId: int,
        upgradeTypeName: str,
    ) -> None:

        self.count = count
        self.id = id
        self.loop = loop
        self.playerId = playerId
        self.upgradeTypeName = upgradeTypeName
