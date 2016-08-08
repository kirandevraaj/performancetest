import unittest
from selenium import webdriver

class SearchTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://www.gsmarena.com/")

    def test_search_nokia_phones(self):
        self.search_field = self.driver.find_element_by_name("sName")
        self.search_field.clear()
        self.search_field.send_keys("Nokia")
        self.search_field.submit()

        produts = self.driver.find_elements_by_xpath('//*[@id="review-body"]/div/ul')
        print produts
        self.assertEqual(1,len(produts))

    def test_search_samsung_phones(self):
        self.search_field = self.driver.find_element_by_name("sName")
        self.search_field.clear()
        self.search_field.send_keys("Samsung")
        self.search_field.submit()
        produts = self.driver.find_elements_by_xpath('//*[@id="review-body"]/div/ul')
        print produts
        self.assertEqual(1,len(produts))


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
