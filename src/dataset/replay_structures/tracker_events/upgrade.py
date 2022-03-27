class Upgrade:

    """_summary_

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

    def __init__(
        self, count: int, id: int, loop: int, playerId: int, upgradeTypeName: str
    ) -> None:

        self.count = count
        self.id = id
        self.loop = loop
        self.playerId = playerId
        self.upgradeTypeName = upgradeTypeName
