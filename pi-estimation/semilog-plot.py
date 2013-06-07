#!/usr/bin/env python

import matplotlib.pyplot as plt

f = open('error-scaling-data.out')

X = []
Y = []
for line in f:
    x, y = line.replace('\n', '').split()
    x = float(x)
    y = float(y)
    X.append(x)
    Y.append(y)

plt.semilogx(X, Y)
plt.show()
