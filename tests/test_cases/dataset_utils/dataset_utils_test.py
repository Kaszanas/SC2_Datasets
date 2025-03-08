"""
**Incorrect Usage Examples:**

>>> wrong_type_object = int(2)
>>> load_replaypack_information_object = load_replaypack_information(
...        replaypack_name=wrong_type_object,
...        replaypack_path="replaypack_path",
...        unpack_n_workers=1)
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) ...

If you don't set parameters or paste incorect parameters' type.
"""
