import sys

from crystal.data.stocks import SYMBOLS_FANG
from crystal.fetcher.yearly import plot_yearly
from crystal.utils.commands import (
    Command,
    Commander,
)


def plot_yearly_stocks():
    stocks = raw_input('Symbols (separated by space): ')
    stocks = stocks.split(' ')
    plot_yearly(stocks)


def plot_yearly_fang():
    plot_yearly(SYMBOLS_FANG)


def commander():
    cmd = Commander([
        Command(title='Exit', action=lambda: sys.exit()),
        Command(title='stocks: yearly close', action=lambda: plot_yearly_stocks()),
        Command(title='stocks: yearly close for FANG', action=lambda: plot_yearly_fang()),
    ])
    cmd.run()


commander()
