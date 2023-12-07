from typing import Any, Dict

# pylama:ignore=E501
from sc2_datasets.replay_parser.toon_player_desc_map.toon_player_info import (
    ToonPlayerInfo,
)


class ToonPlayerDesc:
    """
    Specifies ToonPlayerDesc class representation.

    Parameters
    ----------
    toon : Toon
        Specifies a player's unique account identifier, example: 3-S2-1-6904171.
    toon_player_info : ToonPlayerInfo
        Specific a ToonPlayerInfo class object, which includes a list of parameters.
    """

    @staticmethod
    def from_dict(toon: str, d: Dict[str, Any]) -> "ToonPlayerDesc":
        """
        Specifies ToonPlayerDesc class representation.

        Parameters
        ----------
        toon : Toon
            Specifies a player's unique account identifier, example: 3-S2-1-6904171.
        toon_player_info : ToonPlayerInfo
            Specific a ToonPlayerInfo class object, which includes a list of parameters.
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
