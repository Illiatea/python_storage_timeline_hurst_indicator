import numpy as np

def hurst(data):
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

"""
In this implementation, we check if the length of the data is less than or equal to 100, and if so, we use the first 
approach. Otherwise, we switch to the second approach for larger data sets. This will provide a balance between accuracy
and performance based on the size of the input data.
"""