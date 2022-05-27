import os
from pathlib import Path
import sys
from typing import Any, Dict

import pandas as pd
from tqdm import tqdm

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.dataset.replay_data.sc2_replay_data import SC2ReplayData
from src.dataset.transforms.pandas.player_stats_to_dict import playerstats_to_dict
from src.dataset.pytorch_datasets.sc2_egset_dataset import SC2EGSetDataset
from src.dataset.validators.multiprocess_validator import validate_integrity_persist_mp


def create_additional_data(replay: SC2ReplayData) -> Dict[str, Any]:

    game_hash = hash(replay)
    map_name = replay.metadata.mapName
    game_time_gameloop = replay.header.elapsedGameLoops

    additional_data = {}

    for toon_desc_map in replay.toonPlayerDescMap:
        playerID = str(toon_desc_map.toon_player_info.playerID)

        if playerID in additional_data:
            return {}

        player_name = toon_desc_map.toon_player_info.nickname
        player_toon = toon_desc_map.toon

        if playerID not in additional_data:
            # Addinga additional data that doesnt change:
            additional_data[playerID] = {
                "game_hash": game_hash,
                "map_name": map_name,
                "player_name": player_name,
                "player_toon": player_toon,
                "game_time_gameloop": game_time_gameloop,
            }

    return additional_data


def main():
    unpack_dir = os.path.abspath("./test/test_files/unpack")

    def validator(list_of_replays):
        validation_file_path = Path("./src/experiments/validation_file.json").resolve()

        files_to_skip = validate_integrity_persist_mp(
            list_of_replays=list_of_replays,
            n_workers=8,
            validation_file_path=validation_file_path,
        )

        return files_to_skip

    dataset = SC2EGSetDataset(
        unpack_dir=unpack_dir,
        download=False,
        validator=validator,
    )

    failed_files = 0
    incorrect_player_id = 0
    exception_counter = 0
    processed_files = len(dataset)
    for i in tqdm(range(len(dataset))):
        try:
            replay = dataset[i]

            additional_data = create_additional_data(replay=replay)
            if not additional_data:
                # print("Empty additional data returned, incorrect player id.")
                failed_files += 1
                incorrect_player_id += 1
                continue

            for playerID, additional_features in additional_data.items():
                for toon_desc_map in replay.toonPlayerDescMap:
                    if playerID != str(toon_desc_map.toon_player_info.playerID):
                        continue
                    race = toon_desc_map.toon_player_info.race
                    outcome = toon_desc_map.toon_player_info.result
                    if "race" not in additional_features:
                        additional_data[playerID]["race"] = race
                    if "outcome" not in additional_features:
                        additional_data[playerID]["outcome"] = outcome

            single_game_df = playerstats_to_dict(
                sc2_replay=replay, additional_data_dict=additional_data
            )

            output_path = Path("sc2egset_csv.csv")
            for playerID, player_game_repr in single_game_df.items():
                # Write to csv consecutively:
                final_dataframe = pd.DataFrame(player_game_repr)
                final_dataframe.to_csv(
                    output_path.resolve().as_posix(),
                    index=False,
                    mode="a",
                    header=not output_path.resolve().exists(),
                )

        except:
            failed_files += 1
            exception_counter += 1
            # print(f"Failed to process a file {i}")

    print(f"Processed files: {processed_files}")
    print(f"Failed files: {failed_files}")
    print(f"Exceptions files: {exception_counter}")
    print(f"Incorrect ID: {incorrect_player_id}")


if __name__ == "__main__":
    main()
