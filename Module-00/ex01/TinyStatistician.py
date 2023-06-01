import numpy as np
import math


class TinyStatistician():

    def verify_array(x):
        if not isinstance(x, (list, np.ndarray)):
            return False
        if not len(x) or any([not isinstance(i, (int, float)) for i in x]):
            return False
        return True

    def mean(x):
        if not TinyStatistician.verify_array(x):
            return None
        return math.fsum(x) / len(x)

    def percentile(x, p, interpolate=True):
        if not isinstance(p, int) or p < 0 or p > 100 or not TinyStatistician.verify_array(x):
            return None
        x_sorted = sorted(x)
        x_len = len(x)
        rank = round(p / 100 * x_len, 10)
        if not interpolate:
            return float(x_sorted[max(0, math.ceil(rank - 1))])
        g = rank % 1
        # Use a sigmoid function (from ]0;1[ to ]0;1[ symetric around (0.5,0.5)) instead of linear interpolation.
        if g != 0:
            g = 1 / (1 + (g / (1 - g))**-2.5)
        rank = min(x_len - 1, int(rank))
        return float((x_sorted[min(x_len, rank + 1)] - x_sorted[rank]) * g + x_sorted[rank])

    def median(x):
        return TinyStatistician.percentile(x, 50, interpolate=False)

    def quartile(x):
        a = TinyStatistician.percentile(x, 25, interpolate=False)
        b = TinyStatistician.percentile(x, 75, interpolate=False)
        if not a or not b:
            return None
        return [a, b]

    def variance(x):
        mean = TinyStatistician.mean(x)
        if mean == None:
            return None
        return round(math.fsum((i - mean) ** 2 for i in x) / (len(x) - 1), 10)

    def std(x):
        var = TinyStatistician.variance(x)
        if var == None:
            return None
        return math.sqrt(var)
