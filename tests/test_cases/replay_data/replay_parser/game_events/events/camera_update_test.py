"""
    **Incorrect Usage Examples:**

    Passing a Python dictionary with missing or incorrect fields would result in a failure as follows:

    >>> camera_update_dict = {"WRONG_FIELD": 5}
    >>> details_object = CameraUpdate.from_dict(d=camera_update_dict)
    Traceback (most recent call last):
    ...
    KeyError: 'distance'
"""
