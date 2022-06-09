class Target2D:
    """
    Data type holding information about a 2D target point in space.

    :param x: Specifies the x value of the target.
    :type x: float
    :param y: Specifies the y value of the target.
    :type y: float
    """

    def __init__(self, x: float, y: float) -> None:

        self.x = x
        self.y = y
