#!/usr/bin/env python

from scipy import *
from function import function, domain

# We do a monte-carlo integration with 1,000,000 points
numpoints = 1000000

# Create 'numpoints' number of random points in [0, 1)x[0, 1)
x = random.random(numpoints)
y = random.random(numpoints)

# Scale x to fit the domain
x = x * (domain[1] - domain[0]) + domain[0]

# Evaluate f at all x for future comparison with y
fx = function(x)

# Now to find the range over which the function spans, in the given domain
maxy = max(fx)
miny = min(fx)

# Now scale y to fit the range
y = y * (maxy - miny) + miny

# Now find how many of the points are actually 'under' the curve. This depends
# upon sign. If fx is positive, y is under the curve if 0 < y < fx and 
# contributes positive area. If fx is negative, y is under the curve if 
# 0 > y > fx and contributes negative area
countplus = len(where((y > 0) * (fx > y))[0])
countminus = len(where((y < 0) * (fx < y))[0])

print countplus, countminus

# The total area of the rectangle where we have spread our points is:
totalarea = (domain[1] - domain[0]) * (maxy - miny)

# The area under the function is hence:
integral = totalarea * (countplus - countminus) / numpoints

# But this area is still not quite right. If miny was positive, then we have
# missed out the area that was between miny and the x-axis. Similarly if maxy
# was negative, we have missed out the area that was between maxy and the
# x-axis. So we add/subtract these values from the calculated area
if miny > 0:
    integral += miny * (domain[1] - domain[0])
if maxy < 0:
    integral -= maxy * (domain[1] - domain[0])

# Display the final answer
print integral
