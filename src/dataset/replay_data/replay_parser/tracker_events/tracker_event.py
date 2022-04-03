import abc
from types import NotImplementedType
from typing import Dict, Literal

import torch

# TODO: from_dict documentation


class TrackerEvent(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass: type) -> Literal[True] | NotImplementedType:
        return True
        #  (
        #     hasattr(subclass, "from_dict")
        #     and callable(subclass.from_dict)
        #     # and hasattr(subclass, "to_tensor")
        #     # and callable(subclass.to_tensor)
        #     or NotImplemented
        # )

    @abc.abstractmethod
    def from_dict(d: Dict) -> "TrackerEvent":
        """
        _summary_

        :param dict: _description_
        :type dict: Dict
        :raises NotImplementedError: _description_
        :return: _description_
        :rtype: MessageEvent
        """
        raise NotImplementedError

    # @abc.abstractmethod
    # def to_tensor(self) -> torch.Tensor:
    #     """
    #     _summary_

    #     :raises NotImplementedError: _description_
    #     :return: _description_
    #     :rtype: torch.Tensor
    #     """
    #     raise NotImplementedError
