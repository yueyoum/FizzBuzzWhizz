import unittest
from test_mixin import FBWTest

from fbw_ver1 import run

class Test(unittest.TestCase, FBWTest):
    FBWTest.fbw_func = staticmethod(run)


if __name__ == '__main__':
    unittest.main()


