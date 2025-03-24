import os
import shutil
import unittest
import zipfile
from pathlib import Path

import pytest

from sc2_datasets.utils.zip_utils import (
    UnpackZipFileArguments,
    unpack_chunk,
    unpack_zipfile,
)
from tests.test_utils.test_utils import get_specific_asset_path, get_test_output_dir

"""
    **Incorrect Usage Examples:**

    >>> wrong_type_object = int(2)
    >>> unpack_chunk_object = unpack_chunk(
    ... unpack_arguments=wrong_type_object,
    ... )
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) ...

    If you don't set parameters or paste incorect parameters' type.
"""


@pytest.mark.minor
class ZipUtilsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.test_replaypack_name = "2022_TestReplaypack"
        cls.replaypack_zip_path = get_specific_asset_path(
            filename=cls.test_replaypack_name + ".zip"
        )

        cls.test_output_path = get_test_output_dir()
        cls.unpack_dir_path = Path(cls.test_output_path, "unpack").resolve()

        cls.unpacked = Path("not_existing_path").resolve()

    def setUp(self) -> None:
        if self.unpacked.exists():
            shutil.rmtree(path=str(self.unpacked))

    def test_unpack_zipfile_correct(self):
        path_to_unpacked = unpack_zipfile(
            destination_dir=self.unpack_dir_path,
            subdir=self.test_replaypack_name,
            zip_path=self.replaypack_zip_path,
            n_workers=1,
        )
        self.unpacked = Path(path_to_unpacked)

    def test_unpack_zipfile_incorrect(self):
        parameters = [-1, 0]
        for n_workers in parameters:
            with self.subTest(n_workers):
                with self.assertRaises(Exception):
                    _ = unpack_zipfile(
                        destination_dir=self.unpack_dir_path,
                        subdir=self.test_replaypack_name,
                        zip_path=self.replaypack_zip_path,
                        n_workers=n_workers,
                    )

    def test_unpack_chunk_correct(self):
        with zipfile.ZipFile(self.replaypack_zip_path, "r") as zip_file:
            file_list = zip_file.namelist()

        extraction_path = Path(self.unpack_dir_path, self.test_replaypack_name)
        if not extraction_path.exists():
            extraction_path.mkdir()

        arguments = UnpackZipFileArguments(
            chunk_id=0,
            zip_path=self.replaypack_zip_path,
            filenames=file_list,
            path_to_extract=extraction_path,
        )

        unpack_chunk(unpack_arguments=arguments)
