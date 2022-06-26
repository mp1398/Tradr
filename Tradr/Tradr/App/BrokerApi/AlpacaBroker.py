from Lib.lib import *

import alpaca_trade_api as tradeapi
import requests
import json

"""
Alpaca Broker API module handles broker requests
that influence trading as a whole
"""


@dataclass
class Config:
    paper_api = None
    api = None
    secret_key: str
    api_key: str
    account_url: None
    paper_url: None
    base_url: None
    paper_secret_key: str
    paper_api_key: str
    paper_account_url: None

    def __init__(self):
        base_url = ''
        secret_key = ''
        api_key = ''
        paper_url = 'https://paper-api.alpaca.markets'
        paper_secret_key = '0p331rAnBMq86APQZsSYa8CPXCiJxVdASNfG1gQA'
        paper_api_key = 'PKV9XRB4FDO39ES68MJY'
        paper_account_url = "{}/v2/account/configurations".format(paper_url)
        account_url = "{}/v2/account/configurations".format(base_url)

        paper_api = tradeapi.REST(
            base_url=paper_url,
            key_id=paper_api_key,
            secret_key=paper_secret_key,
        )

        api = tradeapi.REST(
            base_url=base_url,
            key_id=api_key,
            secret_key=secret_key,
        )


class Handler:
    # sets account configuration to turn off shorting,
    # or selling more than we have in cash
    @staticmethod
    def shorting_switch(account_url, api_key, secret_key, switch_mode):
        my_data = {"shorting_enabled": switch_mode}
        r = requests.patch(account_url, headers={'APCA-API-KEY-ID': api_key,
                                                 'APCA-API-SECRET-KEY': secret_key},
                           data=json.dumps(my_data))
        print(r)

    @staticmethod
    def buy_security(position_symbol, market_value, paper):
        # check if the purchase is a live purchase or paper purchase
        # and format request
        if paper is True:
            api = Config.paper_api
        else:
            api = Config.api

        # try to buy security
        try:
            api.submit_order(
                symbol=position_symbol,
                notional=market_value,
                side='buy',
                type='market',
                time_in_force='day'
            )
            # append_bought_today_txt(position_symbol)
            print('bought ' + position_symbol)
            # time.sleep(.25)
        except Exception as e:
            print('couldn\'t buy security ' + position_symbol + ' , error')
            print(e)
            return None

    def sell_security(position_symbol, paper):
        # check if the purchase is a live purchase or paper purchase
        # and format request
        if paper is True:
            api_key = Config.paper_api_key
            secret_key = Config.paper_secret_key
            url = Config.paper_url
        else:
            api_key = Config.api_key
            secret_key = Config.secret_key
            url = Config.base_url

        # we try to close the position with a request instead of api call
        # calling a sell may trigger a short position
        try:
            close_position_url = url.format(position_symbol)
            requests.delete(close_position_url, headers={'APCA-API-KEY-ID': api_key,
                                                         'APCA-API-SECRET-KEY': secret_key})
            print('sold ' + position_symbol)
            # self.update_equity()
            # self.update_portfolio()
            # time.sleep(.25)
        except Exception as e:
            print('couldn\'t sell ' + position_symbol + ' , error')
            print(e)
            return None
