from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Launch Chrome browser
driver = webdriver.Chrome()

# Open Laravel login page
driver.get("http://127.0.0.1:8080/login")

# Fill in email and password fields
driver.find_element(By.NAME, "email").send_keys("test@example.com")
driver.find_element(By.NAME, "password").send_keys("password123")

# Submit the form
driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

# Wait a few seconds to observe result
time.sleep(5)

# Close browser
driver.quit()