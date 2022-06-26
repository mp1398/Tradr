from dataclasses import dataclass
from abc import ABC


# Bot identification is to construct unique bots
# these qualities are descriptors that effect where and how
@dataclass
class Identity:
    name: str
    broker: str
    paper: bool
    data_src: str
    type: str


# Bot order events dictate bot actions
@dataclass
class OrderEvent(ABC):
    pass


# Triggers used by bot for buys and sells
@dataclass
class Triggers(OrderEvent):
    sell_triggers: dict
    buy_triggers: dict

    def iter_sell_trig(self):
        pass

    def iter_buy_trig(self):
        pass

    def check_sell_trig(self):
        pass

    def check_buy_trig(self):
        pass


# multipliers and dividers to modify bot
# purchase/sell amounts
@dataclass
class TriggerModifiers(OrderEvent):
    multipliers: dict
    dividers: dict


# Determines whether bots are even able to buy/sell
@dataclass
class TriggerConstraints(OrderEvent):
    constraints: dict


# This class is the final construction
# of our bot instances
@dataclass
class BotInstance:
    bot_identity: Identity
    bot_triggers: Triggers
    bot_constraints: TriggerConstraints
    bot_modifiers: TriggerModifiers


"""
# Py file testing code
def main():
    cost_avg_identity = Identity(name='cost_avg', broker='Alpaca', data_src='Alpaca', type='investBot',
                                    paper=True)
    cost_avg_triggers = Triggers(buy_triggers={}, sell_triggers={})
    cost_avg_mods = TriggerModifiers(multipliers={}, dividers={})
    cost_avg_const = TriggerConstraints(constraints={})

    cost_avg = BotInstance(bot_identity=cost_avg_identity, bot_triggers=cost_avg_triggers,
                           bot_modifiers=cost_avg_mods, bot_constraints=cost_avg_const)
    print(cost_avg)


if __name__ == '__main__':
    main()
"""