class HurstProcessor:

    def __init__(self, hurst_function):
        self.hurst_function = hurst_function

    def process(self, time_line):

        data = []
        for d in time_line:
            i = d['value']
            data.append(float(i))

        # Process the data using the provided Hurst indicator function
        # TODO: Like for other indicators, this exponent is calculated for some frames of a given size.
        # TODO: That is, calculated for N next or previous items for each time point.
        hurst = self.hurst_function(data)

        # TODO: The result should be a time-line as well. For each time moment (or almost for each) we can calculate
        #  the Hurst exponent.
        return hurst
