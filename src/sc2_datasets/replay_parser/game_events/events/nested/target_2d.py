class Target2D:
    """
    Data type holding information about a 2D target point in space.

    Parameters
    ----------
    x : float
        Specifies the x value of the target.
    y : float
        Specifies the y value of the target.
    """

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
