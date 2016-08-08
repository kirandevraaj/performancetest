import nccm_python_unittest
import compliance
import unittest
import HTMLTestRunner
from nccm_python_unittest import TestCustomer
from device_import import TestDeviceImport
from custom_audit import TestCustomAudit
from  export_violations import Export_Violations
from export_violations_report import Export_Violations_Report

if __name__ == '__main__':
    test_classes_to_run = [TestCustomer,TestDeviceImport,TestCustomAudit,Export_Violations,Export_Violations_Report]
    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner(verbosity=2)
    results = runner.run(big_suite)