from typing import Dict

from sc2_datasets.replay_parser.tracker_events.tracker_event import TrackerEvent


class UnitTypeChange(TrackerEvent):

    """
    UnitTypeChange holds the information about how things were changing during the game.

    Parameters
    ----------
    id : int
        Specifies the ID of an event which corresponds to its name.
    loop : int
        Specifies the game loop number (game-engine tick) when at which the event occurred.
    unitTagIndex : int
        Specifies a pointer for a specific unit which was doing some changes.
    unitTagRecycle : int
        There is no specific information about this parameter.
    unitTypeName : str
        Specifies an in-game object name, who was doing some changes.
    """

    @staticmethod
    def from_dict(d: Dict) -> "UnitTypeChange":
        """
        Static method returning initialized UnitTypeChange class from a dictionary.
        This helps with the original JSON parsing.

        Parameters
        ----------
        d : Dict
            Specifies a dictionary as available in the JSON file that
            is a result of pre-processing some .SC2Replay file.

        Returns
        -------
        UnitTypeChange
            Returns an initialized UnitTypeChange class.
        """
        return UnitTypeChange(
            id=d["id"],
            loop=d["loop"],
            unitTagIndex=d["unitTagIndex"],
            unitTagRecycle=d["unitTagRecycle"],
            unitTypeName=d["unitTypeName"],
        )

    def __init__(
        self,
        id: int,
        loop: int,
        unitTagIndex: int,
        unitTagRecycle: int,
        unitTypeName: str,
    ) -> None:
        self.id = id
        self.loop = loop
        self.unitTagIndex = unitTagIndex
        self.unitTagRecycle = unitTagRecycle
        self.unitTypeName = unitTypeName
