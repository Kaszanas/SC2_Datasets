import json
import logging
from io import BufferedReader
from pathlib import Path

from tqdm import tqdm

from sc2_datasets.torch.datasets.sc2_dataset import SC2Dataset

# NOTE: For now this implementation assumes that each JSON object is on its own line.


def get_json_offsets(json_filepath: Path, offsets_filepath: Path) -> list[int]:
    """
    Retrieves or creates the list of byte offsets for each JSON object
    in a large JSON file.

    Parameters
    ----------
    json_filepath : Path
        Specifies the path to the JSON file.
    offsets_filepath : Path
        Specifies the path to the offsets file.

    Returns
    -------
    list[int]
        Returns the list of byte offsets for each JSON object.
    """
    if offsets_filepath.exists():
        logging.info(f"Loading pre-computed JSON offsets from: {str(offsets_filepath)}")
        with offsets_filepath.open("r", encoding="utf-8") as f:
            offsets = json.load(f)
        return offsets

    offsets = index_json_objects(json_filepath=json_filepath)
    logging.info(f"Saving computed JSON offsets to: {str(offsets_filepath)}")
    with offsets_filepath.open("w", encoding="utf-8") as f:
        json.dump(offsets, f)

    return offsets


def index_json_objects(json_filepath: Path) -> list[int]:
    """
    Indexes the starting byte offset of each JSON object.

    ASSUMES the file is a single pretty-printed array:
    Line 1: [
    Lines 2 to N-1: object followed by a comma (e.g., {...},)
    Line N: object (no comma)
    Last Line: ]


    Parameters
    ----------
    filepath : Path
        Specifies the path to the JSON file.

    """
    offsets = []
    progress_bar = tqdm(desc="Indexing JSON objects", unit="object")

    logging.info(f"Indexing JSON objects in file: {str(json_filepath)}")

    # Use standard file handle in binary mode for accurate byte tracking
    with json_filepath.open("rb") as f:
        # Skip the opening '[' and the newline:
        f.readline()

        while True:
            # Record the current position (start of the next object line)
            start_offset = f.tell()

            # Read the line. This moves the file pointer.
            line = f.readline()

            if not line:
                # End of file reached (or last ']' line)
                break

            # If the line starts with ']', we stop.
            if line.strip().startswith(b"]"):
                break

            # Store the start offset for the successfully read line
            offsets.append(start_offset)
            progress_bar.update(1)

    progress_bar.close()

    logging.info(f"Indexed {len(offsets)} JSON objects.")

    return offsets


def get_object_at_index(
    file_handle: BufferedReader,
    offsets: list[int],
    index: int,
) -> dict:
    """
    Retrieves the complete JSON object at the specified index by seeking
    to the pre-calculated line offset, reading one line, and stripping the trailing comma.
    Assumes each JSON object is on its own line.

    Parameters
    ----------
    file_handle

    offsets : list[int]
        List of byte offsets for each JSON object.
    index : int
        Index of the JSON object to retrieve.

    Returns
    -------
    dict
        The JSON object parsed into a Python dictionary.

    Raises
    ------
    Exception
        If reading the line at the specified offset fails.
    """

    if index < 0 or index >= len(offsets):
        return {}

    start_offset = offsets[index]

    file_handle.seek(start_offset)
    line = file_handle.readline()

    if not line:
        raise Exception("Failed to read line at specified offset!")

    # Decode bytes to string
    line_str = line.decode("utf-8")

    # Clean trailing comma/whitespace
    # We strip whitespace, remove trailing comma if present, then strip again
    json_str = line_str.strip().rstrip(",").strip()

    # Parse with standard library C-optimized parser
    python_obj = json.loads(json_str)

    return python_obj


def merge_json_files(input_dir: Path, output_filepath: Path) -> Path:
    """
    Merges all JSON files in the input directory into a single JSON file.
    Adds additional information fields to each JSON object.

    Parameters
    ----------
    input_dir : Path
        Input directory containing JSON files to be merged.
    output_filepath : Path
        Output filepath where the merged JSON file will be written.

    Returns
    -------
    Path
        Returns the output filepath where the merged JSON file was written.
    """

    with output_filepath.open("w", encoding="utf-8") as output_file:
        output_file.write("[\n")
        first_entry = True

        for json_file in input_dir.glob("*.json"):
            first_entry = json_to_line(
                json_replay_path=json_file,
                output_file=output_file,
                first_entry=first_entry,
            )

        output_file.write("]")

    return output_filepath


