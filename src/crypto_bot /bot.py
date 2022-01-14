import telebot
import os
from loguru import logger


class Bot:

    def __init__(self):
        self.bot = telebot.TeleBot(os.environ['TELEGRAM_TOKEN'])
        self.send_welcome=self.bot.message_handler(commands=['start', 'help'])(self.send_welcome)
        self.bitcoin=self.bot.message_handler(commands=['Bitcoin','bitcoin','btc','BTC','Btc'])(self.bitcoin)
        self.ethereum=self.bot.message_handler(commands=['Ethereum','ethereum','eth','Eth','ETH'])(self.ethereum)


    def send_welcome(self,message):
        self.bot.reply_to(message, "Howdy, how are you doing?")
        logger.info('somebody starts bot')

    def bitcoin(self,message):
        btc = Crypto('btc')

        self.bot.reply_to(message, str(btc.price()))
        logger.info('bitcoin...')

    def ethereum(self,message):
        eth = Crypto('ethereum')

        self.bot.reply_to(message, str(eth.price()))
        logger.info('ethereum...')

    def echo_all(self,message):
        self.bot.reply_to(message, (message.text))


    def run(self):
        logger.info('Start bot')
        self.bot.infinity_polling()
        logger.info('Done')

if __name__ == "__main__":
    mybot=Bot()
    mybot.run()