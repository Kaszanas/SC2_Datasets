import json
from typing import Any, Dict
import logging

from src.dataset.replay_data.replay_parser.details.details import Details

from src.dataset.replay_data.replay_parser.game_events.game_events_parser import (
    GameEventsParser,
)
from src.dataset.replay_data.replay_parser.header.header import Header
from src.dataset.replay_data.replay_parser.init_data.init_data import InitData
from src.dataset.replay_data.replay_parser.message_events.message_events_parser import (
    MessageEventsParser,
)
from src.dataset.replay_data.replay_parser.metadata.metadata import Metadata
from src.dataset.replay_data.replay_parser.toon_player_desc_map.toon_player_desc import (
    ToonPlayerDesc,
)
from src.dataset.replay_data.replay_parser.tracker_events.tracker_events_parser import (
    TrackerEventsParser,
)


class SC2ReplayData:

    """
    _summary_

    :param loaded_replay_object: _description_
    :type loaded_replay_object: Any
    """

    @staticmethod
    def from_file(replay_filepath: str) -> "SC2ReplayData":
        """
        _summary_

        :param replay_filepath: _description_
        :type replay_filepath: str
        :return: _description_
        :rtype: SC2ReplayData
        """
        logging.info(f"\nAttempting to parse: {replay_filepath}")
        with open(replay_filepath, encoding="utf-8") as replay_file:
            try:
                loaded_data = json.load(replay_file)
            except UnicodeDecodeError as exc:
                logging.error(
                    f"UnicodeDecodeError was raised for file {replay_filepath}",
                    exc_info=True,
                )
            return SC2ReplayData(loaded_replay_object=loaded_data)

    def __init__(self, loaded_replay_object: Any) -> None:

        self._header = Header.from_dict(d=loaded_replay_object["header"])
        self._initData = InitData.from_dict(d=loaded_replay_object["initData"])
        self._details = Details.from_dict(d=loaded_replay_object["details"])
        self._metadata = Metadata.from_dict(d=loaded_replay_object["metadata"])
        # TODO: We might want this to be a IterableDataset using PyTorch class:
        self._messageEvents = []
        if loaded_replay_object["messageEvents"]:
            for event_dict in loaded_replay_object["messageEvents"]:
                self._messageEvents.append(MessageEventsParser.from_dict(d=event_dict))
        # TODO: We might want this to be a IterableDataset using PyTorch class:
        self._gameEvents = []
        if loaded_replay_object["gameEvents"]:
            for event_dict in loaded_replay_object["gameEvents"]:
                self._gameEvents.append(GameEventsParser.from_dict(d=event_dict))
        # TODO: We might want this to be a IterableDataset using PyTorch class:
        self._trackerEvents = []
        if loaded_replay_object["trackerEvents"]:
            for event_dict in loaded_replay_object["trackerEvents"]:
                self._trackerEvents.append(TrackerEventsParser.from_dict(d=event_dict))
        # TODO: We might want this to be a IterableDataset using PyTorch class:
        toon_player_desc_dict: Dict[str, Dict[str, Any]] = loaded_replay_object[
            "ToonPlayerDescMap"
        ]
        self._toonPlayerDescMap = [
            ToonPlayerDesc.from_dict(toon=toon, d=player_dict)
            for toon, player_dict in toon_player_desc_dict.items()
        ]

        self._gameEventsErr: bool = loaded_replay_object["gameEventsErr"]
        self._messageEventsErr: bool = loaded_replay_object["messageEventsErr"]
        self._trackerEventsErr: bool = loaded_replay_object["trackerEvtsErr"]

    def to_tensor(self):
        pass

    @property
    def initData(self):
        return self._init_data

    @property
    def header(self):
        return self._header

    @property
    def details(self):
        return self._details

    @property
    def metadata(self):
        return self._metadata

    @property
    def messageEvents(self):
        return self._messageEvents

    @property
    def gameEvents(self):
        return self._gameEvents

    @property
    def trackerEvents(self):
        return self._trackerEvents

    @property
    def toonPlayerDescMap(self):
        return self._toonPlayerDescMap
