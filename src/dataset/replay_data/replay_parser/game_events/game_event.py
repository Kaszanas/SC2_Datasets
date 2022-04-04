import abc
from types import NotImplementedType
from typing import Dict, Literal

import torch

# TODO: from_dict documentation


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
        _summary_

        :param dict: _description_
        :type dict: Dict
        :raises NotImplementedError: _description_
        :return: _description_
        :rtype: MessageEvent
        """
        raise NotImplementedError
