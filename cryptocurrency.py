from bs4 import BeautifulSoup 
import requests
import json
import os
import time

cryptos = ['bitcoin', 'ethereum', 'xrp', 'solana', 'cardano', 'monero']

crypto_currency = {

    'CryptoCurrency' : {
    
    }
}

def crypto_price(crp):
    html = requests.get(f"https://coinmarketcap.com/currencies/{crp}/")
    soup = BeautifulSoup(html.text, 'html.parser')
    crypt = soup.find("div", attrs={'class':'priceValue'}).text

    crypto_currency['CryptoCurrency'][crp] = crypt

for crp in cryptos:
    crypto_price(crp)

#create and update json file
def update_json():
    if not os.path.isdir(f'{os.getcwd()}\\crypto_currency.json'):
        crypto = open('crypto_currency.json', 'w')

    json.dump(crypto_currency, crypto)
    crypto.close()

if __name__ == '__main__': update_json()