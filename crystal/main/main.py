import sys

from crystal.config.stocks import Config
from crystal.data.stocks import SYMBOLS_FANG
from crystal.fetcher.yearly import FetcherYearly
from crystal.origin.stocks import (
    DATA_SOURCE_GOOGLE,
    DATA_SOURCE_YAHOO,
    DATA_SOURCE_QUANDL,
)
from crystal.utils.commands import (
    Command,
    Commander,
)
from crystal.utils.console import get_line

from termcolor import colored


def plot_yearly_stocks():
    stocks = raw_input('Symbols (separated by space): ')
    stocks = stocks.split(' ')
    FetcherYearly(Config.origin).plot_yearly(stocks)


def plot_yearly_fang():
    FetcherYearly(Config.origin).plot_yearly(SYMBOLS_FANG)


def update_stock_source():
    pick = raw_input('Pick source: q (quandal), g (google), y (yahoo):')
    pick = pick.lower()
    if pick.startswith('q'):
        Config.origin = DATA_SOURCE_QUANDL
    elif pick.startswith('g'):
        Config.origin = DATA_SOURCE_GOOGLE
    else:
        Config.origin = DATA_SOURCE_YAHOO


def header():
    print colored(get_line(), 'cyan')
    print colored('Crystal - Stock analysis', 'green')
    print colored(get_line(), 'cyan')
    print colored('Current source: ', 'white') + colored(Config.origin, 'red')
    print colored(get_line(), 'red')


def commander():
    cmd = Commander(
        header_command=Command(title='header', action=lambda: header()),
        commands=[
            Command(title='Exit', action=lambda: sys.exit()),
            Command(title='stocks: yearly close', action=lambda: plot_yearly_stocks()),
            Command(title='stocks: yearly close for FANG', action=lambda: plot_yearly_fang()),
            Command(title='config: change source', action=lambda: update_stock_source()),
        ])
    cmd.run()


commander()
