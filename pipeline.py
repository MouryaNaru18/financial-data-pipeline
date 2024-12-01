from flask import Flask, render_template_string
import yfinance as yf
import pandas as pd

app = Flask(__name__)

@app.route('/')
def display_data():
    # Fetch stock data for MRVL (Marvell Technology)
    ticker = "MRVL"
    data = yf.download(ticker, start="2024-11-01", end="2024-12-01")

    if data.empty:
        return "No data available for the selected date range."

    # Convert the data to an HTML table
    data_html = data.to_html(classes='table table-striped')

    # Return an HTML template displaying the data
    html = f"""
    <!doctype html>
    <html>
    <head><title>Stock Data</title></head>
    <body>
    <h1>Marvell Technology Data</h1>
    {data_html}
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
