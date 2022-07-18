"""
    **Incorrect Usage Examples:**

    Passing a Python dictionary with missing or incorrect fields would result in a failure as follows:

    >>> camera_save_dict = {"WRONG_FIELD": 5}
    >>> details_object = CameraSave.from_dict(d=camera_save_dict)
    Traceback (most recent call last):
    ...
    KeyError: 'id'
"""
