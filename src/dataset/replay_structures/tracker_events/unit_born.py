class UnitBorn:
    def __init__(
        self,
        controlPlayerId: int,
        id: int,
        loop: int,
        unitTagIndex: int,
        unitTagRecycle: int,
        unitTypeName: str,
        upkeepPlayerId: int,
        x: int,
        y: int,
    ) -> None:
        self.controlPlayerId = controlPlayerId
        self.id = id
        self.loop = loop
        self.unitTagIndex = unitTagIndex
        self.unitTagRecycle = unitTagRecycle
        self.unitTypeName = unitTypeName
        self.upkeepPlayerId = upkeepPlayerId
        self.x = x
        self.y = y
