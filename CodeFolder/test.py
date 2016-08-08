from selenium import webdriver

driver = webdriver.Firefox()

driver.get("http://automationpractice.com/")
driver.maximize_window()