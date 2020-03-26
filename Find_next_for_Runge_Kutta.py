import math
import numpy


def func(y, alpha, betta):
    result = [0.0] * 2
    result[0] = 1 - y[0] * y[1]
    result[1] = alpha * y[1] * (y[0] - (1 + betta) / (y[1] + betta))
    return numpy.array(result)


def odds(x0, y0, h, alpha, betta):
    y = [0.0] * 2
    y[0] = x0
    y[1] = y0
    y = numpy.array(y)
    k = [0] * 4
    k[0] = h * func(y, alpha, betta)
    k[1] = h * func(y + k[0]/2, alpha, betta)
    k[2] = h * func(y + k[1]/2, alpha, betta)
    k[3] = h * func(y + k[2], alpha, betta)
    return k


def find_next(x0, y0, h, alpha, betta):
    k = odds(x0, y0, h, alpha, betta)
    y = [0.0] * 2
    y[0] = x0
    y[1] = y0
    y = numpy.array(y)
    result = y + (k[0] + 2*k[1] + 2*k[2] + k[3])/6
    return result

