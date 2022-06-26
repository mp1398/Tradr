"""
We process Alpaca Market Data API requests here
"""
from Lib.lib import *
import alpaca_trade_api as tradeapi


# alpaca free subscription
# offers market data from IEX
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

    pass
