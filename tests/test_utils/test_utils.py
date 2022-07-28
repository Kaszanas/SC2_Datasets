import logging
import os
from pathlib import Path
from typing import Tuple


def get_workspace_dir() -> str:
    """
    Getting path to the workspace where tests are run.
    This function is future proof for testing outsite of local environments.

    :return: Path to the workspace "ProcessingModule/"
    :rtype: str
    """
    logging.info(
        "Entered get_workspace_dir(), attempting to set\
            workspace_dir = os.environ.get('TEST_WORKSPACE')"
    )

    workspace_dir = os.environ.get("TEST_WORKSPACE")
    logging.info(
        f"Successfully set workspace_dir = {workspace_dir}, Attempting to return workspace_dir."
    )
    return workspace_dir


def get_assets_dir() -> str:
    """
    Getting path to the assets directory.

    :return: Returns path to the assets directory
    :rtype: str
    """
    logging.info(
        "Entered get_assets_dir(), calling workspace_dir = get_workspace_dir()"
    )
    workspace_dir = get_workspace_dir()
    logging.info(f"Successfully set workspace_dir = {workspace_dir}")

    input_dir = os.path.join(workspace_dir, "tests/test_files")
    logging.info(f"Successfully set input_dir = {input_dir}, returning input_dir")

    return input_dir


def get_test_output_dir() -> str:
    """
    Getting path to the tests output directory.

    :return: Returns a string representing the path to the test output directory.
    :rtype: str
    """
    logging.info(
        "Entered get_assets_dir(), calling workspace_dir = get_workspace_dir()"
    )
    workspace_dir = get_workspace_dir()
    logging.info(f"Successfully set workspace_dir = {workspace_dir}")

    test_output_dir = os.path.join(workspace_dir, "tests/test_output")
    logging.info(f"Successfully set input_dir = {test_output_dir}, returning input_dir")

    return test_output_dir


class AssetError(Exception):
    pass


def get_specific_asset(filename: str) -> str:

    """
    Getting a specific assets from assets directory referenced by its name.

    :raises AssetError: If the referenced asset does not exist this error is raised.
    :return: Returns path to a specific referenced asset.
    :rtype: str
    """

    asset_dir = get_assets_dir()
    list_image_dir = os.listdir(asset_dir)
    if filename in list_image_dir:
        return os.path.join(asset_dir, filename)
    else:
        raise AssetError("This asset doesn't exist.")


def get_setup_paths(test_replaypack_name: str = "2022_TestReplaypack") -> Tuple:
    """
    Helper function providing basic setup utilities for tests.

    :param test_replaypack_name: Specifies a test replaypack name which will be\
    used to find the .zip archive, defaults to "2022_TestReplaypack"
    :type test_replaypack_name: str, optional
    :return: Returns a tuple containing all of the required variables.
    :rtype: Tuple
    """
    replaypack_zip_path = get_specific_asset(filename=test_replaypack_name + ".zip")

    test_output_path = get_test_output_dir()
    unpack_dir_path = os.path.join(test_output_path, "unpack")
    download_dir_path = os.path.join(test_output_path, "download")

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
