import logging
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import tests.test_utils.test_utils as test_utils


def suite():
    suite = unittest.TestSuite()
    workspace_dir = test_utils.get_workspace_dir()
    start_dir = os.path.join(workspace_dir, "tests/test_cases")
    suite = unittest.TestLoader().discover(
        start_dir=start_dir,
        pattern="dataset_utils_test.py",  # *_test.py
    )
    return suite


if __name__ == "__main__":

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    print(test_utils.get_workspace_dir())
    my_suite = suite()
    result = unittest.TextTestRunner(verbosity=2).run(my_suite)

    if result.wasSuccessful():
        exit(0)
    else:
        exit(1)
