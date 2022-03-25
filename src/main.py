# TODO:This file will run all of the experiments one after the other
# This will be entry point for replicating anyone willing to run it.
from src.dataset.sc2_replaypack_dataset import SC2ReplaypackDataset

SC2ReplaypackDataset(replaypack_name="2016_IEM_10_Taipei")
