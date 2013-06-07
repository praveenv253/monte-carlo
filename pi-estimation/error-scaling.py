#!/usr/bin/env python
from scipy import *
from matplotlib.pyplot import *

def estimate_pi(num_points):
    # Need to create a random 2D array and then find the number of points which 
    # lie inside the circular region
    
    # Create an array_dim x array_dim test array => num_points test points
    array_dim = floor(sqrt(num_points))
    num_points = array_dim * array_dim                    # Reassign num_points
    x = random.random([array_dim, array_dim])
    y = random.random([array_dim, array_dim])

    # Now to count the number of values which lie inside the quarter circle of
    # radius 1
    x = x*x + y*y
    x = floor(x)
    x = ones([array_dim, array_dim]) - x
    count = dot(ones([1, array_dim]), x.dot(ones([array_dim, 1])))[0][0]

    # The value of pi is simply 4 * count / num_points^2, because we are 
    # choosing a quarter circle, and num_points^2 is the total number of points
    result = count * 4 / num_points
    return [num_points, result]

# Estimate pi by using monte carlo, taking a different number of points each 
# time

# Let's take steps of 10k up to 10M
#points = arange(10000, 10010000, 10000)
points = logspace(4, 7, 1000)
print points
x = []
y = []
for i in points:
    num_points, val = estimate_pi(i)
    print i, val
    x.append(num_points)
    y.append(val)

y = array(y)
error = y - pi * ones(1000)
figure(0)
plot(x, error)
show()
