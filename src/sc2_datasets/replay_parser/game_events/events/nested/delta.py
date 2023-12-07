from types import NoneType
from typing import Dict, List

from sc2_datasets.replay_parser.game_events.game_event import GameEvent


class AddSubgroups(GameEvent):

    """
    AddSubgroups is a data type holding information about some subgroup change.
    The exact meaning or context of its attributes remains unclear.

    Parameters
    ----------
    count : int
        Specifies some unknown count parameter.
    intraSubgroupPriority : int
        Specifies some priority within the intra subgroup.
    subgroupPriority : int
        Specifies some subgroup priority.
    unitLink : int
        Most likely specifies which units were affected.
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
    Most likely specifies a change in which units belong to some subgroups.
    The exact definition of this data type remains unclear.

    Parameters
    ----------
    addSubgroups : AddSubgroups
        Most likely specifies a class with additional information
        on which subgroups were added.
    addUnitTags : List[int]
        Most likely specifies which unit tags were added to a subgroup.
    removeMask : NoneType
        This is an unknown parameter. We were not able to interpret it.
    subgroupIndex : int
        Most likely specifies which subgroup was changed.
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
