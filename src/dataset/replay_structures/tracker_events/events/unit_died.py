class UnitDied:

    """
    _summary_

    :param id: _description_
    :type id: int
    :param killerPlayerId: _description_
    :type killerPlayerId: int
    :param killerUnitTagIndex: _description_
    :type killerUnitTagIndex: int
    :param killerUnitTagRecycle: _description_
    :type killerUnitTagRecycle: int
    :param loop: _description_
    :type loop: int
    :param unitTagIndex: _description_
    :type unitTagIndex: int
    :param unitTagRecycle: _description_
    :type unitTagRecycle: int
    :param x: _description_
    :type x: int
    :param y: _description_
    :type y: int
    """

    def __init__(
        self,
        id: int,
        killerPlayerId: int,
        killerUnitTagIndex: int,
        killerUnitTagRecycle: int,
        loop: int,
        unitTagIndex: int,
        unitTagRecycle: int,
        x: int,
        y: int,
    ) -> None:

        self.id = id
        self.killerPlayerId = killerPlayerId
        self.killerUnitTagIndex = killerUnitTagIndex
        self.killerUnitTagRecycle = killerUnitTagRecycle
        self.loop = loop
        self.unitTagIndex = unitTagIndex
        self.unitTagRecycle = unitTagRecycle
        self.x = x
        self.y = y
