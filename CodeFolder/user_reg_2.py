from selenium import webdriver
from config_parse import my_parse
import csv
import time

driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()
url = my_parse("config_file.cfg")

#driver.get(url)
#driver.find_element_by_link_text("Register New Account").click()

def csvtodict(file):
    with open(file,'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print row
            driver.get(url)
            driver.find_element_by_link_text("Register New Account").click()
            driver.find_element_by_id("first_name").send_keys(row.get("firstname"))
            driver.find_element_by_id("last_name").send_keys(row.get("lastname"))
            driver.find_element_by_id("phone_number").send_keys(row.get("phone"))
            driver.find_element_by_id("email_address").send_keys(row.get("emailaddress"))
            driver.find_element_by_id("username").send_keys(row.get("username"))
            #print row["password"]
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("password").send_keys(row.get("password"))
            #time.sleep(5)
            #print row["confirmpass"]
            driver.find_element_by_id("confirm_password").clear()
            #time.sleep(5)
            driver.find_element_by_id("confirm_password").send_keys(row.get("confirmpass"))
            driver.find_element_by_id("submit").click()

csvtodict("userdetails.csv")