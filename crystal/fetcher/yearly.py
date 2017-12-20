"""
Plot the stock values at different periods
"""
from datetime import (
    datetime,
    timedelta,
)

from crystal.fetcher.base import FetcherBase
from crystal.utils.time import timestamp
from crystal.origin.stocks import Origin
from crystal.viz.plotter import (
    plot_single_stock_data,
    plot_multi_stock_data,
)

CATEGORY_CLOSE = 'Close'


class FetcherYearly(FetcherBase):
    def __init__(self, source):
        self.source = source
        self.origin = Origin(source=source)

    def plot_yearly(self, stocks):
        start = datetime.today() - timedelta(days=365)
        end = timestamp(datetime.today())
        if len(stocks) == 1:
            data = self.origin.get_single_stock_data(stocks[0], start, end, CATEGORY_CLOSE)
            plot_single_stock_data(data, stocks[0])
        else:
            data = self.origin.get_multi_stock_data(stocks, start, end, CATEGORY_CLOSE)
            plot_multi_stock_data(data)
