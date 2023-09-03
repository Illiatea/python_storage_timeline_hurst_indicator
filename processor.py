class HurstProcessor:

    def __init__(self, hurst_function, number_of_none_values):
        self.number_of_none_values = number_of_none_values
        self.hurst_function = hurst_function

    def process(self, time_line):

        data_for_calculation = []
        data = []
        for value in time_line:
            i = value['value']
            data_for_calculation.append(float(i))

            if len(data_for_calculation) <= self.number_of_none_values:
                data.append(None)
            else:
                hurst = self.hurst_function(data)
                data.append(hurst)


        result = [{'time': time_line[i]['time'], 'value': data[i]} for i in
                  range(len(time_line))]
        return result
