import numpy as np
import pandas as pd
import matplotlib as my
import yfinance as yf
import matplotlib.pyplot as plt

company_to_ticker = {
    "Apple": "AAPL",
    "Google": "GOOGL",
    "Microsoft": "MSFT",
    "Tesla": "TSLA",
    "Amazon": "AMZN",
    "Reliance": "RELIANCE.NS",
    "TCS": "TCS.NS",
    "Infosys": "INFY.NS"
}
stock_data=yf.download('NFLX',start='2023-01-01',end='2025-01-01')
#print(stock_data.head())
data=pd.DataFrame(stock_data)

def cleaning_data():
    #print(data)
    data.dropna(inplace=True)
    #print(new_data.to_string())
    #print(new_data.head())
    #print(new_data.duplicated())
    data.drop_duplicates(inplace=True)

def basic_stats():
    return data.describe() 

 
def plot_data():
    plt.figure(figsize=(9, 6))
    plt.plot(data['Close'], label='Closing Price')
    plt.title('Netflix Stock Price (2023-2025)')
    plt.xlabel('Date')
    plt.ylabel('Stock Price (USD)')
    plt.legend(shadow=True)
    plt.grid(True)

def plot_mov_avg():
    data['50_day_ma'] = data['Close'].rolling(window=50).mean()
    data['100_day_ma'] = data['Close'].rolling(window=100).mean()
    plt.figure(figsize=(10,6))
    plt.plot(data['Close'], label='Closing Price')
    plt.plot(data['50_day_ma'],label='50 Day moving average')
    plt.plot(data['100_day_ma'],label='100 Day moving average')
    plt.title('Netflix Stock moving Average')
    plt.xlabel('Date')
    plt.ylabel('Stock price(USD)')
    plt.legend()
    plt.grid(True)

def Volatility():
    data['Daily Return']=data['Close'].pct_change()
    volatility=data['Daily Return'].std()
    return (f"Annualized Volatility: {volatility:.2%}")

def cumulativeReturn():
    data['Daily return']=data['Close'].pct_change()
    data['Cumulative Return'] = (1 + data['Daily Return']).cumprod()
    plt.figure(figsize=(10, 6))
    plt.plot(data['Cumulative Return'], label='Cumulative Return')
    plt.title('Cumulative Return of Netflix Stock')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Return')
    plt.legend()
    plt.grid(True)

 
def sharpe_Ratio():
    risk_free_rate = 0
    data['Daily return']=data['Close'].pct_change()
    excess_daily_return = data['Daily Return'] - risk_free_rate
    sharpe_ratio = excess_daily_return.mean() / excess_daily_return.std() * (252**0.5) 
    return (f"Sharpe Ratio: {sharpe_ratio:.2f}")


'''def plot_adjclose(data_set):
    plt.figure(figsize=(10,6))
    plt.plot(data_set['Adj Close'],label='Adjusted Close Price')
    plt.plot(data_set['Close'],label='Close Price')
    plt.title('Netflix Stock: Close vs Adjusted Close (2023–2025)')
    plt.xlabel('Date')
    plt.ylabel('Stock Price(USD)')
    plt.legend()
    plt.show()

plot_adjclose(data)'''



