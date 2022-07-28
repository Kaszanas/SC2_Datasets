from typing import Dict

from sc2_datasets.replay_parser.game_events.game_event import GameEvent


class UserOptions(GameEvent):
    """
    UserOptions is containing some "details" information about player's settings,
    profiles, configuration in the game.

    :param baseBuildNum: Specifies a unique version number of the game build,\
    highly likely game engine number
    :type baseBuildNum: int
    :param buildNum: Specifies a unique version number of the build,\
    highly likely game build number
    :type buildNum: int
    :param cameraFollow: Specifies if the camera object is following an object
    :type cameraFollow: bool
    :param debugPauseEnabled: There is no valuable information about this parameter
    :type debugPauseEnabled: bool
    :param developmentCheatsEnabled: Specifies if cheat option for developers have been enabled
    :type developmentCheatsEnabled: bool
    :param gameFullyDownloaded: Specifies if the game was fully downloaded,\
    with campaign, better graphic settings, etc.
    :type gameFullyDownloaded: bool
    :param hotkeyProfile: Specifies the name of the player's hotkey group,\
    the player was playing on in the game
    :type hotkeyProfile: str
    :param id: Specifies the ID of an event which corresponds to its name.
    :type id: int
    :param isMapToMapTransition: There is no valuable information about this parameter
    :type isMapToMapTransition: bool
    :param loop: Specifies the game loop number (game-engine tick) when\
    at which the event occurred
    :type loop: int
    :param multiplayerCheatsEnabled: Specifies if the game was having cheat\
    options enabled in the game
    :type multiplayerCheatsEnabled: bool
    :param platformMac: Specifies if the game has been played on the Mac operating system
    :type platformMac: bool
    :param syncChecksummingEnabled: There is no valuable information about this parameter
    :type syncChecksummingEnabled: bool
    :param testCheatsEnabled: Specifies if the game was having tests on, to detect cheats
    :type testCheatsEnabled: bool
    :param useGalaxyAsserts: There is no valuable information about this parameter
    :type useGalaxyAsserts: bool
    :param userid: Specifies the id of the player who has been\
    the owner of the options in the game
    :type userid: int
    :param versionFlags: There is no valuable information about this parameter,\
    might it be a player's setting version, default = 0
    :type versionFlags: int
    """

    @staticmethod
    def from_dict(d: Dict) -> "UserOptions":
        """
        Static method returning initialized UserOptions class from a dictionary.
        This helps with the original JSON parsing.

        :param d: Specifies a dictionary as available in the JSON file\
        that is a result of pre-processing some .SC2Replay file.
        :type d: Dict
        :return: Returns an initialized UserOptions class.
        :rtype: UserOptions
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
