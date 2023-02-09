from selenium import webdriver

from getHref import getHref

import concurrent.futures

from betExtract import *

import threading
import os

urls = ['https://br.betano.com/sport/futebol/',
        'https://sports.sportingbet.com/pt-br/sports/futebol-4',
        'https://www.betfair.com/sport/football?action=browseAll&selectedTabType=COMPETITIONS&modules=multipickavb@1050']

options = webdriver.FirefoxOptions()
#options.add_argument('--headless')
browser = webdriver.Firefox(options=options)

thread_gethref = threading.Thread(target=getHref, args=(urls, browser,))
thread_gethref.start()

urls_betano = []
urls_betfair = []
urls_sb = []

def run_betano(urls):
    for url in urls:
        betano(url, browser)

def run_betfair(urls):
    for url in urls:
        betfair(url, browser)

def run_sb(urls):
    for url in urls:
        sporting_bet(url, browser)

threads = []

def run_all_threads(urls, function):
    for url in urls:
        t = threading.Thread(target=function, args=(url,))
        threads.append(t)
        t.start()

for arquivo in os.listdir('dados/sites'):
    if 'betano' in arquivo:
        with open('dados/sites/{}'.format(arquivo), 'r') as file:
            for line in file:
                urls_betano.append(line)

    elif 'betfair' in arquivo:
        with open('dados/sites/{}'.format(arquivo), 'r') as file:
            for line in file:
                urls_betfair.append(line)

    elif 'sb' in arquivo:
        with open('dados/sites/{}'.format(arquivo), 'r') as file:
            for line in file:
                urls_sb.append(line)

# Limit number of concurrent threads to 2
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    if urls_betano:
        executor.submit(run_betano, urls_betano)
    if urls_betfair:
        executor.submit(run_betfair, urls_betfair)
    if urls_sb:
        executor.submit(run_sb, urls_sb)