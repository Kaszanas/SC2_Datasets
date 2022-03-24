import json


class SC2ReplayData:
    def __init__(self, replay_filepath: str) -> None:
        self.replay_filepath = replay_filepath

        with open(self.replay_filepath) as json_file:
            json_data = json.load(json_file)
            self.header = json_data["header"]
            self.init_data = json_data["initData"]

        # TODO: Read JSON file and load info to class

    @property
    def header(self):
        return self.header

    @property
    def init_data(self):
        return self.init_data

    @property
    def initData(self):
        return self.init_data
