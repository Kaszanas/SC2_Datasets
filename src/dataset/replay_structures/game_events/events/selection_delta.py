class SelectionDelta:
    def __init__(
        self,
        controlGroupId,
        delta,
        id,
        loop,
        userid,
    ) -> None:
        self.controlGroupId = controlGroupId
        self.delta = delta
        self.id = id
        self.loop = loop
        self.userid = userid
