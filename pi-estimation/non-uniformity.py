#!/usr/bin/env python

import scipy as sp
import matplotlib.pyplot as plt

if __name__ == '__main__':
    N = 1000
    num_bins = 100
    x = sp.zeros((N, num_bins))
    for i in xrange(N):
        print i
        a = sp.random.random(1e7)
        x[i] += plt.hist(a, bins=num_bins, normed=True)[0]
    sp.save('non-uniformity-data-%s-bins.npy' % num_bins, x)
    mu = sp.average(x, axis=0)
    print mu
    sigma = sp.std(x, axis=0)
    print sigma
