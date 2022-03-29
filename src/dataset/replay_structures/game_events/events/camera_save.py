from src.dataset.replay_structures.game_events.events.nested.target_2d import Target2D


class CameraSave:

    """_summary_

    :param id: _description_
    :type id: int
    :param loop: _description_
    :type loop: int
    :param target: _description_
    :type target: Target
    :param userid: _description_
    :type userid: int
    :param which: _description_
    :type which: int
    """

    def __init__(
        self,
        id: int,
        loop: int,
        target: Target2D,
        userid: int,
        which: int,
    ) -> None:

        self.id = id
        self.loop = loop
        self.target = target
        self.userid = userid
        self.which = which
