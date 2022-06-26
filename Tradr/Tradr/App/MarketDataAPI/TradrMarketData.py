from Lib.lib import *
import pandas as pd
"""
We create our own special market data requests here,
often it's going to be web scraping
"""

@dataclass
class Config:
    pass


class Handler:

    # Returns wikipedia list of current S&P 500 companies
    @staticmethod
    def get_tradable_s_and_p():
        table = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
        df = table[0]
        s_and_p = df['Symbol'].tolist()
        return s_and_p

    # removes list of stocks from s_and_p list
    @staticmethod
    def filter_out_s_and_p(s_and_p):
        pass