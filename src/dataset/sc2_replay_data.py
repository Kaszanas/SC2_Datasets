import json


class SC2ReplayData:
    def __init__(self, replay_filepath: str) -> None:
        self.replay_filepath = replay_filepath

        self._header = {}
        self._init_data = {}

        with open(self.replay_filepath) as json_file:
            # TODO: Read JSON file and load info to class
            json_data = json.load(json_file)
            self._header = json_data["header"]
            self._init_data = json_data["initData"]

            # TODO: Check what are the unique game events that can occur
            # And create serialization classes for them so that the json can be parsed.

    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, header):
        self._header = header

    @property
    def init_data(self):
        return self._init_data

    @init_data.setter
    def init_data(self, init_data):
        self._init_data = init_data

    @property
    def initData(self):
        return self._init_data
