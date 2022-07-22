import unittest


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
    def setUp(self) -> None:
        return super().setUp()

    def test_unpack_zipfile(self):
        pass

    def test_unpack_chunk(self):
        pass
