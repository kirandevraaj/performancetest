from selenium import webdriver
from config_parse import my_parse

url = my_parse("config_file.cfg")

driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get(url)

search_filed = driver.find_element_by_id("searchinput")
search_filed.clear()
search_filed.send_keys("getting started")
search_filed.submit()

searched = driver.find_element_by_class_name("searchresults")
print searched
items = searched.find_elements_by_tag_name("li")
for i in items:
    print i.text

