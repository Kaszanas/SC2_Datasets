import abc
from types import NotImplementedType
from typing import Dict, Literal


class MessageEvent(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass: type) -> Literal[True] | NotImplementedType:
        return (
            hasattr(subclass, "from_dict")
            and callable(subclass.from_dict)
            or NotImplemented
        )

    @abc.abstractmethod
    def from_dict(d: Dict) -> "MessageEvent":
        """
        Abstract method returning some MessageEvent.
        This method helps with implementation, with the original JSON parsing.

        :param d: Specifies a dictionary, it holds translations\
        of a phrase or sentence.
        :type d: Dict
        :raises NotImplementedError: Raises an error if not implemented,\
        this is only an abstract method
        :return: Returns a method sheet which must be implemented
        :rtype: MessageEvent
        """
        raise NotImplementedError
