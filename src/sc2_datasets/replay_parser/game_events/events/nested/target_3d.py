class Target3D:

    """
    Data type holding information about a 3D target point in space.

    :param x: Specifies the x value of the target.
    :type x: float
    :param y: Specifies the y value of the target.
    :type y: float
    :param z: Specifies the z value of the target.
    :type z: float
    """

    def __init__(self, x: float, y: float, z: float) -> None:

        self.x = x
        self.y = y
        self.z = z
