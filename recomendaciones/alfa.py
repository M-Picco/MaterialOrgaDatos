import numpy as np
from scipy.spatial.distance import cosine, pdist, squareform

A = np.array([[1, 0, 1, 0, 1, 2],
              [1, 1, 0, 0, 1, 6],
              [0, 1, 0, 1, 0, 2]], dtype='float64')

alfas = [0, 0.5, 1, 2]

def dist_coseno(u, v):
    nu = np.linalg.norm(u)
    nv = np.linalg.norm(v)
    return 1 - np.round(np.dot(u, v) / (nu * nv), decimals=3)

for a in alfas:
    B = A.copy()
    B[:,-1] *= a

    D = squareform(pdist(B, metric=dist_coseno))

    print('{}:\n{}'.format(a, D))

