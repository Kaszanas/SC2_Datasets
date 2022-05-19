import os
from pathlib import Path
import sys

# Importing the GLM estimator:
import h2o
from h2o.estimators.glm import H2OGeneralizedLinearEstimator

# Initializing H2O backend:
from h2o.backend import H2OLocalServer


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

    # Start H2o server
    for _ in range(5):
        hs = H2OLocalServer.start()
    # Connect to the H2o server:
    h2o.connect(server=hs)

    # TODO: Perform H2O logistic regression.
