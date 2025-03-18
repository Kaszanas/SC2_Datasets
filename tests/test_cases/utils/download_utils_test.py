import os
import shutil
import unittest
from pathlib import Path

import pytest

from sc2_datasets.utils.download_utils import (
    download_and_unpack_replaypack,
    download_replaypack,
)
from tests.settings_test import TEST_SYNTHETIC_REPLAYPACKS
from tests.test_utils.test_utils import get_test_output_dir

"""
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


@pytest.mark.minor
class DownloadUtilsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # Defining basic paths used by the tests:
        cls.test_output_path = get_test_output_dir()
        cls.unpack_dir_path = os.path.join(cls.test_output_path, "unpack")
        cls.download_dir_path = os.path.join(cls.test_output_path, "download")

        # Initializing variables that have to be existing because of the setUp method:
        cls.unpacked = Path("not_existing_path")
        cls.downloaded = Path("not_existing_path")

    def setUp(self) -> None:
        if self.downloaded.exists():
            shutil.rmtree(path=self.downloaded.as_posix())

        if self.unpacked.exists():
            shutil.rmtree(path=self.unpacked.as_posix())

    def test_download_replaypack(self):
        self.downloaded = download_replaypack(
            destination_dir=self.download_dir_path,
            replaypack_name=TEST_SYNTHETIC_REPLAYPACKS[0][0],
            replaypack_url=TEST_SYNTHETIC_REPLAYPACKS[0][1],
        )

    def test_download_and_unpack_replaypack(self):
        self.unpacked = download_and_unpack_replaypack(
            replaypack_download_dir=self.download_dir_path,
            replaypack_unpack_dir=self.unpack_dir_path,
            replaypack_name=TEST_SYNTHETIC_REPLAYPACKS[0][0],
            url=TEST_SYNTHETIC_REPLAYPACKS[0][1],
        )
