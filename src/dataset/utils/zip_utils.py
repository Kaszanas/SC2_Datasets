# Unpacks zip file at zip_path to a destination directory, into a subdirectory.
import os
import zipfile


def unpack_zipfile(destination_dir: str, subdir: str, zip_path: str) -> str:
    """
    Helper function that unpacks the content of .zip archive.

    :param destination_dir: Specifies the path where the .zip file will be extracted.
    :type destination_dir: str
    :param subdir: Specifies the subdirectory where the content will be extracted.
    :type subdir: str
    :param zip_path: Specifies the path to the zip file that will be extracted.
    :type zip_path: str
    :return: Returns a path to the extracted content.
    :rtype: str
    """
    with zipfile.ZipFile(zip_path, "r") as zip_file:
        path_to_extract = os.path.join(destination_dir, subdir)
        # Checking the existence of the extraction output directory
        # If it doesn't exist it will be created:
        if not os.path.exists(path_to_extract):
            os.makedirs(path_to_extract)
        zip_file.extractall(path_to_extract)

        return path_to_extract
