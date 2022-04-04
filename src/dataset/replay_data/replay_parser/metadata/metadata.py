from typing import Any, Dict

import torch


class Metadata:
    """
    _summary_

    :param baseBuild: _description_
    :type baseBuild: str
    :param dataBuild: _description_
    :type dataBuild: str
    :param durationSeconds: _description_
    :type durationSeconds: int
    :param gameVersion: _description_
    :type gameVersion: str
    :param mapName: _description_
    :type mapName: str
    """

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Metadata":
        """
        _summary_

        :param d: _description_
        :type d: Dict[str, Any]
        :return: _description_
        :rtype: Metadata
        """
        return Metadata(
            baseBuild=d["baseBuild"],
            dataBuild=d["dataBuild"],
            durationSeconds=d["durationSeconds"],
            gameVersion=d["gameVersion"],
            mapName=d["mapName"],
        )

    def __init__(
        self,
        baseBuild: str,
        dataBuild: str,
        durationSeconds: int,
        gameVersion: str,
        mapName: str,
    ) -> None:

        self.baseBuild = baseBuild
        self.dataBuild = dataBuild
        self.durationSeconds = durationSeconds
        self.gameVersion = gameVersion
        self.mapName = mapName

    def to_tensor(self) -> torch.Tensor:
        pass
