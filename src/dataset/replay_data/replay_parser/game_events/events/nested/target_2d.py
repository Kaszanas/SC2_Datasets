import torch


class Target2D:
    """
    _summary_

    :param x: _description_
    :type x: float
    :param y: _description_
    :type y: float
    """

    def __init__(self, x: float, y: float) -> None:

        self.x = x
        self.y = y

    def to_tensor(self) -> torch.Tensor:
        pass
