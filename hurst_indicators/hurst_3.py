import numpy as np

def hurst_exponent(data):
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

# Example usage:
"""if __name__ == "__main__":
    # Replace 'your_time_series_data_here' with your actual time series data as a numpy array.
    time_series_data = np.array(["your_time_series_data_here"])

    hurst_value = hurst_exponent(time_series_data)
    print(f"The Hurst exponent is: {hurst_value}")"""
