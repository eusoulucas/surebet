from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from betExtract import close_popup
# Create a new instance of Firefox
driver = webdriver.Firefox()

urls = ['https://br.betano.com/sport/futebol/',
        'https://sports.sportingbet.com/pt-br/sports/futebol-4',
        'https://www.betfair.com/sport/football?action=browseAll&selectedTabType=COMPETITIONS&modules=multipickavb@1050']

for url in urls:
    driver.get(url)

    if 'betano' in url:
        # Closing the popup as soon as it shows 
        close_popup(By.XPATH, '/html/body/div[1]/div/section[2]/div[6]/div/div/div[1]/button', driver)
        # Find all the anchor tags on the page
        anchors = driver.find_elements(By.XPATH, "//a")

        # Extract the href values from the anchor tags
        hrefs = []
        with open("dados/sites/paginas_betano.txt", "a") as file:
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
    elif 'sportingbet' in url:
        close_popup(By.CSS_SELECTOR, 'span.theme-ex', driver)
        # Find all the anchor tags on the page
        anchors = driver.find_elements(By.XPATH, "//a")

        # Extract the href values from the anchor tags
        hrefs = []
        with open("dados/sites/paginas_sb.txt", "a") as file:
            for anchor in anchors:
                try:
                    href = anchor.get_attribute("href")
                    print(href)
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
        with open("dados/sites/paginas_betfair.txt", "a") as file:
            for anchor in anchors:
                try:
                    href = anchor.get_attribute("href")
                    print(href)
                    file.write(str(href) + "\n")
                    hrefs.append(href)
                except:
                    anchors = driver.find_elements(By.XPATH, "//a")
                    continue

    # Close the browser
driver.quit()