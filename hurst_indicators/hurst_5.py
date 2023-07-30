import numpy as np

def hurst_exponent(prices, max_lag=20):
    """
    Calculate the Hurst exponent using the R/S analysis method.

    Parameters:
        prices (array-like): The time series data for which the Hurst exponent is to be calculated.
        max_lag (int): The maximum lag value for the calculation. The default is 20.

    Returns:
        hurst (float): The estimated Hurst exponent.
    """
    prices = np.asarray(prices)
    n = len(prices)
    lags = range(2, max_lag)
    tau = [np.std(np.subtract(prices[lag:], prices[:-lag])) for lag in lags]
    hurst = np.polyfit(np.log(lags), np.log(tau), 1)[0]
    return hurst

# Example usage:
"""time_series_data = [10, 12, 14, 18, 20, 22, 26, 30, 32, 34]
hurst_value = hurst_exponent(time_series_data)
print("Hurst Exponent:", hurst_value)"""
