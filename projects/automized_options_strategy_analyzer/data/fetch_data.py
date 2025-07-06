import yfinance as yf

def get_option_chain(ticker_symbol, expiry_date):
    stock = yf.Ticker(ticker_symbol)
    options = stock.option_chain(expiry_date)
    return options.calls, options.puts
