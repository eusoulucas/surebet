from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of Firefox
driver = webdriver.Firefox()

url = 'https://br.betano.com/sport/futebol/'
driver.get(url)

# Wait for the element with xpath 'xpath_selector' to be present on the page
wait = WebDriverWait(driver, 10)

# Closing the popup as soon as it shows 
close_popup = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/section[2]/div[6]/div/div/div[1]/button')))
close_popup.click()

# Find all the anchor tags on the page
anchors = driver.find_elements(By.XPATH, "//a")

# Extract the href values from the anchor tags
hrefs = []
with open("dados/sites.txt", "a") as file:
    for anchor in anchors:
        try:
            href = anchor.get_attribute("href")
            if 'futebol' in href:
                print(href)
                file.write(str(href) + "\n")
            hrefs.append(href)
        except:
            anchors = driver.find_elements(By.XPATH, "//a")
            continue

# Close the browser
driver.quit()