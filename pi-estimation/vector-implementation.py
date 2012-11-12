#!/usr/bin/env python

from scipy import *

# Need to create a random 2D array and then find the number of points which 
# lie inside the circular region

# Create a 1000x1000 test array => 1000^2 test points
x = random.random([1000, 1000])
y = random.random([1000, 1000])

# Now to count the number of values which lie inside the quarter circle of
# radius 1
# First, create a modulus-squared vector
x = x*x + y*y
# Floor it to kill all values that are less than 1
x = floor(x)
# Additive invert in order to get back all the values less than 1
x = ones([1000, 1000]) - x
# Count by multiplying the matrix with a '1' vector on both sides
count = dot(ones([1, 1000]), x.dot(ones([1000, 1])))[0][0]

# The value of pi is simply 4 * count / 1000^2, because we are choosing a
# quarter circle, and 1000^2 is the total number of points
result = count * 4 / 1000000
print 'Result of monte carlo simulation: ' + str(result)
print 'Error in value: ' + str((result-pi) / pi * 100) + '%'
