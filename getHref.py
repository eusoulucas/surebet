
from selenium.webdriver.common.by import By
from betExtract import close_popup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from datetime import datetime

now = datetime.now()

def getHref(urls, driver):
    wait = WebDriverWait(driver, 10)
    for url in urls:
        driver.get(url)

        if 'betano' in url:
            # Closing the popup as soon as it shows 
            close_popup(By.XPATH, '/html/body/div[1]/div/section[2]/div[6]/div/div/div[1]/button', driver)
            # Find all the anchor tags on the page
            anchors = driver.find_elements(By.XPATH, "//a")
    
            # Extract the href values from the anchor tags
            hrefs = []
            with open("dados/sites/paginas_betano"+ now.strftime("%Y-%m-%d_%H-%M-%S") +".txt", "a") as file:
                for anchor in anchors:
                    try:
                        href = anchor.get_attribute("href")
                        if 'futebol' in href:
                            file.write(str(href) + "\n")
                        hrefs.append(href)
                    except:
                        anchors = wait.until(EC.presence_of_element_located((By.XPATH, "//a")))
                        continue
        elif 'sportingbet' in url:
            close_popup(By.CSS_SELECTOR, 'span.theme-ex', driver)
            # Find all the anchor tags on the page
            anchors = driver.find_elements(By.XPATH, "//a")

            # Extract the href values from the anchor tags
            hrefs = []
            with open("dados/sites/paginas_sb"+ now.strftime("%Y-%m-%d_%H-%M-%S") +".txt", "a") as file:
                for anchor in anchors:
                    try:
                        href = anchor.get_attribute("href")
                        if 'sports/futebol-4' in href:
                            file.write(str(href) + "\n")
                            hrefs.append(href)
                    except:
                        anchors = driver.find_elements(By.XPATH, "//a")
                        continue
        elif 'betfair' in url:
            close_popup(By.ID, 'onetrust-accept-btn-handler', driver)
            # Find all the anchor tags on the page
            anchors = driver.find_elements(By.XPATH, "//a")

            # Extract the href values from the anchor tags
            hrefs = []
            with open("dados/sites/paginas_betfair"+ now.strftime("%Y-%m-%d_%H-%M-%S") +".txt", "a") as file:
                for anchor in anchors:
                    try:
                        href = anchor.get_attribute("href")
                        if 'sport/football' in href:
                            file.write(str(href) + "\n")
                            hrefs.append(href)
                    except:
                        anchors = driver.find_elements(By.XPATH, "//a")
                        continue
    print('URLS EXTRAIDAS')
    driver.quit()