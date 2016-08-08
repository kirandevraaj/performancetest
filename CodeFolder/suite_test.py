import unittest
from searchtest2 import SearchTest
import HTMLTestRunner
import os

dir = os.getcwd()


from findtest import HomePageTest
from searchtest2 import SearchTest

search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTest)
home_page_test = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

smoke_tests = unittest.TestSuite([search_tests,home_page_test])

#unittest.TextTestRunner(verbosity=2).run(smoke_tests)

outfile = open(dir + "\SmokeTestReport.html",'w')

runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,title="Test Report",description='Smoke Tests')

runner.run(smoke_tests)

self.assertTrue(search_button.is_enabled())