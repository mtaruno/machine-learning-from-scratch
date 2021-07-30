"""
Here are the core statistics fundmentals.
"""

import math


def correlation(x, y):
    """Find the correlation coefficient between two samples of data"""
    n = len(x)
    vals = range(n)

    # Find the sum of the products
    prod = sum(x[i] * y[i] for i in vals)

    # Sum the squares of each
    sumx = sum(x[i] ** 2 for i in vals)
    sumy = sum(y[i] ** 2 for i in vals)

    # Sum the products
    sumxy = sum(x[i] * y[i] for i in vals)

    # Calculate and return the correlation coefficient
    return prod / math.sqrt(sumx * sumy)



