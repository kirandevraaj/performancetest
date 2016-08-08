from selenium import webdriver

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

# navigate to the application home page
driver.get("http://www.gsmarena.com/")

# get the search textbox
search_field = driver.find_element_by_name("sName")
search_field.clear()

# enter search keyword and submit
search_field.send_keys("Nokia")
search_field.submit()

# get all the anchor elements which have product names displayed
# currently on result page using find_elements_by_xpath method
products = driver.find_elements_by_xpath('//*[@id="review-body"]/div/ul')
print products


# get the number of anchor elements found
print "Found " + str(len(products)) + " products:"

#Nokia = []
# iterate through each anchor element and print the text that is # name of the product
for product in products:
    print product

# close the browser window
#driver.quit()