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
        Abstract method that returns a GameEvent object. 
        This method aids in implementation,
        specifically in the context of parsing original JSON data.

        Parameters
        ----------
        d : Dict
            A dictionary obtained from pre-processing an .SC2Replay file,\
            available in the JSON format.

        Raises
        ------
        NotImplementedError
            If the method remains unimplemented, this error is raised.

        Returns
        -------
        GameEvent
            A method sheet that must be implemented.
        """
        raise NotImplementedError
