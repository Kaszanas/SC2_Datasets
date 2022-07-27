# Unpacks zip file at zip_path to a destination directory, into a subdirectory.
import logging
import os
import zipfile
import math

from concurrent.futures import ProcessPoolExecutor
from typing import List

from tqdm import tqdm


# REVIEW: Check this:
def unpack_chunk(zip_path: str, filenames: List[str], path_to_extract: str):
    """
    Helper function for unpacking a chunk of files from an archive

    :param zip_path: Specifies the path to the archive file that will be extracted.
    :type zip_path: str
    :param filenames: specifies a list of the filenames which are within the archive
    and will be extracted.
    :type filenames: List[str]
    :param path_to_extract: Specifies the path to which the files will be extracted to.
    :type path_to_extract: str

    **Correct Usage Examples:**

    The use of this method is intended to extract a zipfile from the .zip file.

    You should set every parameter, zip_path, filenames and path_to_extract.

    May help you to work with dataset.

    The parameters should be set as in the example below.

    >>> unpack_chunk_object = unpack_chunk(
    ... zip_path="./directory/zip_path",
    ... filenames="./directory/filenames",
    ... path_to_extract="./directory/path_to_extract")

    >>> assert isinstance(zip_path, str)
    >>> assert all(isinstance(filename, str) for filename in filenames)
    >>> assert isinstance(path_to_extract, str)
    """

    with zipfile.ZipFile(zip_path, "r") as zip_file:
        for filename in filenames:
            try:
                zip_file.extract(filename, path_to_extract)
            except zipfile.error as e:
                logging.error(
                    f"zipfile error was raised: {e}",
                    exc_info=True,
                )


# REVIEW: Check this:
def unpack_zipfile(
    destination_dir: str, subdir: str, zip_path: str, n_workers: int
) -> str:
    """
    Helper function that unpacks the content of .zip archive.

    :param destination_dir: Specifies the path where the .zip file will be extracted.
    :type destination_dir: str
    :param subdir: Specifies the subdirectory where the content will be extracted.
    :type subdir: str
    :param zip_path: Specifies the path to the zip file that will be extracted.
    :type zip_path: str
    :param n_workers: Specifies the number of workers that will be used for unpacking the archive.
    :type n_workers: int
    :return: Returns a path to the extracted content.
    :rtype: str

    **Correct Usage Examples:**

    The use of this method is intended to extract a zipfile.

    You should set every parameter, destination, subdir, zip_path and n_workers.

    May help you to work with dataset.

    The parameters should be set as in the example below.

    >>> unpack_zipfile_object = unpack_zipfile(
    ... destination_dir="./directory/destination_dir",
    ... subdir="./directory/subdir",
    ... zip_path="./directory/zip_path",
    ... n_workers=1)

    >>> assert isinstance(destination_dir, str)
    >>> assert isinstance(subdir, str)
    >>> assert isinstance(zip_path, str)
    >>> assert isinstance(n_workers, int)
    >>> assert n_workers >= 1
    """

    if n_workers <= 0:
        raise Exception("Number of workers cannot be equal or less than zero!")

    file_list: List[str] = []
    path_to_extract = os.path.join(destination_dir, subdir)
    with zipfile.ZipFile(zip_path, "r") as zip_file:
        # Checking the existence of the extraction output directory
        # If it doesn't exist it will be created:
        if not os.path.exists(path_to_extract):
            os.makedirs(path_to_extract)

        file_list = zip_file.namelist()

    chunksize = math.ceil(len(file_list) / n_workers)

    with ProcessPoolExecutor(n_workers) as exe:
        for index in tqdm(
            range(0, len(file_list), chunksize),
            desc=f"Extracting {os.path.basename(destination_dir)}: ",
        ):
            filenames = file_list[index : (index + chunksize)]
            _ = exe.submit(unpack_chunk, zip_path, filenames, path_to_extract)

    return path_to_extract
