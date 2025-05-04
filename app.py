import streamlit as st
import dss as dss
import matplotlib.pyplot as plt 

st.title('Stock Analysis Dashboard')

st.success('HeHe You Opened My dashboard .. STUPID PEEPAL')
st.subheader('Data Description')
st.dataframe(dss.basic_stats())
st.subheader('Stock Close Price')
fig=dss.plot_data()
st.pyplot(fig)

st.subheader('Moving Averages')
#st.slider('Choose Time Frame for Moving Average',0,100,50,step=10)
fig1=dss.plot_mov_avg()
st.pyplot(fig1)

st.subheader('Volatility')
st.write(dss.Volatility())

st.subheader('Cumulative Returns')
fig2=dss.cumulativeReturn()
st.pyplot(fig2)

st.subheader('Sharpe Ratio')
st.write(dss.sharpe_Ratio())