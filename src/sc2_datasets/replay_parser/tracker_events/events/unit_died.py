from typing import Dict

from sc2_datasets.replay_parser.tracker_events.tracker_event import TrackerEvent


class UnitDied(TrackerEvent):
    """
    UnitDied contains some "details" information about unit
    at the moment of it has died in the game.

    Parameters
    ----------
    id : int
        Specifies the ID of an event which corresponds to its name.
    killerPlayerId : int
        Specifies an id number of played who has controlled and destroyed the unit in the game.
    killerUnitTagIndex : int
        Specifies a pointer for a specific unit which destroyed the unit in the game.
    killerUnitTagRecycle : int
        There is no specific information about this parameter.
    loop : int
        Specifies the game loop number (game-engine tick) at which the event occurred.
    unitTagIndex : int
        Specifies a pointer for a specific unit which was destroyed in the game.
    unitTagRecycle : int
        There is no specific information about this parameter.
    x : int
        Specifies x coordinate of map in pixels where the object was destroyed.
    y : int
        Specifies y coordinate of map in pixels where the object was destroyed.
    """

    def from_dict(d: Dict) -> "UnitDied":
        """
        Static method returning initialized UnitDied class from a dictionary.
        This helps with the original JSON parsing.

        Parameters
        ----------
        d : Dict
            Specifies a dictionary as available in the JSON file that
            is a result of pre-processing some .SC2Replay file.

        Returns
        -------
        UnitDied
            Returns an initialized UnitDied class.
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
