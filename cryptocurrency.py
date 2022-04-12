from bs4 import BeautifulSoup 
import requests
import json
import os
import schedule
import time

#get cryptos prices
def bitcoin_price():
    html = requests.get("https://coinmarketcap.com/currencies/bitcoin/")
    soup = BeautifulSoup(html.text, 'html.parser')
    bitcoin = soup.find("div", attrs={'class':'priceValue'}).text

    return bitcoin

def ethereum_price():
    html = requests.get("https://coinmarketcap.com/currencies/ethereum/")
    soup = BeautifulSoup(html.text, 'html.parser')
    ethereum = soup.find("div", attrs={'class':'priceValue'}).text

    return ethereum

def bnb_price():
    html = requests.get("https://coinmarketcap.com/currencies/bnb/")
    soup = BeautifulSoup(html.text, 'html.parser')
    bnb = soup.find("div", attrs={'class':'priceValue'}).text

    return bnb

def xrp_price():
    html = requests.get("https://coinmarketcap.com/currencies/xrp/")
    soup = BeautifulSoup(html.text, 'html.parser')
    xrp = soup.find("div", attrs={'class':'priceValue'}).text

    return xrp

def solana_price():
    html = requests.get("https://coinmarketcap.com/currencies/solana/")
    soup = BeautifulSoup(html.text, 'html.parser')
    solana = soup.find("div", attrs={'class':'priceValue'}).text

    return solana

def cardano_price():
    html = requests.get("https://coinmarketcap.com/currencies/cardano/")
    soup = BeautifulSoup(html.text, 'html.parser')
    cardano = soup.find("div", attrs={'class':'priceValue'}).text

    return cardano

def monero_price():
    html = requests.get("https://coinmarketcap.com/currencies/monero/")
    soup = BeautifulSoup(html.text, 'html.parser')
    monero = soup.find("div", attrs={'class':'priceValue'}).text

    return monero

#create a dict
crypto_currency = {

    'CryptoCurrency' : {
        'Bitcoin' : bitcoin_price(),
        'Ethereum' : ethereum_price(),
        'BNB' : bnb_price(),
        'XRP' : xrp_price(),
        'Solana' : solana_price(),
        'Cardano' : cardano_price(),
        'Monero' : monero_price(),
    }

}

#create and update json file
def update_json():
    if not os.path.isdir(f'{os.getcwd()}\\crypto_currency.json'):
        crypto = open('crypto_currency.json', 'w')

    json.dump(crypto_currency, crypto)
    crypto.close()

#execute every 5 seconds to get real time pricing
schedule.every(5).seconds.do(update_json)

while True:
    schedule.run_pending()
    time.sleep(1)
