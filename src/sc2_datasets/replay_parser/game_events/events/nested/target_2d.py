from dataclasses import dataclass


@dataclass
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

    x: float
    y: float
