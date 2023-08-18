# TODO: Create a Google Colab, which shows, how the indicator is applied to data taken from the database or to data,
#  processed by TA-Lib indicators.

class HurstProcessor:
    def __init__(self, hurst_function):
        self.hurst_function = hurst_function

    def process(self, time_line):
        if not callable(self.hurst_function):
            raise ValueError("hurst_function should be a callable function")

        data = []
        for d in time_line:
            i = d['value']
            data.append(float(i))

        # Process the data using the provided Hurst indicator function
        hurst = self.hurst_function(data)

        return hurst
