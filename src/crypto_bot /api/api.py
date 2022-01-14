import requests
import json



class Crypto:

    def __init__(self,name):
        self.name = name
        api = 'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=3&sortBy=market_cap&sortType=desc&convert=USD&cryptoType=all&tagType=all&audited=false'

        self.response = requests.get(api)
        self.data= self.response.json()

    def price(self):

        if self.name in ['Bitcoin','bitcoin','btc','BTC','Btc']:
            price_ = self.data['data']['cryptoCurrencyList'][0]['quotes'][0]['price']
            time_ = self.data['data']['cryptoCurrencyList'][0]['quotes'][0]['lastUpdated']
            return f'lastUpdated:{time_}\nPrice: {price_}'

        elif self.name in ['Ethereum','ethereum','eth','Eth','ETH']:
            price_ = self.data['data']['cryptoCurrencyList'][1]['quotes'][0]['price']
            time_ = self.data['data']['cryptoCurrencyList'][1]['quotes'][0]['lastUpdated']
            return f'lastUpdated:{time_}\nPrice: {price_}'