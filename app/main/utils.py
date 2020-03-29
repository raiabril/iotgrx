import numpy as np


def filter_values(values):
    for i in range(len(values)):
        if i == 0:
            values[0] = values[0]
        elif i == len(values)-1:
            values[i] = (values[i - 1] + values[i]) / 2
        else:
            values[i] = (values[i - 1] + values[i] + values[i + 1]) / 3
    return values

def calibrate_raw(array, a0, a1, fit_type):
    x = np.array(array, dtype=np.float64)
    calibrated_array = []

    if fit_type == 'linear':
        calibrated_array = x*a1 + a0

    elif fit_type == 'log':
        calibrated_array = a0 + np.exp(x*a1)

    return calibrated_array.tolist()


def fit_curve(x, y, fit_type):

    if fit_type == 'linear':

        x = np.array(x)
        y = np.array(y)
        z = np.polyfit(x, y, 1)
        a0 = z[1]
        a1 = z[0]


    elif fit_type == 'log':

        x = np.array(x)
        y = np.array(y)
        z = np.polyfit(x, np.log(y), 1, w=np.sqrt(y))

        a0 = np.exp(z[1])
        a1 = z[0]

    return a0, a1