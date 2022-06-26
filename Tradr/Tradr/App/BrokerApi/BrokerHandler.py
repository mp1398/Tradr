import alpaca_trade_api as tradeapi
import requests
import json
import time
from BrokerApi.BrokerConfig import *
from abc import ABC, abstractmethod


class BrokerHandler(ABC):

    @abstractmethod
    def buy_security(self, position_symbol, market_value):
        pass

    @abstractmethod
    def sell_security(self, position_symbol):
        pass


# change all hardcoded paper urls to fetched data, that determines if paper or live is used
class AlpacaHandler(BrokerHandler):
    def __init__(self):
        self.api = tradeapi.REST(
            base_url=BrokerConfig.AlpacaBroker.paper_url,
            key_id=BrokerConfig.AlpacaBroker.paper_api_key,
            secret_key=BrokerConfig.AlpacaBroker.paper_secret_key,
        )
        self.account = self.api.get_account()

    def buy_security(self, position_symbol, market_value):
        try:
            self.api.submit_order(
                symbol=position_symbol,
                notional=market_value,
                side='buy',
                type='market',
                time_in_force='day'
            )
            self.append_bought_today_txt(position_symbol)
            print('bought ' + position_symbol)
            time.sleep(.25)
        except Exception as e:
            print('couldn\'t buy security ' + position_symbol + ' , error')
            print(e)
            # HomePage.activity_log.print('couldn\'t buy security ' + position_symbol + ' , error')
            # HomePage.activity_log.print(e)
            return None

    def sell_security(self, position_symbol):
        try:
            close_position_url = 'https://paper-api.alpaca.markets/v2/positions/{0}'.format(position_symbol)
            requests.delete(close_position_url,
                            headers={'APCA-API-KEY-ID': BrokerConfig.AlpacaBroker.paper_api_key,
                                     'APCA-API-SECRET-KEY': BrokerConfig.AlpacaBroker.paper_secret_key})
            print('sold ' + position_symbol)
            time.sleep(.25)
        except Exception as e:
            print('couldn\'t sell security ' + position_symbol + ' , error')
            print(e)
            # HomePage.activity_log.print('couldn\'t sell security ' + position_symbol + ' , error')
            # HomePage.activity_log.print(e)
            return None

    @staticmethod
    def turn_off_shorting():
        my_data = {"shorting_enabled": False}
        r = requests.patch(BrokerConfig.AlpacaBroker.paper_account_url, headers={
            'APCA-API-KEY-ID': BrokerConfig.AlpacaBroker.paper_api_key,
            'APCA-API-SECRET-KEY': BrokerConfig.AlpacaBroker.paper_secret_key},
                           data=json.dumps(my_data))
        print(r)
        # if(r == "485"):
        #  HomePage.activity_log.print(r + " success")

    def fetch_day_trading_count(self):
        return self.account.daytrade_count

    def fetch_api_portfolio_list(self):
        return self.api.list_positions()

    @staticmethod
    def append_bought_today_txt(security):
        with open('bought_today_alpaca.txt', 'a') as f:
            f.write(security)
            f.write("\n")

    @staticmethod
    def clear_bought_today_txt():
        with open('bought_today_alpaca.txt', 'r+') as f:
            f.truncate(0)
        print("bought today list cleared")

    @staticmethod
    def if_bought_today(symbol):
        # we need to strip the '\n' before iterating through
        # we iterate onc
        # read only file
        with open('bought_today_alpaca.txt', 'r') as bought_today_txt:
            for line in bought_today_txt:
                list_symbol = line.rstrip("\n")
                if symbol == list_symbol:
                    return True

        return False


class IKBRHandler(BrokerHandler):
    def buy_security(self, position_symbol, market_value):
        pass

    def sell_security(self, position_symbol):
        pass
