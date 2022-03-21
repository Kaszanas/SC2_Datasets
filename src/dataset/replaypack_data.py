import os
import uuid
import requests

from torch.utils.data import Dataset
from dataset.replay_data import SC2ReplayData
import zipfile


def download_replaypack(
    destination_dir: str, replaypack_name: str, replaypack_url: str
) -> str:
    """
    Exposes logic for downloading a single StarCraft II replaypack from an url.

    :param destination_dir: Specifies the destination directory where the replaypack will be saved.
    :type destination_dir: str
    :param replaypack_name: Specifies the name of a replaypack that will be used for the downloaded .zip archive.
    :type replaypack_name: str
    :param replaypack_url: Specifies the url that is a direct link to the .zip which will be downloaded.
    :type replaypack_url: str
    :raises Exception: If more than one file is downloaded, exception is thrown.
    :return: Returns the filepath to the downloaded .zip archive.
    :rtype: str
    """

    # Check if there is something in the destination directory:
    existing_files = os.listdir(destination_dir)
    if len(existing_files) > 1:
        raise Exception("There is more than one file in the destination directory!")

    # The file was previously downloaded so return it immediately:
    if existing_files:
        if existing_files[0].endswith(".zip"):
            return existing_files[0]
        raise Exception(
            "The file that was detected does not end with a .zip extension! Wrong file was downloaded!"
        )

    # Send a request and save the response content into a .zip file.
    # The .zip file should be a replaypack:
    response = requests.get(url=replaypack_url)
    filename_with_ext = replaypack_name + ".zip"
    download_filepath = os.path.join(destination_dir, filename_with_ext)
    with open(download_filepath, "wb") as output_zip_file:
        output_zip_file.write(response.content)

    return download_filepath


# Unpacks zip file at zip_path to a destination directory, into a subdirectory.
def unpack_zipfile(destination_dir: str, subdir: str, zip_path: str):
    """_summary_

    :param destination_dir: _description_
    :type destination_dir: str
    :param subdir: _description_
    :type subdir: str
    :param zip_path: _description_
    :type zip_path: str
    :return: _description_
    :rtype: _type_
    """
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

    def __init__(
        self,
        replaypack_directory: str,
        replaypack_name: str,
        url: str = "",
        download: bool = False,
    ):
        self.replaypack_directory = replaypack_directory
        self.replaypack_name = replaypack_name

        if download:
            # TODO: Files cannot be downloaded in the same place!
            # This needs to be split as in sc2_dataset.py into download dir and the unpack dir.
            download_path = download_replaypack(
                destination_dir=replaypack_directory + "/.download/",
                replaypack_name=self.replaypack_name,
                replaypack_url=url,
            )

            replaypack_path = unpack_zipfile(
                destination_dir=replaypack_directory,
                subdir=self.replaypack_name,
                zip_path=download_path,
            )

            # TODO: find data files and unpack
            replaypack_files = os.listdir(replaypack_path)
            data_path = None

            for file in replaypack_files:
                if file.endswith("_data.zip"):
                    data_path = unpack_zipfile(
                        destination_dir=replaypack_directory,
                        subdir=self.replaypack_name + "_data",
                        zip_path=file,
                    )

        # Load all of the files
        self.list_of_files = os.listdir(data_path)
        self.len = len(self.list_of_files)

    def __len__(self) -> int:
        return self.len

    def __getitem__(self, index: int) -> SC2ReplayData:
        return SC2ReplayData(replay_filepath=self.list_of_files[index])
