from typing import Any, Dict

from sc2_datasets.replay_parser.toon_player_desc_map.color import Color


class ToonPlayerInfo:

    """
    Specifies ToonPlayerInfo class representation.

    Parameters
    ----------
    nickname : str
        Specifies player name in the game.
    playerID : int
        Specifies player id number in the game, example: in 1v1 game: [1,2].
    userID : int
        Specifies id number of player in the game, example: in 1v1 game: [0,1].
    SQ : int
        Specifies spending quotient value,
        ratio between resources mining and spending,
        more information: https://tl.net/forum/starcraft-2/266019-do-you-macro-like-a-pro
    supplyCappedPercent : int
        Specifies a 'supply block' percent of game time that a player was supply capped.
    startDir : int
        Specifies the start direction of the player, expressed in clock.
    startLocX : int
        Specifies x coordinate of player's starting location.
    startLocY : int
        Specifies y coordinate of player's starting location.
    race : str
        Specifies race the player was playing.
    selectedRace : str
        Specifies race the player selected, might be random.
    APM : int
        Specifies average action per minute value of the player in the game.
    MMR : int
        Specifies the value of matchmaking ratio of the player.
    result : str
        Specifies an information if player has/has not won the game.
    region : str
        Specifies the information on which location the game was played on.
    realm : str
        Specifies the information on which server of the location game was played.
    highestLeague : str
        Specifies the player's highest league ever achieved.
    isInClan : bool
        Specifies if the player was a member of the clan.
    clanTag : str
        Specifies the shortcut of the player's clan.
    handicap : int
        Specifies a percentage value of units and structures maximum health points.
    color : Color
        Specifies the color RGBA palette of the player.
    """

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "ToonPlayerInfo":
        """
        Static method returning initialized ToonPlayerInfo class from a dictionary.
        This helps with the original JSON parsing.

        Parameters
        ----------
        d : Dict[str, Any]
            Specifies a dictionary as available in the JSON file
            that is a result of pre-processing some .SC2Replay file.

        Returns
        -------
        ToonPlayerInfo
            Returns an initialized ToonPlayerInfo class.
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
