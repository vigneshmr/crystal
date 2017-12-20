from pandas_datareader import data

# Known bug exist:
# https://github.com/pydata/pandas-datareader/issues/395
DATA_SOURCE_GOOGLE = 'google'

DATA_SOURCE_QUANDL = 'quandl'
DATA_SOURCE_YAHOO = 'yahoo'


def get_multi_stock_data(
        symbols,
        start_timestamp,
        end_timestamp,
        category,
):
    panel_date = data.DataReader(symbols, DATA_SOURCE_YAHOO, start_timestamp, end_timestamp)
    close = panel_date.ix[category]

    # Align the existing prices in adj_close with our new set of dates by
    # reindexing close using all_weekdays as the new index
    # all_weekdays = pd.date_range(start=start_timestamp, end=end_timestamp, freq='B')
    # close = close.reindex(all_weekdays)
    return close


def get_single_stock_data(
        symbol,
        start_timestamp,
        end_timestamp,
        category,
):
    symbol = quandl_symbol_patch(symbol)
    series = data.DataReader(symbol, DATA_SOURCE_QUANDL, start_timestamp, end_timestamp)
    return series[category]


def quandl_symbol_patch(symbol):
    return ('wiki/' + symbol).upper()
