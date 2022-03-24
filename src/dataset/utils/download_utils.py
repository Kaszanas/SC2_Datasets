import os
from typing import Dict, Tuple
import requests

from dataset.utils.zip_utils import unpack_zipfile
from dataset.utils.dataset_utils import load_replaypack_information


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


def download_and_unpack_replaypack(
    replaypack_download_dir: str,
    replaypack_unpack_dir: str,
    replaypack_name: str,
    url: str,
) -> Tuple[str, Dict[str, str], Dict[str, str]]:
    """
    Helper function that downloads a replaypack from a specified url.
    The archive is saved to replaypack_download_dir using a replaypack_name.
    This function extracts the replaypack to the replaypack_unpack_dir

    :param replaypack_download_dir: Specifies a directory where the .zip archive will be downloaded.
    :type replaypack_download_dir: str
    :param replaypack_unpack_dir: Specifies a directory where the .zip file will be extracted under a replaypack_name directory.
    :type replaypack_unpack_dir: str
    :param replaypack_name: Specifies a replaypack name which will be used to create paths.
    :type replaypack_name: str
    :param url: Specifies the url that will be used to download the replaypack.
    :type url: str
    """

    # Downloading the replaypack:
    download_path = download_replaypack(
        destination_dir=replaypack_download_dir,
        replaypack_name=replaypack_name,
        replaypack_url=url,
    )

    # Unpacking the replaypack:
    replaypack_path = unpack_zipfile(
        destination_dir=replaypack_unpack_dir,
        subdir=replaypack_name,
        zip_path=download_path,
    )
