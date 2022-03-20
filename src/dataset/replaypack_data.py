import os
import uuid
import requests

from torch.utils.data import Dataset
from dataset.replay_data import SC2ReplayData
import zipfile


def download_replaypack(
    destination_dir: str, replaypack_name: str, replaypack_url: str
) -> str:
    existing_files = os.listdir(destination_dir)

    if len(existing_files) > 1:
        raise Exception()

    if existing_files:
        return existing_files[0]

    response = requests.get(url=replaypack_url)
    download_filepath = os.path.join(destination_dir, replaypack_name + ".zip")
    with open(download_filepath, "wb") as output_map_file:
        output_map_file.write(response.content)

    return download_filepath


# Unpacks zip file at zip_path to a destination directory, into a subdirectory.
def unpack_zipfile(destination_dir: str, subdir: str, zip_path: str):
    with zipfile.ZipFile(zip_path, "r") as zip_file:
        path_to_extract = os.path.join(destination_dir, subdir)
        # Checking the existence of the extraction output directory:
        if not os.path.exists(path_to_extract):
            os.makedirs(path_to_extract)
        zip_file.extractall(path_to_extract)

        return path_to_extract


# TODO: This should hold the extraction logs.
# And other information that comes out of the processing pipeline:
class SC2ReplaypackData(Dataset):
    """
    Holds IterableDatasets for the data that
    is within a single StarCraft .json representation of a replay file.
    """

    def __init__(self, replaypack_directory: str, url="", download=False):
        self.replaypack_directory = replaypack_directory

        replaypack_name = uuid.uuid4().hex

        if download:
            # Get the name from URL or it needs to be hardcoded!
            download_path = download_replaypack(
                replaypack_directory + "/.download/", replaypack_name, url
            )

            replaypack_path = unpack_zipfile(
                destination_dir=replaypack_directory,
                subdir=replaypack_name,
                zip_path=download_path,
            )

            # TODO: find data files and unpack
            replaypack_files = os.listdir(replaypack_path)
            data_path = None

            for file in replaypack_files:
                if file.endswith("_data.zip"):
                    data_path = unpack_zipfile(
                        destination_dir=replaypack_directory,
                        subdir="data",
                        zip_path=file,
                    )

        # Load all of the files
        self.list_of_files = os.listdir(data_path)
        self.len = len(self.list_of_files)

    def __len__(self) -> int:
        return self.len

    def __getitem__(self, index: int) -> SC2ReplayData:
        return SC2ReplayData(replay_filepath=self.list_of_files[index])
