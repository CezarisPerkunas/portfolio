import pandas as pd

def simulate_strategy(prices, strike, call_prem, put_prem):
    results = []
    for price in prices:
        pnl = max(price - strike, 0) - call_prem + max(strike - price, 0) - put_prem
        results.append(pnl)
    return pd.Series(results, index=prices)
