import os
from typing import Dict, Tuple

import requests

from src.dataset.utils.zip_utils import unpack_zipfile


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

    **Correct Usage Examples:**

    The use of this method is intended to download a .zip replaypack of SC2 games.

    You should set every parameter, destination_dir, replaypack_name and replaypack_url.

    May help you to download the SC2 replaypack with .zip extension

    The parameters should be set as in the example below.

    >>> download_replaypack_object = download_replaypack(
    ...    destination_dir=replaypack_download_dir,
    ...    replaypack_name=replaypack_name,
    ...    replaypack_url=url)

    >>> assert isinstance(destination_dir, str)
    >>> assert isinstance(replaypack_name, str)
    >>> assert isinstance(replaypack_url, str)
    >>> assert len(os.listdir(destination_dir)) == 0
    >>> assert existing_files[0].endswith(".zip")

    **Incorrect Usage Examples:**

    >>> wrong_type_object = int(2)
    >>> download_replaypack_object = download_replaypack(
    ...    destination_dir=wrong_type_object,
    ...    replaypack_name=replaypack_name,
    ...    replaypack_url=url)
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) ...

    If you don't set parameters or paste incorect parameters' type.

    If the destination directory is empty.

    If the downloaded file has no .zip extension.

    It may throw:

    Exception: There is more than one file in the destination directory!

    Exception: The file that was detected does not end with a .zip extension! Wrong file was downloaded!
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

    **Correct Usage Examples:**

    The use of this method is intended to download a .zip replaypack of SC2 games and unpack the downloaded files
    to the folder.

    You should set every parameter, replaypack_download_dir, replaypack_unpack_dir, replaypack_name and url.

    May help you to download and unpack downloaded files.

    The parameters should be set as in the example below.

    >>> download_and_unpack_replaypack_object = download_and_unpack_replaypack(
    ...            replaypack_download_dir="/directory/replaypack_download_dir",
    ...            replaypack_unpack_dir="/directory/replaypack_unpack_dir",
    ...            replaypack_name="replaypack_name",
    ...            url="url")

    >>> assert isinstance(replaypack_download_dir, str)
    >>> assert isinstance(replaypack_unpack_dir, str)
    >>> assert isinstance(replaypack_name, str)
    >>> assert isinstance(url, str)

    **Incorrect Usage Examples:**

    >>> wrong_type_object = int(2)
    >>> download_and_unpack_replaypack_object = download_and_unpack_replaypack(
    ...            replaypack_download_dir=wrong_type_object,
    ...            replaypack_unpack_dir="/directory/replaypack_unpack_dir",
    ...            replaypack_name="replaypack_name",
    ...            url="url")
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) ...

    If you don't set parameters or paste incorect parameters' type.

    If the parameters aren't set

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
        n_workers=1,
    )
