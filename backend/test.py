import yfinance as yf

ticker = "AAPL"

stock = yf.Ticker(ticker)
hist = stock.history(period="1mo")
print(hist.head())