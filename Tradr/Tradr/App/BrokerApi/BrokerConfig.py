# We set broker configurations here

from abc import ABC
from dataclasses import dataclass


@dataclass
class BrokerConfig(ABC):
    pass


@dataclass
class AlpacaBroker(BrokerConfig):
    secret_key: str
    api_key: str
    paper_url: None
    alpaca_url: str
    paper_secret_key: str
    paper_api_key: str
    paper_account_url: None

    def __init__(self):
        url = ''
        secret_key = ''
        api_key = ''
        paper_url = 'https://paper-api.alpaca.markets'
        paper_secret_key = '0p331rAnBMq86APQZsSYa8CPXCiJxVdASNfG1gQA'
        paper_api_key = 'PKV9XRB4FDO39ES68MJY'
        paper_account_url = "{}/v2/account/configurations".format(paper_url)


@dataclass
class IBKRConfig(BrokerConfig):
    pass
