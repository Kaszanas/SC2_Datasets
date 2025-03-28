# Unpacks zip file at zip_path to a destination directory, into a subdirectory.
import logging
import math
import zipfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import List

from tqdm import tqdm


class UnpackZipFileArguments:
    """
    Helper class for passing arguments to a multi-threaded unpacking function.

    Parameters
    ----------
    zip_path : Path
        Specifies the path to the archive file that will be extracted.
    filenames : List[str]
        Specifies a list of the filenames which are within the archive\
        and will be extracted.
    path_to_extract : Path
        Specifies the path to which the files will be extracted to.
    """

    def __init__(
        self,
        chunk_id: int,
        zip_path: Path,
        filenames: List[str],
        path_to_extract: Path,
    ):
        self.chunk_id = chunk_id
        self.zip_path = zip_path
        self.filenames = filenames
        self.path_to_extract = path_to_extract


# REVIEW: Check this:
def unpack_chunk(
    unpack_arguments: UnpackZipFileArguments,
) -> None:
    """
    Helper function for unpacking a chunk of files from an archive.

    Parameters
    ----------
    zip_path : str
        Specifies the path to the archive file that will be extracted.
    filenames : List[str]
        Specifies a list of the filenames which are within the archive\
        and will be extracted.
    path_to_extract : str
        Specifies the path to which the files will be extracted to.

    Examples
    --------
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

    with zipfile.ZipFile(unpack_arguments.zip_path, "r") as zip_file:
        for filename in tqdm(
            unpack_arguments.filenames,
            desc=f"W {unpack_arguments.chunk_id} Extracting from {unpack_arguments.zip_path.name}:",
            unit="file",
        ):
            # Check if the file already exists:
            maybe_unpacked_file = Path(
                unpack_arguments.path_to_extract, filename
            ).resolve()
            if maybe_unpacked_file.exists():
                continue

            try:
                zip_file.extract(member=filename, path=unpack_arguments.path_to_extract)
            except zipfile.error as e:
                logging.error(
                    f"zipfile error was raised: {e}",
                    exc_info=True,
                )


# REVIEW: Check this:
def unpack_zipfile(
    destination_dir: Path,
    subdir: str,
    zip_path: Path,
    n_workers: int,
) -> Path:
    """
    Helper function that unpacks the content of .zip archive.

    Parameters
    ----------
    destination_dir : Path
        Specifies the path where the .zip file will be extracted.
    subdir : str
        Specifies the subdirectory where the content will be extracted.
    zip_path : Path
        Specifies the path to the zip file that will be extracted.
    n_workers : int
        Specifies the number of workers that will be used for unpacking the archive.

    Returns
    -------
    str
        Returns a path to the extracted content.

    Raises
    ------
    Exception
        Raises an exception if the number of workers is less or equal to zero.

    Examples
    --------
    The use of this method is intended to extract a zipfile.

    You should set every parameter, destination, subdir, zip_path and n_workers.

    May help you to work with dataset.

    The parameters should be set as in the example below.

    >>> from pathlib import Path
    >>> unpack_zipfile_object = unpack_zipfile(
    ... destination_dir=Path("./directory/destination_dir").resolve(),
    ... subdir="./directory/subdir",
    ... zip_path=Path("./directory/zip_path").resolve,
    ... n_workers=1)

    >>> assert isinstance(destination_dir, Path)
    >>> assert isinstance(subdir, str)
    >>> assert isinstance(zip_path, Path)
    >>> assert isinstance(n_workers, int)
    >>> assert n_workers >= 1
    """

    if n_workers <= 0:
        raise Exception("Number of workers cannot be equal or less than zero!")

    file_list: List[str] = []
    path_to_extract = Path(destination_dir, subdir).resolve()
    if not path_to_extract.exists():
        path_to_extract.mkdir(parents=True)

    file_list = []
    with zipfile.ZipFile(zip_path, "r") as zip_file:
        # Checking the existence of the extraction output directory
        # If it doesn't exist it will be created:
        file_list = zip_file.namelist()

    chunksize = math.ceil(len(file_list) / n_workers)

    # Get chunks to unpack with threads:
    file_chunks = []
    for index in range(0, len(file_list), chunksize):
        file_chunks.append(file_list[index : (index + chunksize)])

    # Get the arguments for the unpacking function:
    unpack_arguments = []
    for index, chunk in enumerate(file_chunks):
        unpack_arguments.append(
            UnpackZipFileArguments(
                chunk_id=index,
                zip_path=zip_path,
                filenames=chunk,
                path_to_extract=path_to_extract,
            )
        )

    with ThreadPoolExecutor(
        max_workers=n_workers,
        initializer=tqdm.set_lock,
        initargs=(tqdm.get_lock(),),
    ) as exe:
        _ = exe.map(unpack_chunk, unpack_arguments)

    return path_to_extract
