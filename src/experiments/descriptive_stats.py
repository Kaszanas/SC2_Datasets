import os
from pathlib import Path
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.dataset.pytorch_datasets.sc2_egset_dataset import SC2EGSetDataset
from src.dataset.validators.multiprocess_validator import validate_integrity_persist_mp

if __name__ == "__main__":

    unpack_dir = os.path.abspath("./test/test_files/unpack")

    # TODO: Apply required validator as a lambda:

    def validator(list_of_replays):
        validation_file_path = Path("./src/experiments/validation_file.json").resolve()

        replay_list = list_of_replays

        files_to_skip = validate_integrity_persist_mp(
            list_of_replays=replay_list,
            n_workers=8,
            validation_file_path=validation_file_path,
        )

        return files_to_skip

    dataset = SC2EGSetDataset(
        unpack_dir=unpack_dir, download=False, validator=validator
    )

    # TODO: Get the number of games that are in the dataset:
    # This will be done by reading the file:
    number_of_valid_replays = len(dataset)

    print(number_of_valid_replays)

    number_of_invalid_files = 0
    for replaypack_name, skip_files in dataset.skip_files.items():
        number_of_invalid_files += len(skip_files)

    print(number_of_invalid_files)

    print("something")

    # TODO: Get the number of games that were skipped post-validation:
    # Also done by reading the file:
