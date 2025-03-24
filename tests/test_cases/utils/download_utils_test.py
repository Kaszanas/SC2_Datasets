import os
import shutil
import unittest
from pathlib import Path

import pytest

from sc2_datasets.utils.download_utils import (
    download_replaypack,
)
from tests.settings_test import TEST_SYNTHETIC_REPLAYPACKS
from tests.test_utils.test_utils import get_test_output_dir


@pytest.mark.minor
class DownloadUtilsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # Defining basic paths used by the tests:
        cls.test_output_path = get_test_output_dir()
        cls.unpack_dir_path = Path(cls.test_output_path, "unpack").resolve()
        cls.download_dir_path = Path(cls.test_output_path, "download").resolve()

        # Initializing variables that have to be existing because of the setUp method:
        cls.unpacked = Path("not_existing_path").resolve()
        cls.downloaded = Path("not_existing_path").resolve()

    def setUp(self) -> None:
        if self.downloaded.exists():
            shutil.rmtree(path=str(self.downloaded))

        if self.unpacked.exists():
            shutil.rmtree(path=str(self.unpacked))

    def test_download_replaypack(self):
        self.downloaded = download_replaypack(
            destination_dir=self.download_dir_path,
            replaypack_name=TEST_SYNTHETIC_REPLAYPACKS[0][0],
            replaypack_url=TEST_SYNTHETIC_REPLAYPACKS[0][1],
        )
