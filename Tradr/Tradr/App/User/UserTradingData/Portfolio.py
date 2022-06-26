"""
Storage of portfolio data for trading
"""
from abc import ABC


# Portfolio constraints (divided by broker)
# determine whether bots can trade at all
@dataclass
class Portfolio(ABC):
    new_portfolio: bool
    cash: float
    equity: float
    bought_today: list
    day_trade_cnt: int
    owned_securities: list
    cash_buffer: float
    cash_buffer_pct: float

    @staticmethod
    def append_bought_today_txt(security):
        with open('bought_today.txt', 'a') as f:
            f.write(security)
            f.write("\n")

    @staticmethod
    def clear_bought_today_txt():
        with open('bought_today.txt', 'r+') as f:
            f.truncate(0)
        print("bought today list cleared")

    @staticmethod
    def if_bought_today(symbol):
        with open('bought_today.txt', 'r') as bought_today_txt:
            for line in bought_today_txt:
                list_symbol = line.rstrip("\n")
                if symbol == list_symbol:
                    return True

        return False


@dataclass
class AlpacaPortfolio(Portfolio):
    """
    day_trade_count = BrokerHandler.AlpacaBroker.fetch_day_trading_count()
    portfolio_api_list = BrokerHandler.AlpacaBroker.fetch_portfolio_list()
    bought_today_list = BrokerHandler.AlpacaBroker.fetch_bought_today_list()
    new_portfolio = BrokerHandler.AlpacaBroker.is_new_portfolio()
    """
    new_portfolio: bool
    cash: float
    equity: float
    bought_today: list
    day_trade_cnt: int
    owned_securities: list

    def __init__(self):
        pass
