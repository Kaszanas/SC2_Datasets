from typing import Dict

from sc2_datasets.replay_parser.tracker_events.tracker_event import TrackerEvent


class UnitOwnerChange(TrackerEvent):
    """
    UnitOwnerChange holds some detail information about how the unit position
    was changing during the game.

    Parameters
    ----------
    controlPlayerId : int
        Specifies the information about player id who made the unit in the game.
    id : int
        Specifies the ID of an event which corresponds to its name.
    loop : int
        Specifies the game loop number (game-engine tick) when at which the event occurred.
    unitTagIndex : int
        Specifies a pointer for a specific unit which was doing some changes.
    unitTagRecycle : int
        There is no specific information about this parameter.
    upkeepPlayerId : int
        Specifies an id number of player who was having the control of the unit in the game.
    """

    def from_dict(d: Dict[str, int]) -> "UnitOwnerChange":
        """
        Static method returning initialized UnitOwnerChange class from a dictionary.
        This helps with the original JSON parsing.

        Parameters
        ----------
        d : Dict
            Specifies a dictionary as available in the JSON file that
            is a result of pre-processing some .SC2Replay file.

        Returns
        -------
        UnitOwnerChange
            Returns an initialized UnitOwnerChange class.
        """
        return UnitOwnerChange(
            controlPlayerId=d["controlPlayerId"],
            id=d["id"],
            loop=d["loop"],
            unitTagIndex=d["unitTagIndex"],
            unitTagRecycle=d["unitTagRecycle"],
            upkeepPlayerId=d["upkeepPlayerId"],
        )

    def __init__(
        self,
        controlPlayerId: int,
        id: int,
        loop: int,
        unitTagIndex: int,
        unitTagRecycle: int,
        upkeepPlayerId: int,
    ) -> None:
        self.controlPlayerId = controlPlayerId
        self.id = id
        self.loop = loop
        self.unitTagIndex = unitTagIndex
        self.unitTagRecycle = unitTagRecycle
        self.upkeepPlayerId = upkeepPlayerId
