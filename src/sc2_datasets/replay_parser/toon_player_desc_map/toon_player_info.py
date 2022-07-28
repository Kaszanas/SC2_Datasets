from typing import Any, Dict

from sc2_datasets.replay_parser.toon_player_desc_map.color import Color


class ToonPlayerInfo:

    """
    Specifies ToonPlayerInfo class representation

    :param nickname: Specifies player name in the game
    :type nickname: str
    :param playerID: Specifies player id number in the game, example: in 1v1 game: [1,2]
    :type playerID: int
    :param userID: Specifies id number of player in the game, example: in 1v1 game: [0,1]
    :type userID: int
    :param SQ: Specifies spending quotient value,\
    ratio between resources mining and spending,\
    more information: https://tl.net/forum/starcraft-2/266019-do-you-macro-like-a-pro
    :type SQ: int
    :param supplyCappedPercent: Specifies a 'supply block' percent of game time\
    that a player was supply capped.
    :type supplyCappedPercent: int
    :param startDir: Specifies  the start direction of the player,\
    expressed in clock
    :type startDir: int
    :param startLocX: Specifies x coordinate of player's starting location
    :type startLocX: int
    :param startLocY: Specifies y coordinate of player's starting location
    :type startLocY: int
    :param race: Specifies race the player was playing
    :type race: str
    :param selectedRace: Specifies race the player selected, might be random
    :type selectedRace: str
    :param APM: Specifies average action per minute value of the player in the game
    :type APM: int
    :param MMR: Specifies the value of matchmaking ratio of the player
    :type MMR: int
    :param result: Specifies an information if player has/has not won the game
    :type result: str
    :param region: Specifies the information on which location the game was played on
    :type region: str
    :param realm: Specifies the information on which server of the location game was played
    :type realm: str
    :param highestLeague: Specifies the player's highest league ever achieved
    :type highestLeague: str
    :param isInClan: Specifies if the player was a member of the clan
    :type isInClan: bool
    :param clanTag: Specifies the shortcut of the player's clan
    :type clanTag: str
    :param handicap: Specifies a percentage value of units and structures maximum health points
    :type handicap: int
    :param color: Specifies the color RGBA palette of the player
    :type color: Color
    """

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "ToonPlayerInfo":
        """
        Static method returning initialized ToonPlayerInfo class from a dictionary.
        This helps with the original JSON parsing.

        :param d: Specifies a dictionary as available in the JSON file\
        that is a result of pre-processing some .SC2Replay file.
        :type d: Dict[str, Any]
        :return: Returns an initialized ToonPlayerInfo class.
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
