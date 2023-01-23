import os

from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxDriver
from selenium.webdriver.common.by import By

# Retrieve login credentials from environment variables
username = os.environ.get("BET365_USERNAME")
password = os.environ.get("BET365_PASSWORD")

# Create a new instance of the Firefox driver
driver = FirefoxDriver()

# Navigate to the website
driver.get("https://br.betano.com/sport/futebol/competicoes/brasil/10004/")

# Provide your login credentials
username = driver.find_element(By.XPATH, "//input[@name='username']")
password = driver.find_element(By.XPATH, "//input[@name='password']")
username.send_keys("YOUR_USERNAME")
password.send_keys("YOUR_PASSWORD")

# Submit the form
driver.find_element_by_class_name("submit").submit()

# Extract data from the page
data = driver.find_elements_by_xpath('//div')
print(data)

# Close the browser
driver.quit()