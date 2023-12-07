class Target3D:

    """
    Data type holding information about a 3D target point in space.

    Parameters
    ----------
    x : float
        Specifies the x value of the target.
    y : float
        Specifies the y value of the target.
    z : float
        Specifies the z value of the target.
    """

    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z
