from selenium import webdriver

# Create a new firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()


# Navigate to application home page
#driver.get("http://demo.magentocommerce.com/")


driver.get("http://127.0.0.1:8080/")
driver.find_element_by_id("logindefaultlogin1").click()

#driver.implicitly_wait(10)

driver.find_element_by_link_text("Devices").click()

devices = driver.find_element_by_class_name("group")
devices.find_element_by_tag_name("name")



#driver.quit()




