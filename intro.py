import yfinance as yf
import streamlit as st

st.title("Stockprice Analyzer")
data = yf.Ticker("AAPL")
st.write(data.history(period="1mo"))