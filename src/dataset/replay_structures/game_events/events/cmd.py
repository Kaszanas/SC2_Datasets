from types import NoneType

# TODO: Can the sequence be an int here?
# Should this be encoded somehow if there is a NoneType detected?


class Cmd:
    """_summary_

    :param id: _description_
    :type id: int
    :param loop: _description_
    :type loop: int
    :param otherUnit: _description_
    :type otherUnit: NoneType
    :param sequence: _description_
    :type sequence: int
    :param unitGroup: _description_
    :type unitGroup: NoneType | int
    :param userid: _description_
    :type userid: int
    """

    def __init__(
        self,
        id: int,
        loop: int,
        otherUnit: NoneType,
        sequence: int,
        unitGroup: NoneType | int,
        userid: int,
    ) -> None:

        self.id = id
        self.loop = loop
        self.otherUnit = otherUnit
        self.sequence = sequence
        self.unitGroup = unitGroup
        self.userid = userid
