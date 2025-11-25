import json
import logging
from pathlib import Path

from tqdm import tqdm

from sc2_datasets.torch.datasets.sc2_dataset import SC2Dataset


def dataset_to_single_json(
    dataset: SC2Dataset,
    output_filepath: Path,
) -> Path:
    """
    Iterates over an input SC2Dataset and writes all replays into a single JSon file.

    Parameters
    ----------
    dataset : SC2Dataset
        Specifies the input dataset that will be processed.
    output_filepath : Path
        Specifies the output filepath where the single JSON file will be written.

    Returns
    -------
    Path
        Returns the output filepath where the single JSON file was written.
    """

    replaypacks = dataset.replaypacks

    if output_filepath.exists():
        logging.info(
            f"Output filepath {str(output_filepath)} already exists, returning existing file."
        )
        return output_filepath

    with output_filepath.open("w", encoding="utf-8") as output_file:
        output_file.write("[\n")
        first_entry = True

        for replaypack in replaypacks:
            len_replaypack = len(replaypack)

            processed_dir_mapping = replaypack._replaypack_dir_mapping

            replaypack_name = replaypack.replaypack_name
            replaypack_url = replaypack.url

            replay_filepaths = replaypack.list_of_files

            for file_index in tqdm(
                range(len_replaypack),
                desc=f"Processing replays in {replaypack_name}",
            ):
                json_replay_path = replay_filepaths[file_index]
                filename = json_replay_path.name

                old_file_path = processed_dir_mapping.get(filename, None)

                try:
                    with json_replay_path.open("r", encoding="utf-8") as json_file:
                        json_data = json.load(json_file)
                        json_data["additional_information"] = {
                            "replaypack_name": replaypack_name,
                            "replaypack_url": replaypack_url,
                            "filename": filename,
                            "original_filepath": str(old_file_path)
                            if old_file_path is not None
                            else None,
                        }
                        if not first_entry:
                            output_file.write(",\n")

                        json.dump(
                            json_data,
                            output_file,
                            separators=(",", ":"),
                            ensure_ascii=False,
                            sort_keys=True,
                        )
                        first_entry = False

                except Exception as e:
                    logging.warning(
                        f"Failed to load JSON replay file: {str(json_replay_path)} from replaypack: {replaypack_name} with error: {str(e)}"
                    )
        output_file.write("]")

    return output_filepath
