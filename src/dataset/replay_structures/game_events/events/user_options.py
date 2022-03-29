class UserOptions:
    """_summary_

    :param baseBuildNum: _description_
    :type baseBuildNum: int
    :param buildNum: _description_
    :type buildNum: int
    :param cameraFollow: _description_
    :type cameraFollow: bool
    :param debugPauseEnabled: _description_
    :type debugPauseEnabled: bool
    :param developmentCheatsEnabled: _description_
    :type developmentCheatsEnabled: bool
    :param gameFullyDownloaded: _description_
    :type gameFullyDownloaded: bool
    :param hotkeyProfile: _description_
    :type hotkeyProfile: str
    :param id: _description_
    :type id: int
    :param isMapToMapTransition: _description_
    :type isMapToMapTransition: bool
    :param loop: _description_
    :type loop: int
    :param multiplayerCheatsEnabled: _description_
    :type multiplayerCheatsEnabled: bool
    :param platformMac: _description_
    :type platformMac: bool
    :param syncChecksummingEnabled: _description_
    :type syncChecksummingEnabled: bool
    :param testCheatsEnabled: _description_
    :type testCheatsEnabled: bool
    :param useGalaxyAsserts: _description_
    :type useGalaxyAsserts: bool
    :param userid: _description_
    :type userid: int
    :param versionFlags: _description_
    :type versionFlags: int
    """

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
