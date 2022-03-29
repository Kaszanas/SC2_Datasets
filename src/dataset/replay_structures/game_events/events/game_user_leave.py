class GameUserLeave:
    """_summary_

    :param id: _description_
    :type id: int
    :param leaveReason: _description_
    :type leaveReason: int
    :param loop: _description_
    :type loop: int
    :param userid: _description_
    :type userid: int
    """

    def __init__(
        self,
        id: int,
        leaveReason: int,
        loop: int,
        userid: int,
    ) -> None:

        self.id = id
        self.leaveReason = leaveReason
        self.loop = loop
        self.userid = userid
