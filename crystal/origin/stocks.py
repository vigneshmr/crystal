from crystal.origin.base import OriginBase

from pandas_datareader import data

# Known bug exist:
# https://github.com/pydata/pandas-datareader/issues/395
DATA_SOURCE_GOOGLE = 'google'
DATA_SOURCE_QUANDL = 'quandl'
DATA_SOURCE_YAHOO = 'yahoo'


class Origin(OriginBase):
    def __init__(self, source):
        self.source = source

    def get_multi_stock_data(
            self,
            symbols,
            start_timestamp,
            end_timestamp,
            category,
    ):
        panel_date = data.DataReader(symbols, self.source, start_timestamp, end_timestamp)
        close = panel_date.ix[category]

        # Align the existing prices in adj_close with our new set of dates by
        # reindexing close using all_weekdays as the new index
        # all_weekdays = pd.date_range(start=start_timestamp, end=end_timestamp, freq='B')
        # close = close.reindex(all_weekdays)
        return close

    def get_single_stock_data(
            self,
            symbol,
            start_timestamp,
            end_timestamp,
            category,
    ):
        if self.source == DATA_SOURCE_QUANDL:
            symbol = self._quandl_symbol_patch(symbol)
        else:
            symbol = [symbol]

        series = data.DataReader(symbol, self.source, start_timestamp, end_timestamp)
        return series[category]

    @staticmethod
    def _quandl_symbol_patch(symbol):
        if '/' not in symbol:
            symbol = 'wiki/' + symbol
        return symbol.upper()
