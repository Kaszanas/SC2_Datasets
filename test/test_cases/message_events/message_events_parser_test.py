import json
import unittest
from src.dataset.replay_structures.message_events.message_event import MessageEvent
from src.dataset.replay_structures.message_events.message_events_parser import (
    MessageEventParser,
)
import test.test_utils.test_utils as test_utils


class MessageEventsParserTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.test_replay = test_utils.get_specific_asset(filename="test_replay.json")

    def test_message_events_parser(self):

        with open(self.test_replay) as f:
            loaded_file = json.load(f)

            # Iterating over all of the message events and verifying
            # If the parsing works correctly:
            for game_event in loaded_file["messageEvents"]:
                some_parsed_event = MessageEventParser.from_dict(d=game_event)
                self.assertIsInstance(some_parsed_event, MessageEvent)
