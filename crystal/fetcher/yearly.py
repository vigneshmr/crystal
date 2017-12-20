"""
Plot the stock values at different periods
"""
from datetime import (
    datetime,
    timedelta,
)

from crystal.utils.time import timestamp
from crystal.origin.stocks import (
    get_multi_stock_data,
    get_single_stock_data,
)
from crystal.viz.plotter import (
    plot_single_stock_data,
    plot_multi_stock_data,
)

CATEGORY_CLOSE = 'Close'


def plot_yearly(stocks):
    start = datetime.today() - timedelta(days=365)
    end = timestamp(datetime.today())
    if len(stocks) == 1:
        data = get_single_stock_data(stocks[0], start, end, CATEGORY_CLOSE)
        plot_single_stock_data(data, stocks[0])
    else:
        data = get_multi_stock_data(stocks, start, end, CATEGORY_CLOSE)
        plot_multi_stock_data(data)
