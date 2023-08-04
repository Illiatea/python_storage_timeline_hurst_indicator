# TODO: This file can be named "indicators.py", because from the module, which contains this file it is already
#  clear, which type of indicators it is.
# TODO: This file contains 9 easy style errors, which are displayed by PyCharm.
# TODO: Comments can be placed BEFORE the function definition (function header).
import numpy as np

def hurst_1(data):
    """Compute the Hurst Exponent for a given time series data."""

    # Compute the range of lag values
    lags = range(2, len(data)//2)
    tau = [np.std(np.subtract(data[lag:], data[:-lag])) for lag in lags]

    # Calculate the slope of the log-log plot of the standard deviation versus lag
    m = np.polyfit(np.log10(lags), np.log10(tau), 1)

    # Return the Hurst Exponent
    hurst = m[0] / 2.0
    return hurst

def hurst_2(data):
    """
      Calculates the Hurst exponent of the given data.

      Args:
        data: A list of numbers.

      Returns:
        The Hurst exponent.
    """
    n = len(data)
    m = 0
    d = 0
    for i in range(n):
        r = 0
        for j in range(i):
            r += (data[i] - data[j]) ** 2
        m += r ** (1 / 2)
        d += r
    H = (m / d) ** (1 / 2)
    return H

def hurst_3(data):
    """
    Calculate the Hurst exponent of a given time series data.

    Parameters:
        data (numpy.ndarray): The input time series data.

    Returns:
        float: The calculated Hurst exponent.
    """
    # Calculate the cumulative deviation from the mean
    deviations = np.cumsum(data - np.mean(data))

    # Calculate the range of the data for different window sizes
    ranges = np.max(deviations) - np.min(deviations)

    # Calculate the standard deviation of the data for different window sizes
    std_dev = np.std(data)

    # Calculate the R/S ratio for different window sizes
    rs_ratio = ranges / std_dev

    # Fit a line to the R/S ratio data in a log-log scale
    log_rs_ratio = np.log(rs_ratio)
    log_window_sizes = np.log(np.arange(1, len(rs_ratio) + 1))

    # Calculate the slope (Hurst exponent) of the fitted line
    hurst_exponent = np.polyfit(log_window_sizes, log_rs_ratio, 1)[0]

    return hurst_exponent

def hurst_4(data):
    """
    Calculates the Hurst exponent of the given data.

    Args:
      data: A list of numbers.

    Returns:
      The Hurst exponent.
    """
    n = len(data)

    # Use the first approach for small data sets
    if n <= 100:
        m = 0
        d = 0
        for i in range(n):
            r = 0
            for j in range(i):
                r += (data[i] - data[j]) ** 2
            m += r ** (1 / 2)
            d += r
        H = (m / d) ** (1 / 2)
        return H

    # Use the second approach for larger data sets
    else:
        # Compute the range of lag values
        lags = range(2, n // 2)
        tau = [np.std(np.subtract(data[lag:], data[:-lag])) for lag in lags]

        # Calculate the slope of the log-log plot of the standard deviation versus lag
        m = np.polyfit(np.log10(lags), np.log10(tau), 1)

        # Return the Hurst Exponent
        hurst = m[0] / 2.0
        return hurst

def hurst_5(prices, max_lag=20):
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