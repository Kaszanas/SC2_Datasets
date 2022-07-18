import json
import unittest
from sc2egset_dataset.dataset.replay_data.replay_parser.tracker_events.tracker_event import (
    TrackerEvent,
)
from sc2egset_dataset.dataset.replay_data.replay_parser.tracker_events.tracker_events_parser import (
    TrackerEventsParser,
)
import tests.test_utils.test_utils as test_utils


class TrackerEventsParserTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.test_replay = test_utils.get_specific_asset(filename="test_replay.json")

    def test_tracker_events_parser(self):

        with open(self.test_replay) as f:
            loaded_file = json.load(f)

            # Iterating over all of the tracker events and verifying
            # If the parsing works correctly:
            for tracker_event in loaded_file["trackerEvents"]:
                some_parsed_event = TrackerEventsParser.from_dict(d=tracker_event)
                self.assertIsInstance(some_parsed_event, TrackerEvent)
