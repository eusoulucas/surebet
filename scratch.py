from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of Firefox
driver = webdriver.Firefox()

# Navigate to the website you want to scrape
driver.get("https://br.betano.com/sport/futebol/competicoes/brasil/10004/")

# Wait for the element with xpath 'xpath_selector' to be present on the page
wait = WebDriverWait(driver, 10)

# Closing the popup as soon as it shows
close_popup = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/section[2]/div[7]/div/div/div[1]/button')))
close_popup.click()