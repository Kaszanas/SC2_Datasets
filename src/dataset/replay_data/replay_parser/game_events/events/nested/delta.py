from types import NoneType
from typing import Dict, List


from src.dataset.replay_data.replay_parser.game_events.game_event import GameEvent


class AddSubgroups(GameEvent):

    """
    _summary_

    :param count: _description_
    :type count: int
    :param intraSubgroupPriority: _description_
    :type intraSubgroupPriority: int
    :param subgroupPriority: _description_
    :type subgroupPriority: int
    :param unitLink: _description_
    :type unitLink: int
    """

    @staticmethod
    def from_dict(d: Dict) -> "AddSubgroups":
        return [
            AddSubgroups(
                count=subgroup["count"],
                intraSubgroupPriority=subgroup["intraSubgroupPriority"],
                subgroupPriority=subgroup["subgroupPriority"],
                unitLink=subgroup["unitLink"],
            )
            for subgroup in d
        ]

    def __init__(
        self,
        count: int,
        intraSubgroupPriority: int,
        subgroupPriority: int,
        unitLink: int,
    ) -> None:

        self.count = count
        self.intraSubgroupPriority = intraSubgroupPriority
        self.subgroupPriority = subgroupPriority
        self.unitLink = unitLink


class Delta(GameEvent):

    """
    _summary_

    :param addSubgroups: _description_
    :type addSubgroups: AddSubgroups
    :param addUnitTags: _description_
    :type addUnitTags: List[int]
    :param removeMask: _description_
    :type removeMask: NoneType
    :param subgroupIndex: _description_
    :type subgroupIndex: int
    """

    @staticmethod
    def from_dict(d: Dict) -> "Delta":
        return Delta(
            addSubgroups=AddSubgroups.from_dict(d=d["addSubgroups"]),
            addUnitTags=d["addUnitTags"],
            removeMask=d["removeMask"],
            subgroupIndex=d["subgroupIndex"],
        )

    def __init__(
        self,
        addSubgroups: List[AddSubgroups],
        addUnitTags: List[int],
        removeMask: NoneType,
        subgroupIndex: int,
    ) -> None:

        self.addSubgroups = addSubgroups
        self.addUnitTags = addUnitTags
        self.removeMask = removeMask
        self.subgroupIndex = subgroupIndex
