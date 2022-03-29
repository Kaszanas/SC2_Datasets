from types import NoneType
from typing import List


class AddSubgroups:

    """_summary_

    :param count: _description_
    :type count: int
    :param intraSubgroupPriority: _description_
    :type intraSubgroupPriority: int
    :param subgroupPriority: _description_
    :type subgroupPriority: int
    :param unitLink: _description_
    :type unitLink: int
    """

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


class Delta:

    """_summary_

    :param addSubgroups: _description_
    :type addSubgroups: AddSubgroups
    :param addUnitTags: _description_
    :type addUnitTags: List[int]
    :param removeMask: _description_
    :type removeMask: NoneType
    :param subgroupIndex: _description_
    :type subgroupIndex: int
    """

    def __init__(
        self,
        addSubgroups: AddSubgroups,
        addUnitTags: List[int],
        removeMask: NoneType,
        subgroupIndex: int,
    ) -> None:

        self.addSubgroups = addSubgroups
        self.addUnitTags = addUnitTags
        self.removeMask = removeMask
        self.subgroupIndex = subgroupIndex
