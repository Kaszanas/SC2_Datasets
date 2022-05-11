import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.dataset.pytorch_datasets.sc2_egset_dataset import SC2EGSetDataset

# TODO: Apply required validator as a lambda:
dataset = SC2EGSetDataset(
    unpack_dir=os.path.abspath("./test/test_files/unpack"),
    download=False,
    validator=(),
)


# TODO: Get the number of games that are in the dataset:


# TODO: Get the number of games that were skipped post-validation:
