from typing import Any, Dict

import torch
from src.dataset.replay_data.replay_parser.toon_player_desc_map.toon_player_info import (
    ToonPlayerInfo,
)


class ToonPlayerDesc:
    """
    _summary_

    :param toon: _description_
    :type toon: Toon
    :param toon_player_info: _description_
    :type toon_player_info: ToonPlayerInfo
    """

    @staticmethod
    def from_dict(toon: str, d: Dict[str, Any]) -> "ToonPlayerDesc":
        """
        _summary_

        :param d: _description_
        :type d: Dict[str, Any]
        :return: _description_
        :rtype: ToonPlayerDescMap
        """
        return ToonPlayerDesc(
            toon=toon,
            toon_player_info=ToonPlayerInfo.from_dict(d=d),
        )

    def __init__(
        self,
        toon: str,
        toon_player_info: ToonPlayerInfo,
    ) -> None:

        self.toon = toon
        self.toon_player_info = toon_player_info

    def to_tensor(self) -> torch.Tensor:
        pass
