from ConfigParser import ConfigParser
from selenium import webdriver

parser = ConfigParser()
parser.read("config_file.cfg")

site_url = parser.get("home","url")
print site_url
#print parser.get("home","username")
#print parser.get("home","password")

driver = webdriver.Firefox()
#driver.get("https://pymotw.com/2/ConfigParser/")
driver.get(site_url)


