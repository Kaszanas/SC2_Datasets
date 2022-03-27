class PlayerSetup:

    """
    _summary_

    :param id: _description_
    :type id: int
    :param loop: _description_
    :type loop: int
    :param playerId: _description_
    :type playerId: int
    :param slotId: _description_
    :type slotId: int
    :param type: _description_
    :type type: int
    :param userId: _description_
    :type userId: int
    """

    def __init__(
        self, id: int, loop: int, playerId: int, slotId: int, type: int, userId: int
    ) -> None:

        self.id = id
        self.loop = loop
        self.playerId = playerId
        self.slotId = slotId
        self.type = type
        self.userId = userId
