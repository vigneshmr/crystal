from pandas_datareader import data
import pandas as pd

from datetime import (
    datetime,
    timedelta,
)

_DATA_SOURCE = 'google'
_CATEGORY_CLOSE = 'Close'


def timestamp(date):
    """Return current timestamp"""
    return date.strftime('%Y-%m-%d')


def get_stock_data(
        ticker_list,
        start_timestamp,
        end_timestamp,
        category,
):
    panel_date = data.DataReader(ticker_list, _DATA_SOURCE, start_timestamp, end_timestamp)
    close = panel_date.ix[category]
    all_weekdays = pd.date_range(start=start_timestamp, end=end_timestamp, freq='B')

    # Align the existing prices in adj_close with our new set of dates by
    # reindexing close using all_weekdays as the new index
    close = close.reindex(all_weekdays)
    return close


def get_yearly_close_data(ticker_list):
    return get_stock_data(
        ticker_list,
        timestamp(datetime.today() - timedelta(days=365)),
        timestamp(datetime.today()),
        _CATEGORY_CLOSE,
    )


def run():
    close_list = get_yearly_close_data(['MSFT', 'AAPL'])
    import ipdb;
    ipdb.set_trace()


run()
