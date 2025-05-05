import streamlit as st
import dss as dss
import matplotlib.pyplot as plt 
import yfinance as yf
import pandas as pd
import altair as alt
from vega_datasets import data

st.title('Stock Analysis Dashboard')
company_to_ticker = {
    "Apple": "AAPL",
    "Google": "GOOGL",
    "Microsoft": "MSFT",
    "Tesla": "TSLA",
    "Amazon": "AMZN",
    "Reliance": "RELIANCE.NS",
    "TCS": "TCS.NS",
    "Infosys": "INFY.NS",
    "Netflix":"NFLX"
}
Company=st.selectbox("Name of Company:",['Apple','Google','Microsoft','Amazon','Tesla','Reliance','TCS','Infosys','Netflix'])
if Company in company_to_ticker :
    ticker=company_to_ticker[Company]
elif Company not in company_to_ticker:
    st.error('Enter a valid Company')
stock_data=yf.download({ticker},start='2023-01-01',end='2025-01-01')
data=pd.DataFrame(stock_data)

st.success('HeHe You Opened My dashboard .. STUPID PEEPAL')
st.subheader('Data Description')
st.dataframe(dss.basic_stats(data))
st.subheader('Stock Close Price')
fig=dss.plot_data(ticker,data)
st.pyplot(fig)

st.subheader('Moving Averages')
#st.slider('Choose Time Frame for Moving Average',0,100,50,step=10)
fig1=dss.plot_mov_avg(ticker,data)
st.pyplot(fig1)

st.subheader('Volatility')
st.write(dss.Volatility(ticker,data))

st.subheader('Cumulative Returns')
fig2=dss.cumulativeReturn(ticker,data)
st.pyplot(fig2)

st.subheader('Sharpe Ratio')
st.write(dss.sharpe_Ratio(ticker,data))