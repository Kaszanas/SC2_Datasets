import json
import unittest
from src.dataset.replay_structures.game_events.game_event import GameEvent
from src.dataset.replay_structures.game_events.game_events_parser import (
    GameEventsParser,
)

import test.test_utils.test_utils as test_utils


class GameEventsParserTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.test_replay = test_utils.get_specific_asset(filename="test_replay.json")

    def test_tracker_events_parser(self):

        with open(self.test_replay) as f:
            loaded_file = json.load(f)

            # Iterating over all of the tracker events and verifying
            # If the parsing works correctly:
            for tracker_event in loaded_file["gameEvents"]:
                some_parsed_event = GameEventsParser.from_dict(d=tracker_event)
                self.assertIsInstance(some_parsed_event, GameEvent)
