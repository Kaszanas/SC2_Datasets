import os
from pathlib import Path
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.dataset.pytorch_datasets.sc2_egset_dataset import SC2EGSetDataset
from src.dataset.validators.multiprocess_validator import validate_integrity_persist_mp

if __name__ == "__main__":

    unpack_dir = os.path.abspath("./test/test_files/unpack")
    validation_file_path = Path("./src/experiments/validation_file.json").resolve()

    # TODO: Apply required validator as a lambda:
    dataset = SC2EGSetDataset(
        unpack_dir=unpack_dir,
        download=False,
        validator=lambda list_of_replays: validate_integrity_persist_mp(
            list_of_replays=list_of_replays,
            n_workers=8,
            validation_file_path=validation_file_path,
        ),
    )

    # TODO: Get the number of games that are in the dataset:
    # This will be done by reading the file:

    # TODO: Get the number of games that were skipped post-validation:
    # Also done by reading the file:
