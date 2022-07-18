import logging
import os


def get_workspace_dir() -> str:
    """
    Getting path to the workspace where tests are run. This function is future proof for testing outsite of local environments.

    :return: Path to the workspace "ProcessingModule/"
    :rtype: str
    """
    logging.info(
        "Entered get_workspace_dir(), attempting to set workspace_dir = os.environ.get('TEST_WORKSPACE')"
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

    logging.info(
        "Attempting to set input_dir = os.path.join(workspace_dir, 'test/test_files/single_replay')"
    )
    input_dir = os.path.join(workspace_dir, "test/test_files/single_replay")
    logging.info(f"Successfully set input_dir = {input_dir}, returning input_dir")

    return input_dir


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
