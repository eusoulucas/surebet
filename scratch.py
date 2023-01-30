from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

from time import sleep

def close_popup(wait, by, path):
    # Closing the popup as soon as it shows
    close_popup = wait.until(EC.presence_of_element_located((by, path)))
    close_popup.click()

def betano(url):
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

    # Print the infos
    for info in infos:
        aux = info.split('\n')
        if len(aux) > 16:
            del aux[4]
        df_aux = pd.DataFrame(aux)
        df = pd.concat([df, df_aux], axis=1)

    # Printando o dataframe
    df = df.transpose()
    df.rename(columns={0:'data', 1:'hora', 2:'time_casa', 3:'time_visitante',
                        4:'casa_ganha', 5:'empate', 6:'visitante_ganha',8:'mais25',
                        10:'menos25', 12:'ambosmarcaMSIM', 14:'ambosmarcaMNAO'},
                inplace=True)
    df.drop([7,9,11,13,15], axis='columns', inplace=True)
    
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

    print(infos)

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
    #print(df)
    df.to_csv("dados/jogos_sportingbetBrasil.csv")

def betfair(url):
    # Navigate to the website you want to scrape
    driver.get(url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait for the element with xpath 'xpath_selector' to be present on the page
    wait = WebDriverWait(driver, 10)

    # Closing the popup as soon as it shows
    sleep(5)
    close_popup(wait, By.ID, 'onetrust-accept-btn-handler')
    elements = driver.find_elements(By.XPATH, "//*[contains(@class, 'com-coupon-line-new-layout betbutton-layout avb-row avb-table')]")

    # Extract the text of the elements
    infos = [element.text for element in elements]
    
    df_aux = pd.DataFrame()
    df = pd.DataFrame()

    for info in infos:
        inf = info.split('\n')   
        print(inf) 
        if len(inf) == 8:
            inf.insert(6, 'Não sera')
        df_aux = pd.DataFrame(inf)
        df = pd.concat([df, df_aux], axis=1)#.pivot_table(values=[0,])

    df = df.transpose()
    df.rename(columns={0:'data_hora', 1:'maisq25', 2:'menosq25', 3:'casaganha',
                        4:'empate', 5:'visitante_ganha', 6:'Ao vivo',7:'time_casa',8:'time_visitante'},
                inplace=True)
    print(df)
    df.to_csv("dados/jogos_BetFair.csv")

# Create a new instance of Firefox
driver = webdriver.Firefox()

urls_betano = ['https://br.betano.com/sport/futebol/brasil/campeonato-paulista-serie-a1/16901/',
                'https://br.betano.com/sport/futebol/inglaterra/efl-cup/10215/',
                'https://br.betano.com/sport/futebol/alemanha/bundesliga/216/',
                'https://br.betano.com/sport/futebol/italia/serie-a/1635/',
                'https://br.betano.com/sport/futebol/espanha/laliga/5/']

for url in urls_betano:
    betano(url)

urls_sb = ["https://sports.sportingbet.com/pt-br/sports/futebol-4/aposta/brasil-33"]
for url in urls_sb:
    sporting_bet(url)

urls_bf = ["https://www.betfair.com/sport/football/brasil-paulista-serie-a1/2490975"]
for url in urls_bf:
    betfair(url)

# Close the browser
driver.quit()