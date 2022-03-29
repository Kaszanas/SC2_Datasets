class CommandManagerState:
    """_summary_

    :param id: _description_
    :type id: int
    :param loop: _description_
    :type loop: int
    :param sequence: _description_
    :type sequence: int
    :param state: _description_
    :type state: int
    :param userid: _description_
    :type userid: int
    """

    def __init__(
        self,
        id: int,
        loop: int,
        sequence: int,
        state: int,
        userid: int,
    ) -> None:

        self.id = id
        self.loop = loop
        self.sequence = sequence
        self.state = state
        self.userid = userid
