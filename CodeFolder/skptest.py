import unittest
import sys
import os
import platform
print "windows platform = ", platform.platform()
print sys.platform

class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping\n")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(platform.platform() == "Windows-7-6.1.7601-SP1",
                     "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        print "This test was not skipped, because the platform is windows "

suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)