import unittest


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


class DownloadUtilsTest(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_download_replaypack(self):
        pass

    def test_download_and_unpack_replaypack(self):
        pass
