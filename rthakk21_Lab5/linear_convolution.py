import numpy as np

from scipy.linalg import toeplitz

def linear_convolution(x,h):
    col = np.append(h,np.zeros(len(x)-1))
    row = np.append(np.array([x[0]]),np.zeros(len(x)-1))
    toe = toeplitz(col,row)
    return np.dot(toe,x)