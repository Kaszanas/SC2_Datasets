from types import NoneType


class ControlGroupUpdate:
    """_summary_

    :param controlGroupIndex: _description_
    :type controlGroupIndex: int
    :param controlGroupUpdate: _description_
    :type controlGroupUpdate: int
    :param id: _description_
    :type id: int
    :param loop: _description_
    :type loop: int
    :param mask: _description_
    :type mask: NoneType
    :param userid: _description_
    :type userid: int
    """

    def __init__(
        self,
        controlGroupIndex: int,
        controlGroupUpdate: int,
        id: int,
        loop: int,
        mask: NoneType,
        userid: int,
    ) -> None:

        self.controlGroupIndex = controlGroupIndex
        self.controlGroupUpdate = controlGroupUpdate
        self.id = id
        self.loop = loop
        self.mask = mask
        self.userid = userid
