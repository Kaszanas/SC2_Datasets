from pathlib import Path

import pandas as pd

from src.dataset.pytorch_datasets.sc2_egset_dataset import SC2EGSetDataset
from src.dataset.transforms.pandas.avg_playerstats_pd_dict import (
    avg_playerstats_pd_dict_transform,
)
from src.dataset.validators.multiprocess_validator import validate_integrity_persist_mp


def sc2egset_dataset_to_dataframe(
    unpack_dir: Path,
    validation_file_path: Path,
):

    dataset = SC2EGSetDataset(
        unpack_dir=unpack_dir,
        download=False,
        transform=avg_playerstats_pd_dict_transform,
        validator=lambda list_of_replays: validate_integrity_persist_mp(
            list_of_replays=list_of_replays,
            n_workers=8,
            validation_file_path=validation_file_path,
        ),
    )

    dataset_dict_list = []
    for index in len(dataset):
        game_dict_row = dataset[index]
        dataset_dict_list.append(game_dict_row)

    dataset_dataframe = pd.DataFrame(dataset_dict_list)

    return dataset_dataframe
