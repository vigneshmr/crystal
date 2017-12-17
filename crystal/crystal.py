from datetime import (
    datetime,
    timedelta,
)
import sys

from utils.commands import (
    Command,
    Commander,
)

from pandas_datareader import data
import matplotlib.pyplot as plt

_DATA_SOURCE = 'yahoo'
_CATEGORY_CLOSE = 'Close'


def timestamp(date):
    """Return current timestamp"""
    return date.strftime('%Y-%m-%d')


def get_stock_data(
        symbol,
        start_timestamp,
        end_timestamp,
        category,
):
    panel_date = data.DataReader([symbol], _DATA_SOURCE, start_timestamp, end_timestamp)
    close = panel_date.ix[category]

    # Align the existing prices in adj_close with our new set of dates by
    # reindexing close using all_weekdays as the new index
    # all_weekdays = pd.date_range(start=start_timestamp, end=end_timestamp, freq='B')
    # close = close.reindex(all_weekdays)
    return close


def plot_stock_data(symbol, start_ts, end_ts, category):
    close = get_stock_data(symbol, start_ts, end_ts, category)
    plt.plot(close)
    plt.ylabel('time')
    plt.xlabel('stock value')
    plt.title('stock - ' + symbol + ', category: ' + category)
    plt.draw()
    plt.show()


def plot_yearly_close(symbol):
    return plot_stock_data(
        symbol,
        timestamp(datetime.today() - timedelta(days=365)),
        timestamp(datetime.today()),
        _CATEGORY_CLOSE,
    )


def plot_any_stock():
    stock = raw_input('Symbol: ')
    plot_yearly_close(stock)


def commander():
    cmd = Commander([
        Command(title='Exit', action=lambda: sys.exit()),
        Command(title='stock: plot yearly close', action=lambda: plot_any_stock()),
    ])
    cmd.run()


commander()
