import abc
from types import NotImplementedType
from typing import Dict, Literal


class TrackerEvent(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass: type) -> Literal[True] | NotImplementedType:
        return (
            hasattr(subclass, "from_dict")
            and callable(subclass.from_dict)
            or NotImplemented
        )

    @abc.abstractmethod
    def from_dict(d: Dict) -> "TrackerEvent":
        """
        Abstract method returning some TrackerEvent.
        This method helps with implementation, with the original JSON parsing.

        Parameters
        ----------
        d : Dict
            Specifies a dictionary as available in the JSON file
            that is a result of pre-processing some .SC2Replay file.

        Raises
        ------
        NotImplementedError
            Raises an error if not implemented, this is only an abstract method.

        Returns
        -------
        TrackerEvent
            Returns a method sheet which must be implemented.
        """
        raise NotImplementedError
