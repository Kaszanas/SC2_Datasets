from typing import Dict

from sc2_datasets.replay_parser.tracker_events.tracker_event import TrackerEvent


class UnitTypeChange(TrackerEvent):

    """
    UnitTypeChange holds the information about how things were changing during the game.

    :param id: Specifies the ID of an event which corresponds to its name.
    :type id: int
    :param loop: Specifies the game loop number (game-engine tick) when at which the event occurred
    :type loop: int
    :param unitTagIndex: Specifies a pointer for a specific unit which was doing some changes
    :type unitTagIndex: int
    :param unitTagRecycle: There is no specific information about this parameter
    :type unitTagRecycle: int
    :param unitTypeName: Specifies an in game object name, who was doing some changes
    :type unitTypeName: str
    """

    @staticmethod
    def from_dict(d: Dict) -> "UnitTypeChange":
        """
        Static method returning initialized UnitTypeChange class from a dictionary.
        This helps with the original JSON parsing.

        :param d: Specifies a dictionary as available in the JSON file that\
        is a result of pre-processing some .SC2Replay file.
        :type d: Dict
        :return: Returns an initialized UnitTypeChange class.
        :rtype: UnitTypeChange
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
