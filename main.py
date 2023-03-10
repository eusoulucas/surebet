from selenium import webdriver

from utils.getHref import getHref

from utils.betExtract import *

import threading
import os

urls = ['https://br.betano.com/sport/futebol/',
        'https://sports.sportingbet.com/pt-br/sports/futebol-4',
        'https://www.betfair.com/sport/football?action=browseAll&selectedTabType=COMPETITIONS&modules=multipickavb@1050']

getHref(urls, webdriver.Firefox())

urls_betano = []
urls_betfair = []
urls_sb = []

def run_betano(urls):
    for url in urls:
        betano(url, webdriver.Firefox())

def run_betfair(urls):
    for url in urls:
        betfair(url, webdriver.Firefox())

def run_sb(urls):
    for url in urls:
        sporting_bet(url, webdriver.Firefox())

threads = []
for arquivo in os.listdir('dados/sites'):
    if 'betano' in arquivo:
        with open('dados/sites/{}'.format(arquivo), 'r') as file:
            for line in file:
                urls_betano.append(line)
        t = threading.Thread(target=run_betano, args=(urls_betano,))
        threads.append(t)
    
    elif 'betfair' in arquivo:
        with open('dados/sites/{}'.format(arquivo), 'r') as file:
            for line in file:
                urls_betfair.append(line)
        t = threading.Thread(target=run_betfair, args=(urls_betfair,))
        threads.append(t)

    elif 'sb' in arquivo:
        with open('dados/sites/{}'.format(arquivo), 'r') as file:
            for line in file:
                urls_sb.append(line)
        t = threading.Thread(target=run_sb, args=(urls_sb,))
        threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()
