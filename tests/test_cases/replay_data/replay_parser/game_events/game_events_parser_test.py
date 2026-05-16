import json
import unittest

import pytest

import tests.test_utils.test_utils as test_utils
from sc2_datasets.replay_parser.game_events.game_event import GameEvent
from sc2_datasets.replay_parser.game_events.game_events_parser import GameEventsParser
from sc2_datasets.utils.json_backends import AvailableBackends, load, set_json_backend


@pytest.mark.minor
class GameEventsParserTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.test_replay = test_utils.get_specific_asset_path(
            filename="test_replay.json"
        )

    def test_game_events_parser(self):
        for backend in AvailableBackends:
            with self.subTest(backend=backend.value):
                set_json_backend(backend.value)
                with open(self.test_replay, "rb") as f:
                    loaded_file = load(f)

                    # Iterating over all of the game events and verifying
                    # If the parsing works correctly:
                    for game_event in loaded_file["gameEvents"]:
                        some_parsed_event = GameEventsParser.from_dict(d=game_event)
                        self.assertIsInstance(some_parsed_event, GameEvent)
