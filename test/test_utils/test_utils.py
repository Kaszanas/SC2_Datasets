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

    workspace_dir = os.environ.get("DATASET_TEST_WORKSPACE")
    logging.info(
        f"Successfully set workspace_dir = {workspace_dir}, Attempting to return workspace_dir."
    )
    return workspace_dir
