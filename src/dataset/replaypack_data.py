from torch.utils.data import Dataset
import os

from dataset.replay_data import SC2ReplayData

# TODO: This should hold the extraction logs.
# And other information that comes out of the processing pipeline:
class SC2ReplaypackData(Dataset):
    """
    Holds IterableDatasets for the data that
    is within a single StarCraft .json representation of a replay file.
    """

    def __init__(self, replaypack_directory: str) -> None:
        self.replaypack_directory = replaypack_directory
        self.list_of_files = []
        self.len = 0
        # Load all of the files
        if os.path.exists(self.replaypack_directory) and os.path.isdir(
            self.replaypack_directory
        ):
            self.list_of_files = os.listdir(self.replaypack_directory)
            self.len = len(self.list_of_files)

    def __len__(self) -> int:
        return self.len

    def __getitem__(self, index: int) -> "SC2ReplayData":

        # TODO: Load the data from the json file and return SC2ReplayData
        replay_filepath = self.list_of_files[index]
        sc2_replay_data = SC2ReplayData(replay_filepath=replay_filepath)

        return sc2_replay_data
