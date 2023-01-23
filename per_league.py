from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

# Create a new instance of Firefox
driver = webdriver.Firefox()

# Navigate to the website you want to scrape
driver.get("https://br.betano.com/sport/futebol/competicoes/brasil/10004/")

# Wait for the element with xpath 'xpath_selector' to be present on the page
wait = WebDriverWait(driver, 10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Closing the popup as soon as it shows
close_popup = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/section[2]/div[7]/div/div/div[1]/button')))
close_popup.click()

elements = driver.find_elements(By.CLASS_NAME, 'league-block')

# Extract the text of the elements
infos = [element.text for element in elements]

df = pd.DataFrame()
df_aux = pd.DataFrame()
info = []
aux = []
data = {}
dataG = {}

# Print the infos
for info in infos:
    aux = info.split('\n')
    aux.pop(0)
    try:
        aux.remove("Em local neutro")
    except:
        pass
    for i in range(0, len(aux), 19):
        print(str(aux) + "\n")
        try:    
            data = {
                "data": aux[i+0],
                "horario": aux[i+1],
                "time_casa": aux[i+2],
                "time_visitante": aux[i+3],
                "odds_casa": aux[i+5],
                "odds_empate": aux[i+6],
                "odds_visitante": aux[i+7],
                "total de gols+": aux[i+10],
                "total de gols-": aux[i+12],
                "ambas marcam sim": aux[i+15],
                "ambas marcam não": aux[i+17],
                }
        except Exception as e:
            print(e)

        df_aux = pd.json_normalize(data)
        df = pd.concat([df, df_aux])

# Printando o dataframe
print(df)
df.to_csv("dados/jogos_betanoBrasil.csv")

# Close the browser
driver.quit()