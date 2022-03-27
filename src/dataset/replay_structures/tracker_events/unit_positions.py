from typing import List


class UnitPositions:
    def __init__(
        self, firstUnitIndex: int, id: int, items: List[int], loop: int
    ) -> None:
        self.firstUnitIndex = firstUnitIndex
        self.id = id
        self.items = items
        self.loop = loop
