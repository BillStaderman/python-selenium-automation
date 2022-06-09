#2 Create locators + search strategy for these page elements of Amazon Sign in page:

# Amazon logo        Search by ID: <i class="a-icon a-icon-logo" role="img" aria-label="Amazon"></i>
# Continue button    Search by id="continue"
# Need help link     Search by partial link   //a[text()='Need help'

# Forgot your password link - NO link
# Other issues with Sign-In link - No link

# Create your Amazon account button    Search by id="continue"
# *Conditions of use link   Search by partial link text    //a[text()='Conditions of Use'
# *Privacy Notice link      Search by partial link text    //a[ctext()='Privacy Notice'

# 3 Create a test case for Help search

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:\\Users\\William\\Desktop\\python-selenium-automation\\chromedriver.exe')

driver.get('https://www.amazon.com/gp/help/customer/display.html') # Open Amazon Help page

search = driver.find_element(By.ID, 'hubHelpSearchInput')
search.clear()
search.send_keys('Cancel Order', Keys.ENTER) #  Use “Search Help Library” field and search for Cancel order:

# Verify that ‘Cancel Items or Orders’ text is present
actual_text = driver.find_element(By.XPATH, "//*[@id='a-page']/div[2]/div[2]/div[1]/div/div[2]/div/div/h1").text
expected_text = 'Cancel Items or Orders'
assert expected_text == actual_text, f'Expected (expected_text), but got (actual_text)'

driver.quit()
