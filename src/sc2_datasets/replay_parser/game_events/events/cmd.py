from types import NoneType
from typing import Dict

from sc2_datasets.replay_parser.game_events.game_event import GameEvent


# TODO: Can the sequence be an int here?
# Should this be encoded somehow if there is a NoneType detected?


class Cmd(GameEvent):
    """
    Cmd is containing some "details" information about command interface events

    :param id: Specifies the ID of an event which corresponds to its name.
    :type id: int
    :param loop: Specifies the game loop number (game-engine tick)\
    at which the event occurred
    :type loop: int
    :param otherUnit: There is no specific information about this parameter
    :type otherUnit: NoneType
    :param sequence: Highly likely this parameter specifies\
    an id parameter which sequence user has typed in the console,\
    there is no specific information about this parameter
    :type sequence: int
    :param unitGroup: There is no specific information about this parameter
    :type unitGroup: NoneType | int
    :param userid: Highly likely this parameter specifies\
    a user's id who has been using interface, there is no specific information.
    :type userid: int
    """

    @staticmethod
    def from_dict(d: Dict) -> "Cmd":
        """
        Static method returning initialized Cmd class from a dictionary.
        This helps with the original JSON parsing.

        :param d: Specifies a dictionary as available in the JSON file\
        that is a result of pre-processing some .SC2Replay file.
        :type d: Dict
        :return: Returns an initialized Cmd class.
        :rtype: Cmd
        """
        return Cmd(
            id=d["id"],
            loop=d["loop"],
            otherUnit=d["otherUnit"],
            sequence=d["sequence"],
            unitGroup=d["unitGroup"],
            userid=d["userid"]["userId"],
        )

    def __init__(
        self,
        id: int,
        loop: int,
        otherUnit: NoneType,
        sequence: int,
        unitGroup: NoneType | int,
        userid: int,
    ) -> None:
        self.id = id
        self.loop = loop
        self.otherUnit = otherUnit
        self.sequence = sequence
        self.unitGroup = unitGroup
        self.userid = userid
