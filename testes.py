from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium import webdriver

from time import sleep

# FUNÇÕES
def waiting(path_type, value):
    # Putting WebDriverWait on a variable
    wait = WebDriverWait(driver, 10)

    # Wait for the page to be loaded
    if path_type == "CLASS_NAME":
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, value)))
    elif path_type == "XPATH":
        wait.until(EC.presence_of_element_located((By.XPATH, value)))


# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Navigate to the website
driver.get('https://br.betano.com/sport/futebol/competicoes/brasil/10004/')

# Closing pop-up
xpath = '/html/body/div[1]/div/section[2]/div[7]/div/div/div[1]/button'
waiting('XPATH', xpath)
close_button = driver.find_element(By.XPATH, xpath)
close_button.click()

sleep(5)# Just to check

# Close the browser
driver.quit()
