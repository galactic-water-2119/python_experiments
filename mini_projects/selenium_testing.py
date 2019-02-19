from  selenium import webdriver
from  selenium.common.exceptions import TimeoutException
#from  selenium.webdriver.common.by import By
#from  selenium.webdriver.support.ui import WebDriverWait
#from  selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Safari()
browser.get("https://tejesh.gitlab.io/flask-js-frontend/")

username = browser.find_element_by_id("username")
password = browser.find_element_by_id("password")
submit = browser.find_element_by_id("submit")

username.send_keys("tejesh")
password.send_keys("passwd")


submit.click()

'''
wait = WebDriverWait( browser, 5 )

try:
    page_loaded = wait.until_not(
        lambda browser: browser.current_url == login_page
    )
except TimeoutException:
    self.fail( "Loading timeout expired" )

    self.assertEqual(
browser.current_url,
correct_page,
msg = "Successful Login"
)
'''