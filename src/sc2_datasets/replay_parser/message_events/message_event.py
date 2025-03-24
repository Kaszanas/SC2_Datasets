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
        Abstract method returning a MessageEvent.
        This method assists in the implementation for original JSON parsing.

        Parameters
        ----------
        d : Dict
            Specifies a dictionary holding translations of a phrase or sentence.

        Raises
        ------
        NotImplementedError
            If not implemented, this abstract method raises an error.

        Returns
        -------
        MessageEvent
            A method sheet that must be implemented.
        """
        raise NotImplementedError
