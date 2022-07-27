from typing import Dict


class Color:
    """
    Specifies RGBA model color representation

    :param a: Specifies an alpha parameter of RGBA
    :type a: int
    :param b: Specifies a blue parameter of RGBA
    :type b: int
    :param g: Specifies a green parameter of RGBA
    :type g: int
    :param r: Specifies a red parameter of RGBA
    :type r: int
    """

    @staticmethod
    def from_dict(d: Dict[str, int]) -> "Color":
        """
        Static method returning initialized Color class from a dictionary.
        This helps with the original JSON parsing.

        :param d: Specifies a dictionary as available in the JSON file\
        that is a result of pre-processing some .SC2Replay file.
        :type d: Dict[str, int]
        :return: Returns an initialized Color class.
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
