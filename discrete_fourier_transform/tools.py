import numpy as np


def cconv(x, y, P):
    """ Periodic convolution with period P of two signals x and y
    """
    x = _wrap(x, P)
    h = _wrap(y, P)

    return np.fromiter([np.dot(np.roll(x[::-1], k+1), h) for k in np.arange(P)], float)


def _wrap(x, N):
    """Zero-padding to length N or periodic summation with period N"""
    M = len(x)
    rows = np.ceil(M/N)
    
    if (M < int(N*rows)):
        x = np.pad(x, (0, int(N*rows-M)), 'constant')
    
    x = np.reshape(x, (rows, N))
    
    return np.sum(x, axis=0)