from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key='30I57ES42OHCEDD0')
data, meta_data = ts.get_intraday('GOOGL')

# Print the data
print(data)

def getDailyStocks(Stock):
    stockData = ts.get_daily(symbol=Stock)
    print(stockData)