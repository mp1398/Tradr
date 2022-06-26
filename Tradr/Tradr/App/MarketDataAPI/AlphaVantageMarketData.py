from Lib.lib import *
import requests

"""
We process Alpha Vantage API market data requests here
"""


@dataclass
class Config:
    av_api_key: str = 'NYBHZ3SFQHRJOCSV'


class Handler:

    @staticmethod
    def indicator_request(indicator, ticker, time_interval, time_period, series_type):
        url = f'https://www.alphavantage.co/query?function={indicator}&symbol={ticker}&' \
              f'interval={time_interval}&time_period={time_period}&series_type={series_type}&' \
              f'apikey={Config.av_api_key}'

        r = requests.get(url)
        data = r.json()

        return data


"""
alpha_vantage_config = Config()
alpha_vantage_handler = Handler()
SMA_IBM = alpha_vantage_handler.indicator_request('SMA', 'IBM', 'weekly', '10', 'open')
print(SMA_IBM)
"""