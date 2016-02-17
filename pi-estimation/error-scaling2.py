#!/usr/bin/env python3

"""
The real error scaling program.
Calculates standard deviation from the mean at each given total number of
points. Then, we plot standard deviation against number of points.
"""

from __future__ import print_function, division

import sys
import scipy as sp
import matplotlib.pyplot as plt


def find_pi_approx(num_points):
    # Need to create a random 2D array and then find the number of points which
    # lie inside the circular region

    # Create an array_dim x array_dim test array => num_points test points
    array_dim = sp.floor(num_points)
    num_points = array_dim                            # Reassign num_points
    x = sp.random.random(array_dim)
    y = sp.random.random(array_dim)

    # Now to count the number of values which lie inside the quarter circle of
    # radius 1
    x = x*x + y*y
    x = sp.floor(x)
    # x now contains only 1's and 0's. The fraction of 0's corresponds to the
    # region within the quarter-circle.
    count = sp.dot(sp.ones([1, array_dim]), x)[0]
    count = num_points - count

    # The value of pi is simply 4 * count / num_points^2, because we are
    # choosing a quarter circle, and num_points^2 is the total number of points
    result = count * 4 / num_points
    return num_points, result


def get_error(num_points, num_iter=100):
    """
    Compute mean and standard deviation from the mean. Standard deviation from
    the mean is error.
    """

    num_points = sp.floor(num_points)

    pi_values = []
    for i in range(num_iter):
        pi_values.append(find_pi_approx(num_points)[1])

    pi_values = sp.array(pi_values)
    return num_points, sp.std(pi_values)


if __name__ == '__main__':
    points = sp.logspace(4, 6, 100)
    x = []
    y = []
    for i in points:
        num_points, err = get_error(i)
        print(num_points, err)
        x.append(num_points)
        y.append(err)

    plt.figure(0)
    plt.plot(x, y)
    plt.show()
