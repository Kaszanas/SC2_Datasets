import unittest
import os
import shutil

from sc2egset_dataset.dataset.utils.zip_utils import unpack_zipfile

from tests.test_utils.test_utils import get_specific_asset, get_test_output_dir


"""
    **Incorrect Usage Examples:**

    >>> wrong_type_object = int(2)
    >>> unpack_chunk_object = unpack_chunk(
    ... zip_path=wrong_type_object,
    ... filenames="./directory/filenames",
    ... path_to_extract="./directory/path_to_extract")
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) ...

    If you don't set parameters or paste incorect parameters' type.



    **Incorrect Usage Examples:**

    Setting number of workers to zero or less than zero will result in failure.

    >>> unpack_zipfile_object = unpack_zipfile(
    ... destination_dir="./directory/destination_dir",
    ... subdir="./directory/subdir",)
    ... zip_path="./directory/zip_path",)
    ... n_workers=0)
    Traceback (most recent call last):
    ...
    Exception: Number of workers cannot be equal or less than zero!
"""


class ZipUtilsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:

        cls.test_replaypack_name = "2022_TestReplaypack"
        cls.replaypack_zip_path = get_specific_asset(
            filename=cls.test_replaypack_name + ".zip"
        )
        cls.test_output_path = get_test_output_dir()
        cls.unpack_dir_path = os.path.join(cls.test_output_path, "unpack")

    def tearDown(self) -> None:

        # Deleting the unpacked content after every test:
        shutil.rmtree(path=self.unpacked)

    def test_unpack_zipfile(self):

        self.unpacked = unpack_zipfile(
            destination_dir=self.unpack_dir_path,
            subdir=self.test_replaypack_name,
            zip_path=self.replaypack_zip_path,
            n_workers=1,
        )

    # def test_unpack_chunk(self):
    #     pass
