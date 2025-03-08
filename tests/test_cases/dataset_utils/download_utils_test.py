"""
**Incorrect Usage Examples:**

>>> wrong_type_object = int(2)
>>> download_replaypack_object = download_replaypack(
...    destination_dir=wrong_type_object,
...    replaypack_name=replaypack_name,
...    replaypack_url=url)
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) ...

If you don't set parameters or paste incorect parameters' type.

If the destination directory is empty.

If the downloaded file has no .zip extension.

It may throw:

Exception: There is more than one file in the destination directory!

Exception: The file that was detected does not end with a .zip extension!
Wrong file was downloaded!
"""
