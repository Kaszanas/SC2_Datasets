from typing import Any, Dict


class Details:
    """
    _summary_

    :param gameSpeed: _description_
    :type gameSpeed: str
    :param isBlizzardMap: _description_
    :type isBlizzardMap: bool
    :param timeUTC: _description_
    :type timeUTC: str
    """

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Details":
        """
        _summary_

        :param d: _description_
        :type d: Dict[str, Any]
        :return: _description_
        :rtype: Details
        """
        return Details(
            gameSpeed=d["gameSpeed"],
            isBlizzardMap=d["isBlizzardMap"],
            timeUTC=d["timeUTC"],
        )

    def __init__(
        self,
        gameSpeed: str,
        isBlizzardMap: bool,
        timeUTC: str,
    ) -> None:

        self.gameSpeed = gameSpeed
        self.isBlizzardMap = isBlizzardMap
        self.timeUTC = timeUTC
