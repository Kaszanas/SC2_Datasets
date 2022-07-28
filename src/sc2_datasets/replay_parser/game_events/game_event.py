import abc
from types import NotImplementedType
from typing import Dict, Literal


class GameEvent(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass: type) -> Literal[True] | NotImplementedType:
        return (
            hasattr(subclass, "from_dict")
            and callable(subclass.from_dict)
            or NotImplemented
        )

    @abc.abstractmethod
    def from_dict(d: Dict) -> "GameEvent":
        """
        Abstract method returning some GameEvent. This method helps with implementation,
        with the original JSON parsing.

        :param d: Specifies a dictionary as available in the JSON file\
        that is a result of pre-processing some .SC2Replay file.
        :type d: Dict
        :raises NotImplementedError: Raises an error if method is not implemented
        :return: Returns a method sheet which must be implemented
        :rtype: GameEvent
        """
        raise NotImplementedError
