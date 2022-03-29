class UnitOwnerChange:
    """_summary_

    :param controlPlayerId: _description_
    :type controlPlayerId: int
    :param id: _description_
    :type id: int
    :param loop: _description_
    :type loop: int
    :param unitTagIndex: _description_
    :type unitTagIndex: int
    :param unitTagRecycle: _description_
    :type unitTagRecycle: int
    :param upkeepPlayerId: _description_
    :type upkeepPlayerId: int
    """

    def __init__(
        self,
        controlPlayerId: int,
        id: int,
        loop: int,
        unitTagIndex: int,
        unitTagRecycle: int,
        upkeepPlayerId: int,
    ) -> None:

        self.controlPlayerId = controlPlayerId
        self.id = id
        self.loop = loop
        self.unitTagIndex = unitTagIndex
        self.unitTagRecycle = unitTagRecycle
        self.upkeepPlayerId = upkeepPlayerId
