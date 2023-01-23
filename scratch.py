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

elements = driver.find_elements(By.XPATH, '/html/body/div[1]/div/section[2]/div[5]/div[2]/section/div[4]/div/div[1]/div[2]/table')

# Extract the text of the elements
infos = [element.text for element in elements]

# Print the infos
for info in infos:
    aux = info.split('\n')
    print(aux)

data = {
    "data": aux[0],
    "horario": aux[1],
    "time_casa": aux[2],
    "time_visitante": aux[3],
    str(aux[5]): {
        aux[2]: aux[6],
        'empate': aux[7],
        aux[3]: aux[8]
    },
    str(aux[9]): {
        aux[10]: aux[11],
        aux[12]: aux[13]
    },
    str(aux[14]): {
        aux[15]: aux[16],
        aux[17]: aux[18]
    },
}


import pandas as pd
df = pd.json_normalize(data)
#df = pd.DataFrame(data)
print(df)

# Close the browser
driver.quit()