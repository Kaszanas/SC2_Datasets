from typing import Dict

import torch


class Color:
    """
    _summary_

    :param a: _description_
    :type a: int
    :param b: _description_
    :type b: int
    :param g: _description_
    :type g: int
    :param r: _description_
    :type r: int
    """

    @staticmethod
    def from_dict(d: Dict[str, int]) -> "Color":
        """
        _summary_

        :param d: _description_
        :type d: Dict[str, int]
        :return: _description_
        :rtype: Color
        """
        return Color(
            a=d["a"],
            b=d["b"],
            g=d["g"],
            r=d["r"],
        )

    def __init__(
        self,
        a: int,
        b: int,
        g: int,
        r: int,
    ) -> None:

        self.a = a
        self.b = b
        self.g = g
        self.r = r

    def to_tensor(self) -> torch.Tensor:
        pass
