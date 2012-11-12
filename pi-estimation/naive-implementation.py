#!/usr/bin/env python

from scipy import *

# Need to create a random 2D array and then find the number of points which 
# lie inside the circular region

# Create a 1000x1000 test array => 1000^2 test points
x = random.random([1000, 1000])
y = random.random([1000, 1000])

# Now to count the number of values which lie inside the quarter circle of
# radius 1
count = 0
for i in range(1000):
    for j in range(1000):
        # For a point (x, y) to lie in a circle of radius 'r', we must have
        # x^2 + y^2 < r^2
        if x[i][j] * x[i][j] + y[i][j] * y[i][j] < 1:
            count += 1

# The value of pi is simply 4 * count / 1000^2, because we are choosing a
# quarter circle, and 1000^2 is the total number of points
result = 4 * count / 1000000.0
print 'Result of monte carlo simulation: ' + str(result)
print 'Error in value: ' + str((result-pi) / pi * 100) + '%'
