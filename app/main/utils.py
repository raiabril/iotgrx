def filter_values(values):
    for i in range(len(values)):
        if i == 0:
            values[0] = values[0]
        elif i == len(values)-1:
            values[i] = (values[i - 1] + values[i]) / 2
        else:
            values[i] = (values[i - 1] + values[i] + values[i + 1]) / 3
    return values
