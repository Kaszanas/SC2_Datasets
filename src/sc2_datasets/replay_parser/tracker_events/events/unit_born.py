from typing import Dict

from sc2_datasets.replay_parser.tracker_events.tracker_event import TrackerEvent


class UnitBorn(TrackerEvent):

    """
    UnitBorn is containing some "details" information about unit
    at the moment of it has appeared in the game

    :param controlPlayerId: Specifies the information about player id who made\
    the unit in the game
    :type controlPlayerId: int
    :param id: Specifies the ID of an event which corresponds to its name.
    :type id: int
    :param loop: Specifies the game loop number (game-engine tick)\
    at which the event occurred
    :type loop: int
    :param unitTagIndex: Specifies a pointer for a specific unit which\
    was creating in the game
    :type unitTagIndex: int
    :param unitTagRecycle: There is no specific information about this parameter
    :type unitTagRecycle: int
    :param unitTypeName: Specifies the in game unit name that was created in the game
    :type unitTypeName: str
    :param upkeepPlayerId: Specifies an id number of player who was having\
    the control of the unit in the game
    :type upkeepPlayerId: int
    :param x: Specifies x coordinate of map in pixels where the object was created.
    :type x: int
    :param y: Specifies y coordinate of map in pixels where the object was created.
    :type y: int
    """

    def from_dict(d: Dict) -> "UnitBorn":
        """
        Static method returning initialized UnitBorn class from a dictionary.
        This helps with the original JSON parsing.

        :param d: Specifies a dictionary as available in the JSON file\
        that is a result of pre-processing some .SC2Replay file.
        :type d: Dict
        :return: Returns an initialized UnitBorn class.
        :rtype: UnitBorn
        """
        return UnitBorn(
            controlPlayerId=d["controlPlayerId"],
            id=d["id"],
            loop=d["loop"],
            unitTagIndex=d["unitTagIndex"],
            unitTagRecycle=d["unitTagRecycle"],
            unitTypeName=d["unitTypeName"],
            upkeepPlayerId=d["upkeepPlayerId"],
            x=d["x"],
            y=d["y"],
        )

    def __init__(
        self,
        controlPlayerId: int,
        id: int,
        loop: int,
        unitTagIndex: int,
        unitTagRecycle: int,
        unitTypeName: str,
        upkeepPlayerId: int,
        x: int,
        y: int,
    ) -> None:
        self.controlPlayerId = controlPlayerId
        self.id = id
        self.loop = loop
        self.unitTagIndex = unitTagIndex
        self.unitTagRecycle = unitTagRecycle
        self.unitTypeName = unitTypeName
        self.upkeepPlayerId = upkeepPlayerId
        self.x = x
        self.y = y
