# Save as app.py and run with: streamlit run app.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

def long_straddle_payoff(stock_prices, strike, call_premium, put_premium):
    call_payoff = np.maximum(stock_prices - strike, 0) - call_premium
    put_payoff = np.maximum(strike - stock_prices, 0) - put_premium
    return call_payoff + put_payoff

st.title("Options Strategy Payoff Viewer")

strike = st.slider("Strike Price", 100, 200, 150)
call_premium = st.slider("Call Premium", 0, 20, 5)
put_premium = st.slider("Put Premium", 0, 20, 5)

stock_range = np.linspace(100, 200, 100)
payoff = long_straddle_payoff(stock_range, strike, call_premium, put_premium)

fig, ax = plt.subplots()
ax.plot(stock_range, payoff)
ax.axhline(0, color='black', linestyle='--')
ax.set_title("Long Straddle Payoff")
ax.set_xlabel("Stock Price at Expiry")
ax.set_ylabel("P&L")
st.pyplot(fig)
