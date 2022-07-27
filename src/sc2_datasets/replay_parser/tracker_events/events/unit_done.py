from typing import Dict

from sc2_datasets.replay_parser.tracker_events.tracker_event import TrackerEvent


class UnitDone(TrackerEvent):

    """
    UnitDone is containing some "details" information about unit at the moment
    of it has built in the game

    :param id: Specifies the ID of an event which corresponds to its name.
    :type id: int
    :param loop: Specifies the game loop number (game-engine tick)\
    at which the event occurred
    :type loop: int
    :param unitTagIndex: Specifies a pointer for a specific unit\
    which was finishing its build
    :type unitTagIndex: int
    :param unitTagRecycle: There is no specific information about this parameter
    :type unitTagRecycle: int
    """

    @staticmethod
    def from_dict(d: Dict) -> "UnitDone":
        """
        Static method returning initialized UnitDone class from a dictionary.
        This helps with the original JSON parsing.

        :param d: Specifies a dictionary as available in the JSON file
        that is a result of pre-processing some .SC2Replay file.
        :type d: Dict
        :return: Returns an initialized UnitDone class.
        :rtype: UnitDone
        """
        return UnitDone(
            id=d["id"],
            loop=d["loop"],
            unitTagIndex=d["unitTagIndex"],
            unitTagRecycle=d["unitTagRecycle"],
        )

    def __init__(
        self,
        id: int,
        loop: int,
        unitTagIndex: int,
        unitTagRecycle: int,
    ) -> None:

        self.id = id
        self.loop = loop
        self.unitTagIndex = unitTagIndex
        self.unitTagRecycle = unitTagRecycle
