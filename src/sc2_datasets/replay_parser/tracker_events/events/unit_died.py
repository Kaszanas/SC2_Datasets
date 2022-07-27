from typing import Dict

from sc2_datasets.replay_parser.tracker_events.tracker_event import TrackerEvent


class UnitDied(TrackerEvent):

    """
    UnitDied is containing some "details" information about unit
    at the moment of it has died in the game

    :param id: Specifies the ID of an event which corresponds to its name.
    :type id: int
    :param killerPlayerId: Specifies an id number of played who has controlled\
    and destroyed the unit in the game
    :type killerPlayerId: int
    :param killerUnitTagIndex: Specifies a pointer for a specific unit\
    which destroyed the unit in the game
    :type killerUnitTagIndex: int
    :param killerUnitTagRecycle: There is no specific information about this parameter
    :type killerUnitTagRecycle: int
    :param loop: Specifies the game loop number (game-engine tick) at which the event occurred
    :type loop: int
    :param unitTagIndex: Specifies a pointer for a specific unit which\
    was destroyed in the game
    :type unitTagIndex: int
    :param unitTagRecycle: There is no specific information about this parameter
    :type unitTagRecycle: int
    :param x: Specifies x coordinate of map in pixels where the object was destroyed.
    :type x: int
    :param y: Specifies y coordinate of map in pixels where the object was destroyed.
    :type y: int
    """

    def from_dict(d: Dict) -> "UnitDied":
        """
        Static method returning initialized UnitDied class from a dictionary.
        This helps with the original JSON parsing.

        :param d: Specifies a dictionary as available in the JSON file that
        is a result of pre-processing some .SC2Replay file.
        :type d: Dict
        :return: Returns an initialized UnitDied class.
        :rtype: UnitDied
        """
        return UnitDied(
            id=d["id"],
            killerPlayerId=d["killerPlayerId"],
            killerUnitTagIndex=d["killerUnitTagIndex"],
            killerUnitTagRecycle=d["killerUnitTagRecycle"],
            loop=d["loop"],
            unitTagIndex=d["unitTagIndex"],
            unitTagRecycle=["unitTagRecycle"],
            x=d["x"],
            y=d["y"],
        )

    def __init__(
        self,
        id: int,
        killerPlayerId: int,
        killerUnitTagIndex: int,
        killerUnitTagRecycle: int,
        loop: int,
        unitTagIndex: int,
        unitTagRecycle: int,
        x: int,
        y: int,
    ) -> None:

        self.id = id
        self.killerPlayerId = killerPlayerId
        self.killerUnitTagIndex = killerUnitTagIndex
        self.killerUnitTagRecycle = killerUnitTagRecycle
        self.loop = loop
        self.unitTagIndex = unitTagIndex
        self.unitTagRecycle = unitTagRecycle
        self.x = x
        self.y = y
