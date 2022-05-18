import os
from pathlib import Path
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from src.experiments.utils.dataset_to_dataframe import (
    sc2egset_dataset_to_dataframe,
)


# TODO: Test if this works:
if __name__ == "__main__":
    unpack_dir = Path("./test/test_files/unpack").resolve().as_posix()
    validation_file_path = Path("./src/experiments/validation_file.json").resolve()

    dataset_dataframe = sc2egset_dataset_to_dataframe(
        unpack_dir=unpack_dir,
        validation_file_path=validation_file_path,
    )

    # TODO: Perform H2O logistic regression.
