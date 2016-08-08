from selenium import webdriver
from config_parse import my_parse

driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()
url = my_parse("config_file.cfg")

driver.get(url)

driver.find_element_by_link_text("Register New Account").click()

firstname = driver.find_element_by_id("first_name")
lastname = driver.find_element_by_id("last_name")
phone = driver.find_element_by_id("phone_number")
emailaddress = driver.find_element_by_id("email_address")
username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")
confirmpass = driver.find_element_by_id("confirm_password")
register = driver.find_element_by_id("submit")

firstname.send_keys("raj")
lastname.send_keys("kumar")
phone.send_keys("9845012345")
emailaddress.send_keys("rajkumar@yahoo.com")
username.send_keys("rajkumar")
password.send_keys("password123")
confirmpass.send_keys("password123")
register.click()