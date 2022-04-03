from typing import Any, Tuple

from src.dataset.replay_data.sc2_replay_data import SC2ReplayData


class SelectTarget:
    def __call__(self, sc2_replay_data: SC2ReplayData, target: str) -> Tuple[]:
        """
        _summary_

        :param sc2_replay_data: _description_
        :type sc2_replay_data: SC2ReplayData
        :param target: _description_
        :type target: str
        :return: _description_
        :rtype: Any
        """
        pass

    def __repr__(self) -> str:
        return self.__class__.__name__ + "()"
