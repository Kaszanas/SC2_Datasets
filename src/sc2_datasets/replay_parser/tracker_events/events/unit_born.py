from typing import Dict

from sc2_datasets.replay_parser.tracker_events.tracker_event import TrackerEvent


class UnitBorn(TrackerEvent):
    """
    UnitBorn contains some "details" information about unit
    at the moment of it has appeared in the game.

    Parameters
    ----------
    controlPlayerId : int
        Specifies the information about player id who made the unit in the game.
    id : int
        Specifies the ID of an event which corresponds to its name.
    loop : int
        Specifies the game loop number (game-engine tick) at which the event occurred.
    unitTagIndex : int
        Specifies a pointer for a specific unit which was creating in the game.
    unitTagRecycle : int
        There is no specific information about this parameter.
    unitTypeName : str
        Specifies the in game unit name that was created in the game.
    upkeepPlayerId : int
        Specifies an id number of player who was having the control of the unit in the game.
    x : int
        Specifies x coordinate of map in pixels where the object was created.
    y : int
        Specifies y coordinate of map in pixels where the object was created.
    """

    def from_dict(d: Dict) -> "UnitBorn":
        """
        Static method returning initialized UnitBorn class from a dictionary.
        This helps with the original JSON parsing.

        Parameters
        ----------
        d : Dict
            Specifies a dictionary as available in the JSON file
            that is a result of pre-processing some .SC2Replay file.

        Returns
        -------
        UnitBorn
            Returns an initialized UnitBorn class.
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
