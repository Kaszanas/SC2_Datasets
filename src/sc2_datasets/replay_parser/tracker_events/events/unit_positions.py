from typing import Dict, List

from sc2_datasets.replay_parser.tracker_events.tracker_event import TrackerEvent


class UnitPositions(TrackerEvent):
    """
    UnitPositions holds some detail information about how
    the unit position was changing during the game.

    Parameters
    ----------
    firstUnitIndex : int
        Specifies a pointer for a specific unit which was doing some changes.
    id : int
        Specifies the ID of an event which corresponds to its name.
    items : List[int]
        Specifies a list of int values, there is no specific information what
        the numbers mean.
    loop : int
        Specifies the game loop number (game-engine tick) when at which the event occurred.
    """

    def from_dict(d: Dict) -> "UnitPositions":
        """
        Static method returning initialized UnitPositions class from a dictionary.
        This helps with the original JSON parsing.

        Parameters
        ----------
        d : Dict
            Specifies a dictionary as available in the JSON file that
            is a result of pre-processing some .SC2Replay file.

        Returns
        -------
        UnitPositions
            Returns an initialized UnitPositions class.
        """
        return UnitPositions(
            firstUnitIndex=d["firstUnitIndex"],
            id=d["id"],
            items=d["items"],
            loop=d["loop"],
        )

    def __init__(
        self,
        firstUnitIndex: int,
        id: int,
        items: List[int],
        loop: int,
    ) -> None:
        self.firstUnitIndex = firstUnitIndex
        self.id = id
        self.items = items
        self.loop = loop
