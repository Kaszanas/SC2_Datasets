"""
    **Incorrect Usage Examples:**

    Passing a Python dictionary with missing or incorrect fields would result in a failure as follows:

    >>> details_dict = {"WRONG_FIELD": "Faster"}
    >>> details_object = Details.from_dict(d=details_dict)
    Traceback (most recent call last):
    ...
    KeyError: 'gameSpeed'
"""
