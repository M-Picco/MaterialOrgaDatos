import numpy as np
from scipy.spatial.distance import pdist, euclidean, squareform

A = np.array([[0, 0],
            [10, 10],
            [21, 21],
            [33, 33],
            [5, 27],
            [28, 6]])

dists = squareform(pdist(A, 'euclidean'))
print(dists)