from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("http://automationpractice.com/index.php")
search_field = driver.find_element_by_id("search_query_top")
search_field.clear()
search_field.send_keys("dress")
search_field.submit()

shorts = driver.find_elements_by_xpath('//*[@id="center_column"]/ul')
#products = shorts.find_elements_by_tag_name("li")
print "Found " + str(len(shorts)) + " products:"

for item in shorts:
    print item.text
    print '-' * 200

driver.quit()