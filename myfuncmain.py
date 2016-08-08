import nccm_python_unittest
import compliance
import unittest
import HTMLTestRunner
from nccm_python_unittest import TestCustomer
from compliance import TestZCompliance
from myfunc import TestCustomer

if __name__ == '__main__':
    test_classes_to_run = [TestCustomer]

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)