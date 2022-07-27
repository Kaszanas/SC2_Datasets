from typing import Any, Dict

# pylama:ignore=E501
from sc2_datasets.replay_parser.toon_player_desc_map.toon_player_info import (
    ToonPlayerInfo,
)


class ToonPlayerDesc:
    """
    Specifies ToonPlayerDesc class representation

    :param toon: Specifies a player's unique account identifier, example: 3-S2-1-6904171
    :type toon: Toon
    :param toon_player_info: Specific a ToonPlayerInfo class object,
    which include list of parameters
    :type toon_player_info: ToonPlayerInfo
    """

    @staticmethod
    def from_dict(toon: str, d: Dict[str, Any]) -> "ToonPlayerDesc":
        """
        Static method returning initialized ToonPlayerDesc class from a dictionary.
        This helps with the original JSON parsing.

        :param d: Specifies a dictionary as available in the JSON file\
        that is a result of pre-processing some .SC2Replay file.
        :type d: Dict[str, Any]
        :return: Returns an initialized ToonPlayerDesc class.
        :rtype: ToonPlayerDesc
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
