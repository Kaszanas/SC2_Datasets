from pathlib import Path

import requests

from sc2_datasets.utils.zip_utils import unpack_zipfile
from tqdm import tqdm


# REVIEW: This was changed, needs review:
def download_replaypack(
    destination_dir: Path,
    replaypack_name: str,
    replaypack_url: str,
) -> Path:
    """
    Exposes logic for downloading a single StarCraft II replaypack from an url.

    Parameters
    ----------
    destination_dir : Path
        Specifies the destination directory where the replaypack will be saved.
    replaypack_name : str
        Specifies the name of a replaypack that will\
        be used for the downloaded .zip archive.
    replaypack_url : str
        Specifies the url that is a direct link\
        to the .zip which will be downloaded.

    Returns
    -------
    Path
        Returns the filepath to the downloaded .zip archive.

    Examples
    --------
    The use of this method is intended
    to download a .zip replaypack containing StarCraft II games.

    Replaypack download directory should be empty before running
    this function.

    Replaypack name will be used as the name for the downloaded .zip archive.

    Replaypack url should be valid and poiting directly to a .zip archive hosted
    on some server.

    The parameters should be set as in the example below.

    >>> from pathlib import Path
    >>> replaypack_download_dir = Path("datasets/download_directory").resolve()
    >>> replaypack_name = "TournamentName"
    >>> replaypack_url = "some_url"
    >>> download_replaypack_object = download_replaypack(
    ...    destination_dir=replaypack_download_dir,
    ...    replaypack_name=replaypack_name,
    ...    replaypack_url=replaypack_url)

    >>> assert isinstance(replaypack_download_dir, Path)
    >>> assert isinstance(replaypack_name, str)
    >>> assert isinstance(replaypack_url, str)
    >>> assert len(os.listdir(replaypack_download_dir)) == 0
    >>> assert existing_files[0].endswith(".zip")
    """

    # Check if there is something in the destination directory:
    existing_files = []
    if destination_dir.exists():
        existing_files = list(destination_dir.iterdir())

    filename_with_ext = replaypack_name + ".zip"
    download_filepath = Path(destination_dir, filename_with_ext).resolve()

    # The file was previously downloaded so return it immediately:
    if existing_files:
        if download_filepath in existing_files:
            return download_filepath

    # Send a request and save the response content into a .zip file.
    # The .zip file should be a replaypack:
    with requests.get(url=replaypack_url, stream=True) as response:
        total_size = int(response.headers.get("content-length", 0))
        chunk_size = 1 * 10**6  # 1 MB

        with (
            download_filepath.open("wb") as output_zip_file,
            tqdm(
                total=total_size,
                unit="B",
                unit_scale=True,
                desc=f"Downloading: {replaypack_name}",
            ) as progress_bar,
        ):
            for data_chunk in response.iter_content(chunk_size=chunk_size):
                size = output_zip_file.write(data_chunk)
                progress_bar.update(size)

    return download_filepath


def download_and_unpack_replaypack(
    replaypack_download_dir: Path,
    replaypack_unpack_dir: Path,
    replaypack_name: str,
    url: str,
) -> Path:
    """
    Helper function that downloads a replaypack from a specified url.
    The archive is saved to replaypack_download_dir using a replaypack_name.
    This function extracts the replaypack to the replaypack_unpack_dir.

    Parameters
    ----------
    replaypack_download_dir : Path
        Specifies a directory where the .zip archive will be downloaded.
    replaypack_unpack_dir : Path
        Specifies a directory where the .zip file will be extracted
        under a replaypack_name directory.
    replaypack_name : str
        Specifies a replaypack name which will be used to create paths.
    url : str
        Specifies the url that will be used to download the replaypack.

    Returns
    -------
    Path
        Returns the filepath to the directory where the .zip was extracted.

    Examples
    --------
    The use of this method is intended to download a .zip replaypack of SC2 games
    and unpack the downloaded files to the folder.

    You should set every parameter:
    replaypack_download_dir, replaypack_unpack_dir, replaypack_name and url.

    The parameters should be set as in the example below.

    >>> from pathlib import Path
    >>> download_and_unpack_replaypack_object = download_and_unpack_replaypack(
    ...            replaypack_download_dir=Path("./directory/replaypack_download_dir"),
    ...            replaypack_unpack_dir=Path("./directory/replaypack_unpack_dir"),
    ...            replaypack_name="replaypack_name",
    ...            url="url")

    >>> assert isinstance(replaypack_download_dir, Path)
    >>> assert isinstance(replaypack_unpack_dir, Path)
    >>> assert isinstance(replaypack_name, str)
    >>> assert isinstance(url, str)
    """

    # Downloading the replaypack:
    download_path = download_replaypack(
        destination_dir=replaypack_download_dir,
        replaypack_name=replaypack_name,
        replaypack_url=url,
    )

    # Unpacking the replaypack:
    _ = unpack_zipfile(
        destination_dir=replaypack_unpack_dir,
        subdir=replaypack_name,
        zip_path=download_path,
        n_workers=1,
    )

    return_path = Path(replaypack_unpack_dir, replaypack_name).resolve()

    return return_path
