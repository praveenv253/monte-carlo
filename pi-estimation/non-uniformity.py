#!/usr/bin/env python

import scipy as sp
import matplotlib.pyplot as plt

if __name__ == '__main__':
    a = sp.random.random(1e8)
    plt.hist(a, bins=100)
    plt.show()

