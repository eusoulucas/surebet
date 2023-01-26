from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

from time import sleep

def close_popup(wait, by, path):
    # Closing the popup as soon as it shows
    close_popup = wait.until(EC.presence_of_element_located((by, path)))
    close_popup.click()

def betano(url):
    # Navigate to the website you want to scrape
    driver.get(url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait for the element with xpath 'xpath_selector' to be present on the page
    wait = WebDriverWait(driver, 10)
    close_popup(wait, By.XPATH, '/html/body/div[1]/div/section[2]/div[6]/div/div/div[1]/button')
    
    elements = driver.find_elements(By.CLASS_NAME, 'events-list__grid__event') # ta buscando apenas o texto do header

    # Extract the text of the elements
    infos = [element.text for element in elements]
    
    # Creating the variables
    df = pd.DataFrame()
    df_aux = pd.DataFrame()
    aux = []
    data = {}
    dataG = {}

    # Print the infos
    for info in infos:
        aux = info.split('\n')
        print(aux)
        try:
            aux.remove("Em local neutro")
        except:
            pass
        try:    
            data = {
                "data": aux[0],
                "horario": aux[1],
                "time_casa": aux[2],
                "time_visitante": aux[3],
                "odds_casa": aux[4],
                "odds_empate": aux[5],
                "odds_visitante": aux[6],
                "total de gols+": aux[8],
                "total de gols-": aux[10],
                "ambas marcam sim": aux[12],
                "ambas marcam não": aux[14],
                }
        except Exception as e:
            print(e)

        df_aux = pd.json_normalize(data)
        df = pd.concat([df, df_aux])

    # Printando o dataframe
    print(df)
    df.to_csv("dados/jogos_betanoBrasil.csv")

def sporting_bet(url):
    # Navigate to the website you want to scrape
    driver.get(url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait for the element with xpath 'xpath_selector' to be present on the page
    wait = WebDriverWait(driver, 10)

    # O SITE ATENDE BEM AO USO DE CSS_SELECTOR COMO LOCALIZADOR
    # Closing the popup as soon as it shows
    sleep(5)
    close_popup(wait, By.CSS_SELECTOR, 'span.theme-ex')

    elements = driver.find_elements(By.CLASS_NAME,'grid-event-wrapper') # ta buscando apenas o texto do header

    # Extract the text of the elements
    infos = [element.text for element in elements]

    # Creating the variables
    df = pd.DataFrame()
    df_aux = pd.DataFrame()
    aux = []
    data = {}
    dataG = {}

    # Print the infos
    for info in infos:
        aux = info.split('\n')

        try:    
            data = {
                "time_casa": aux[0],
                "time_visitante": aux[1],
                "data_hora": aux[2],
                "odds_casa": aux[3],
                "odds_empate": aux[4],
                "odds_visitante": aux[5],
                "mais ou menos que": aux[6],
                "mais": aux[7],
                "mais": aux[8]
                }
        except Exception as e:
            print(e)

        df_aux = pd.json_normalize(data)
        df = pd.concat([df, df_aux])

    # Printando o dataframe
    print(df)
    df.to_csv("dados/jogos_sportingbetBrasil.csv")

# Create a new instance of Firefox
driver = webdriver.Firefox()

url_one = "https://br.betano.com/sport/futebol/ligas/10016o,193989r,10008o,181895o,16880r,16880o,16901r,16901o,16893r,16887r,16887o,16888o,16882o,16872r,183633r,16894r,17837r,17837o,17407r,200263r/"
betano(url_one)

url_two = "https://sports.sportingbet.com/pt-br/sports/futebol-4/aposta/brasil-33"
sporting_bet(url_two)

# Close the browser
driver.quit()