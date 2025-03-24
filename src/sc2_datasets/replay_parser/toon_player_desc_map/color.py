from typing import Dict


class Color:
    """
    Specifies RGBA model color representation.

    Parameters
    ----------
    a : int
        Specifies an alpha parameter of RGBA.
    b : int
        Specifies a blue parameter of RGBA.
    g : int
        Specifies a green parameter of RGBA.
    r : int
        Specifies a red parameter of RGBA.
    """

    @staticmethod
    def from_dict(d: Dict[str, int]) -> "Color":
        """
        Specifies RGBA model color representation.

        Parameters
        ----------
        a : int
            Specifies an alpha parameter of RGBA.
        b : int
            Specifies a blue parameter of RGBA.
        g : int
            Specifies a green parameter of RGBA.
        r : int
            Specifies a red parameter of RGBA.
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