def json_to_line(
    json_replay_path: Path,
    output_file: BufferedReader,
    first_entry: bool,
    replaypack_name: str | None = None,
    replaypack_url: str | None = None,
    filename: str | None = None,
    old_file_path: Path | None = None,
    sort_keys: bool = False,
) -> None:
    """
    Loads a JSON replay file, adds additional information, and writes it as a single line.
    By default the additional information is set to none for compatibility with older replays,
    and potentially other datasets that do not have this information.

    Parameters
    ----------
    json_replay_path : Path
        Specifies a path to the JSON file.
    output_file : BufferedReader
        Specifies the output file handle where the single-line JSON will be written.
    first_entry : bool
        Whether this is the first entry in the output file.
    replaypack_name : str | None, optional
        Replaypack name to beplaced in additional information, by default None
    replaypack_url : str | None, optional
        Replaypack url to be placed in additional information, by default None
    filename : str | None, optional
        Filename from which the JSON came originally, by default None
    old_file_path : Path | None, optional
        Path to the file before it was processed, by default None
    sort_keys : bool, optional
        If the JSON keys are supposed to be sorted, by default False
    """

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
                sort_keys=sort_keys,
            )
            first_entry = False
            return first_entry
    except Exception as e:
        logging.warning(
            f"Failed to load JSON replay file: {str(json_replay_path)} from replaypack: {replaypack_name} with error: {str(e)}"
        )

    return first_entry


def dataset_to_single_json(
    dataset: SC2Dataset,
    output_filepath: Path,
    sort_keys: bool = False,
) -> Path:
    """
    Iterates over an input SC2Dataset and writes all replays into a single JSon file.

    Parameters
    ----------
    dataset : SC2Dataset
        Specifies the input dataset that will be processed.
    output_filepath : Path
        Specifies the output filepath where the single JSON file will be written.
    sort_keys : bool, optional
        Whether to sort the keys in the output JSON file, by default False.

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

                first_entry = json_to_line(
                    json_replay_path=json_replay_path,
                    output_file=output_file,
                    first_entry=first_entry,
                    replaypack_name=replaypack_name,
                    replaypack_url=replaypack_url,
                    filename=filename,
                    old_file_path=old_file_path,
                    sort_keys=sort_keys,
                )

        output_file.write("]")

    return output_filepath


# from io import BufferedReader
# import ijson
# from ijson.common import ObjectBuilder
# NOTE: Benchmarking showed that this method is 5x slower than the using json.loads():
# def parse_exact_object_at_offset(f: BufferedReader, offset: int) -> dict | None:
#     """
#     Seeks to an offset and parses exactly one JSON object.
#     Stops immediately after the closing brace '}' to avoid reading trailing commas.
#     """
#     # Seek to the precise start of the object (the '{'):
#     f.seek(offset)

#     # Create a raw event parser
#     # This yields events like ('prefix', 'event_type', 'value')
#     parser = ijson.parse(f)

#     # Use ObjectBuilder to reconstruct the dict from events automatically
#     builder = ObjectBuilder()

#     # Iterate over the stream of events
#     for prefix, event, value in parser:
#         # Feed the event into the builder to construct the Python object:
#         builder.event(event, value)

#         # 5. The Magic Condition:
#         # If we hit 'end_map' (closing brace '}') AND the prefix is empty (root level),
#         # it means we have just finished the object we started at the offset.
#         if event == "end_map" and (prefix == "" or prefix is None):
#             # We have the full object. BREAK immediately.
#             # Do NOT ask the parser for the next event (which would be the comma).
#             return builder.value

#     return None


# def get_object_at_index(
#     file_path: Path,
#     offsets: list[int],
#     index: int,
# ) -> dict:
#     """
#     Retrieves the complete JSON object at the specified index by seeking
#     to the pre-calculated line offset, reading one line, and stripping the trailing comma.


#     Parameters
#     ----------
#     file_path : Path
#         Specifies the path to the JSON file.
#     offsets : list[int]
#         Specifies the list of byte offsets for each JSON object.
#     index : int
#         Specifies the index of the JSON object to retrieve.
#     """
#     if index < 0 or index >= len(offsets):
#         raise IndexError(
#             "Index out of range. Cannot retrieve object from an indexed JSON file."
#         )

#     start_offset = offsets[index]
#     with file_path.open("rb") as f:
#         try:
#             maybe_dict = parse_exact_object_at_offset(f=f, offset=start_offset)
#             if maybe_dict:
#                 return maybe_dict, True
#         except Exception as e:
#             logging.exception(
#                 f"Error parsing object at index {index}, offset {start_offset}: {e}"
#             )
#             return dict(), False

#     return dict(), False
