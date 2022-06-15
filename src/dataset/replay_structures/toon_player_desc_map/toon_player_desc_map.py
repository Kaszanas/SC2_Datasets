from src.dataset.replay_structures.toon_player_desc_map.toon import Toon
from src.dataset.replay_structures.toon_player_desc_map.toon_player_info import (
    ToonPlayerInfo,
)


class ToonPlayerDescMap:
    """
    _summary_

    :param toon: _description_
    :type toon: Toon
    :param toon_player_info: _description_
    :type toon_player_info: ToonPlayerInfo
    """

    def __init__(self, toon: Toon, toon_player_info: ToonPlayerInfo) -> None:

        self.toon = toon
        self.toon_player_info = toon_player_info
