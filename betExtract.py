from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import pandas as pd

from time import sleep

def close_popup(by, path, drv):
    wait = WebDriverWait(drv, 10)
    # Closing the popup as soon as it shows
    close_popup = wait.until(EC.presence_of_element_located((by, path)))
    close_popup.click()

def betano(url, drv):
    drv.get(url)
    drv.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Wait for the element with xpath 'xpath_selector' to be present on the page
    wait = WebDriverWait(drv, 30)
    df = pd.DataFrame()
    try:
        close_popup(By.XPATH, '/html/body/div[1]/div/section[2]/div[6]/div/div/div[1]/button', drv)
    except:
        pass
    try:
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'events-list__grid__event')))
        elements = drv.find_elements(By.CLASS_NAME, 'events-list__grid__event')
        infos = [element.text for element in elements]
        
        df = pd.DataFrame(infos)
        df = df[0].str.split("\n", expand=True)

        df.rename(columns={0:'data', 1:'hora', 2:'time_casa', 3:'time_visitante', 4:'vitoria_casa',
                    5:'empate', 6:'visitante_ganha', 8:'maisq25', 10:'menosq25'},
                inplace=True)
        df.to_csv("dados/jogos_betanoBrasil.csv", mode='a', index=False, header=False)
        drv.quit()
    except Exception as e:
        drv.quit()
        print(e)

def sporting_bet(url, drv):
    # Navigate to the website you want to scrape
    drv.get(url)
    drv.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # O SITE ATENDE BEM AO USO DE CSS_SELECTOR COMO LOCALIZADOR
    # Closing the popup as soon as it shows
    sleep(5)
    close_popup(By.CSS_SELECTOR, 'span.theme-ex', drv)

    elements = drv.find_elements(By.CLASS_NAME,'grid-event-wrapper') # ta buscando apenas o texto do header

    # Extract the text of the elements
    infos = [element.text for element in elements]

    # Creating the variables
    df = pd.DataFrame()
    df_aux = pd.DataFrame()
    aux = []
    data = {}
    print(infos)

    for info in infos:
        aux = info.split('\n')
        print(aux) 
        df_aux = pd.DataFrame(aux)
        df = pd.concat([df, df_aux], axis=1)

    df = df.transpose()
    df.rename(columns={0:'time_casa', 1:'time_visitante', 2:'dataHora', 3:'casaganha',
                        4:'empate', 5:'visitante_ganha', 6:'maisMenosQ',7:'maisQ',8:'menosQ'},
                inplace=True)
    print(df)
    df.to_csv("dados/jogos_sportingbetBrasil.csv")

def betfair(url, drv):
    # Navigate to the website you want to scrape
    drv.get(url)
    drv.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Closing the popup as soon as it shows
    sleep(5)
    close_popup(By.ID, 'onetrust-accept-btn-handler', drv)
    elements = drv.find_elements(By.XPATH, "//*[contains(@class, 'com-coupon-line-new-layout betbutton-layout avb-row avb-table')]")

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
'''

url = 'https://sports.sportingbet.com/pt-br/sports/futebol-4/aposta/brasil-33'
drv = webdriver.Firefox()

sporting_bet(url, drv)

drv.quit()
'''