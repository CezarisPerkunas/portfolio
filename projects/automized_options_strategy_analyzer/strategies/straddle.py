import numpy as np
import matplotlib.pyplot as plt

def long_straddle_payoff(stock_prices, strike, call_premium, put_premium):
    call_payoff = np.maximum(stock_prices - strike, 0) - call_premium
    put_payoff = np.maximum(strike - stock_prices, 0) - put_premium
    return call_payoff + put_payoff
