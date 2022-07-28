from typing import Dict


from sc2_datasets.replay_parser.tracker_events.tracker_event import TrackerEvent


class UnitOwnerChange(TrackerEvent):
    """
    UnitOwnerChange holds some detail information about how the unit position
    was changing during the game.

    :param controlPlayerId: Specifies the information about player id who made the unit in the game
    :type controlPlayerId: int
    :param id: Specifies the ID of an event which corresponds to its name.
    :type id: int
    :param loop: Specifies the game loop number (game-engine tick) when at which the event occurred
    :type loop: int
    :param unitTagIndex: Specifies a pointer for a specific unit which was doing some changes
    :type unitTagIndex: int
    :param unitTagRecycle: There is no specific information about this parameter
    :type unitTagRecycle: int
    :param upkeepPlayerId: Specifies an id number of player who was having\
    the control of the unit in the game
    :type upkeepPlayerId: int
    """

    def from_dict(d: Dict[str, int]) -> "UnitOwnerChange":
        """
        Static method returning initialized UnitOwnerChange class from a dictionary.
        This helps with the original JSON parsing.

        :param d: Specifies a dictionary as available in the JSON file that\
        is a result of pre-processing some .SC2Replay file.
        :type d: Dict
        :return: Returns an initialized UnitOwnerChange class.
        :rtype: UnitOwnerChange
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
