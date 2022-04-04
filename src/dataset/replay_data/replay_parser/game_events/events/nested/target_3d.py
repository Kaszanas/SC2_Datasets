import torch


class Target3D:

    """
    _summary_

    :param x: _description_
    :type x: float
    :param y: _description_
    :type y: float
    :param z: _description_
    :type z: float
    """

    def __init__(self, x: float, y: float, z: float) -> None:

        self.x = x
        self.y = y
        self.z = z

    def to_tensor(self) -> torch.Tensor:
        pass
