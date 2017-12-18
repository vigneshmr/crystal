from pandas_datareader import data

_DATA_SOURCE = 'yahoo'


def get_multi_stock_data(
        symbols,
        start_timestamp,
        end_timestamp,
        category,
):
    panel_date = data.DataReader(symbols, _DATA_SOURCE, start_timestamp, end_timestamp)
    close = panel_date.ix[category]

    # Align the existing prices in adj_close with our new set of dates by
    # reindexing close using all_weekdays as the new index
    # all_weekdays = pd.date_range(start=start_timestamp, end=end_timestamp, freq='B')
    # close = close.reindex(all_weekdays)
    return close
