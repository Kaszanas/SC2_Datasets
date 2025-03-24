from typing import Dict

from sc2_datasets.replay_parser.game_events.game_event import GameEvent


class UserOptions(GameEvent):
    """
    Represents UserOptions containing detailed information about a player's settings,
    profiles, and configuration within the game.

    Parameters
    ----------
    baseBuildNum : int
        A unique version number of the game build, likely representing the game engine number.
    buildNum : int
        A unique version number of the build, likely indicating the game build number.
    cameraFollow : bool
        Indicates if the camera object is following an object.
    debugPauseEnabled : bool
        Indicates the availability of information about this parameter.
    developmentCheatsEnabled : bool
        Specifies if the cheat options for developers have been enabled.
    gameFullyDownloaded : bool
        Indicates if the game was fully downloaded, including campaign and enhanced graphics.
    hotkeyProfile : str
        Name of the player's hotkey group used in the game.
    id : int
        ID corresponding to the event.
    isMapToMapTransition : bool
        Availability of information regarding map transitions.
    loop : int
        Game loop number at which the event occurred.
    multiplayerCheatsEnabled : bool
        Indicates if cheat options were enabled in the game.
    platformMac : bool
        Indicates if the game was played on the Mac operating system.
    syncChecksummingEnabled : bool
        Availability of information about checksumming.
    testCheatsEnabled : bool
        Indicates if tests were enabled in the game to detect cheats.
    useGalaxyAsserts : bool
        Availability of information about Galaxy Asserts.
    userid : int
        ID of the player who owned the options in the game.
    versionFlags : int
        Availability of information about version flags, default value is 0.
    """

    @staticmethod
    def from_dict(d: Dict) -> "UserOptions":
        """
        Static method returning an initialized UserOptions class from a dictionary.
        This assists in parsing the original JSON data.

        Parameters
        ----------
        d : Dict
            A dictionary available in the JSON file resulting from pre-processing
            an .SC2Replay file.

        Returns
        -------
        UserOptions
            Returns an initialized UserOptions class.

        """
        return UserOptions(
            baseBuildNum=d["baseBuildNum"],
            buildNum=d["buildNum"],
            cameraFollow=d["cameraFollow"],
            debugPauseEnabled=d["debugPauseEnabled"],
            developmentCheatsEnabled=d["developmentCheatsEnabled"],
            gameFullyDownloaded=d["gameFullyDownloaded"],
            hotkeyProfile=d["hotkeyProfile"],
            id=d["id"],
            isMapToMapTransition=d["isMapToMapTransition"],
            loop=d["loop"],
            multiplayerCheatsEnabled=d["multiplayerCheatsEnabled"],
            platformMac=d["platformMac"],
            syncChecksummingEnabled=d["syncChecksummingEnabled"],
            testCheatsEnabled=d["testCheatsEnabled"],
            useGalaxyAsserts=d["useGalaxyAsserts"],
            userid=d["userid"]["userId"],
            versionFlags=d["versionFlags"],
        )

    def __init__(
        self,
        baseBuildNum: int,
        buildNum: int,
        cameraFollow: bool,
        debugPauseEnabled: bool,
        developmentCheatsEnabled: bool,
        gameFullyDownloaded: bool,
        hotkeyProfile: str,
        id: int,
        isMapToMapTransition: bool,
        loop: int,
        multiplayerCheatsEnabled: bool,
        platformMac: bool,
        syncChecksummingEnabled: bool,
        testCheatsEnabled: bool,
        useGalaxyAsserts: bool,
        userid: int,
        versionFlags: int,
    ) -> None:
        self.baseBuildNum = baseBuildNum
        self.buildNum = buildNum
        self.cameraFollow = cameraFollow
        self.debugPauseEnabled = debugPauseEnabled
        self.developmentCheatsEnabled = developmentCheatsEnabled
        self.gameFullyDownloaded = gameFullyDownloaded
        self.hotkeyProfile = hotkeyProfile
        self.id = id
        self.isMapToMapTransition = isMapToMapTransition
        self.loop = loop
        self.multiplayerCheatsEnabled = multiplayerCheatsEnabled
        self.platformMac = platformMac
        self.syncChecksummingEnabled = syncChecksummingEnabled
        self.testCheatsEnabled = testCheatsEnabled
        self.useGalaxyAsserts = useGalaxyAsserts
        self.userid = userid
        self.versionFlags = versionFlags
