from typing import Any, Dict

import torch
from src.dataset.replay_data.replay_parser.toon_player_desc_map.color import Color


class ToonPlayerInfo:

    """
    _summary_

    :param nickname: _description_
    :type nickname: _type_
    :param playerID: _description_
    :type playerID: _type_
    :param userID: _description_
    :type userID: _type_
    :param SQ: _description_
    :type SQ: _type_
    :param supplyCappedPercent: _description_
    :type supplyCappedPercent: _type_
    :param startDir: _description_
    :type startDir: _type_
    :param startLocX: _description_
    :type startLocX: _type_
    :param startLocY: _description_
    :type startLocY: _type_
    :param race: _description_
    :type race: _type_
    :param selectedRace: _description_
    :type selectedRace: _type_
    :param APM: _description_
    :type APM: _type_
    :param MMR: _description_
    :type MMR: _type_
    :param result: _description_
    :type result: _type_
    :param region: _description_
    :type region: _type_
    :param realm: _description_
    :type realm: _type_
    :param highestLeague: _description_
    :type highestLeague: _type_
    :param isInClan: _description_
    :type isInClan: bool
    :param clanTag: _description_
    :type clanTag: _type_
    :param handicap: _description_
    :type handicap: _type_
    :param color: _description_
    :type color: Color
    """

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "ToonPlayerInfo":
        """
        _summary_

        :param d: _description_
        :type d: Dict[str, Any]
        :return: _description_
        :rtype: ToonPlayerInfo
        """
        return ToonPlayerInfo(
            nickname=d["nickname"],
            playerID=d["playerID"],
            userID=d["userID"],
            SQ=d["SQ"],
            supplyCappedPercent=d["supplyCappedPercent"],
            startDir=d["startDir"],
            startLocX=d["startLocX"],
            startLocY=d["startLocY"],
            race=d["race"],
            selectedRace=d["selectedRace"],
            APM=d["APM"],
            MMR=d["MMR"],
            result=d["result"],
            region=d["region"],
            realm=d["realm"],
            highestLeague=d["highestLeague"],
            isInClan=d["isInClan"],
            clanTag=d["clanTag"],
            handicap=d["handicap"],
            color=Color.from_dict(d=d["color"]),
        )

    def __init__(
        self,
        nickname: str,
        playerID: int,
        userID: int,
        SQ: int,
        supplyCappedPercent: int,
        startDir: int,
        startLocX: int,
        startLocY: int,
        race: str,
        selectedRace: str,
        APM: int,
        MMR: int,
        result: str,
        region: str,
        realm: str,
        highestLeague: str,
        isInClan: bool,
        clanTag: str,
        handicap: int,
        color: Color,
    ) -> None:

        self.nickname = nickname
        self.playerID = playerID
        self.userID = userID
        self.SQ = SQ
        self.supplyCappedPercent = supplyCappedPercent
        self.startDir = startDir
        self.startLocX = startLocX
        self.startLocY = startLocY
        self.race = race
        self.selectedRace = selectedRace
        self.APM = APM
        self.MMR = MMR
        self.result = result
        self.region = region
        self.realm = realm
        self.highestLeague = highestLeague
        self.isInClan = isInClan
        self.clanTag = clanTag
        self.handicap = handicap
        self.color = color

    def to_tensor(self) -> torch.Tensor:
        pass
