import abc
from types import NotImplementedType
from typing import Dict, Literal


# TODO: from_dict documentation


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
        _summary_

        :param dict: Specifies a dictionary, it holds translations of a phrase or sentence.
        :type dict: Dict
        :raises NotImplementedError: Raises an error if not implemented, this is only an abstract method
        :return: Specifies a sheet of method to must be implemented in other classes
        :rtype: MessageEvent
        """
        raise NotImplementedError
