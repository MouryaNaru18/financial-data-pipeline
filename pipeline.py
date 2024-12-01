import yfinance as yf

# Fetching data for a specific stock (e.g., MRVL - Marvell Technology)
ticker = "MRVL"
data = yf.download(ticker, start="2023-10-01", end="2023-12-01")

# Save the data to a CSV
data.to_csv(f"{ticker}_data.csv")

print(f"Data for {ticker} saved to CSV.")
