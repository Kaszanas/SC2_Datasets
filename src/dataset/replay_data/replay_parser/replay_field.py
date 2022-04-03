import abc
from types import NotImplementedType
from typing import Dict

# from pyparsing import Literal
import torch


class SC2ReplayField(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass: type):  # -> Literal[True] | NotImplementedType:
        return True
        # (
        #     hasattr(subclass, "from_dict")
        #     and callable(subclass.from_dict)
        #     # and hasattr(subclass, "to_tensor")
        #     # and hasattr(subclass.to_tensor)
        #     or NotImplemented
        # )

    # @abc.abstractmethod
    # def from_dict(d: Dict) -> "SC2ReplayField":
    #     """
    #     _summary_

    #     :param d: _description_
    #     :type d: Dict
    #     :raises NotImplementedError: _description_
    #     :return: _description_
    #     :rtype: ReplayField
    #     """
    #     raise NotImplementedError

    # @abc.abstractmethod
    # def to_tensor(self) -> torch.Tensor:
    #     """
    #     _summary_

    #     :raises NotImplementedError: _description_
    #     :return: _description_
    #     :rtype: torch.Tensor
    #     """
    #     raise NotImplementedError
