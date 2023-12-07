import logging
import os
from pathlib import Path
from typing import Tuple


def get_workspace_dir() -> Path:
    """
    Getting path to the workspace where tests are run.
    This function is future proof for testing outsite of local environments.

    Returns
    -------
    Path
        Returns the path to the workspace.
    """

    logging.info(
        "Entered get_workspace_dir(), attempting to set \
        workspace_dir = os.environ.get('TEST_WORKSPACE')"
    )

    workspace_dir = Path(os.environ.get("TEST_WORKSPACE")).resolve()
    logging.info(
        f"Successfully set workspace_dir = {workspace_dir.as_posix()}, \
        Attempting to return workspace_dir."
    )
    return workspace_dir


def get_assets_dir() -> Path:
    """
    Getting path to the assets directory.

    Returns
    -------
    str
        Returns path to the assets directory.
    """

    logging.info(
        "Entered get_assets_dir(), calling workspace_dir = get_workspace_dir()"
    )
    workspace_dir = get_workspace_dir()
    logging.info(f"Successfully set workspace_dir = {workspace_dir}")

    input_dir = Path(workspace_dir, "tests/test_files").resolve()
    logging.info(
        f"Successfully set input_dir = {input_dir.as_posix()}, returning input_dir"
    )

    return input_dir


def get_test_output_dir() -> Path:
    """
    Getting path to the tests output directory.

    Returns
    -------
    Path
        Returns a string representing the path to the test output directory.
    """

    logging.info(
        "Entered get_assets_dir(), calling workspace_dir = get_workspace_dir()"
    )
    workspace_dir = get_workspace_dir()
    logging.info(f"Successfully set workspace_dir = {workspace_dir.as_posix()}")

    test_output_dir = Path(workspace_dir, "tests/test_output").resolve()
    logging.info(
        f"Successfully set input_dir = {test_output_dir.as_posix()}, returning input_dir"
    )

    return test_output_dir


class AssetError(Exception):
    pass


def get_specific_asset_path(filename: str) -> Path:
    """
    Getting a specific assets from assets directory referenced by its name.

    Parameters
    ----------
    filename : str
        Filename for the asset for which the path should be retrieved.

    Returns
    -------
    Path
        Returns path to a specific referenced asset.

    Raises
    ------
    AssetError
        If the referenced asset does not exist this error is raised.
    """

    asset_dir = get_assets_dir()
    list_image_dir = os.listdir(asset_dir)
    if not filename in list_image_dir:
        raise AssetError("This asset doesn't exist.")

    return Path(asset_dir, filename)


def get_setup_paths(test_replaypack_name: str = "2022_TestReplaypack") -> Tuple:
    """
    Helper function providing basic setup utilities for tests.

    Parameters
    ----------
    test_replaypack_name : str, optional
        Specifies a test replaypack name which will be \
        used to find the .zip archive, by default "2022_TestReplaypack"

    Returns
    -------
    Tuple
        Returns a tuple containing all of the required variables.
    """

    replaypack_zip_path = get_specific_asset_path(
        filename=test_replaypack_name + ".zip"
    )

    test_output_path = get_test_output_dir()
    unpack_dir_path = Path(test_output_path, "unpack").resolve()
    download_dir_path = Path(test_output_path, "download").resolve()

    # Initializing the unpacked where it should be:
    unpacked = Path(unpack_dir_path, test_replaypack_name)
    download = Path(download_dir_path, test_replaypack_name)

    return (
        test_replaypack_name,
        replaypack_zip_path,
        unpack_dir_path,
        download_dir_path,
        unpacked,
        download,
    )
