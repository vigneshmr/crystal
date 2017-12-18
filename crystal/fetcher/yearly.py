"""
Plot the stock values at different periods
"""
from datetime import (
    datetime,
    timedelta,
)

from crystal.utils.time import timestamp
from crystal.data.stocks import get_multi_stock_data
from crystal.viz.plotter import plot_stock_data

CATEGORY_CLOSE = 'Close'


def plot_yearly(stocks):
    start = datetime.today() - timedelta(days=365)
    end = timestamp(datetime.today())
    data = get_multi_stock_data(stocks, start, end, CATEGORY_CLOSE)
    plot_stock_data(data)
