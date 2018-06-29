import numpy as np
from scipy.spatial.distance import jaccard

M = np.array([[1, 1, 0, 1, 0, 0, 1, 0],
              [0, 1, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 1, 1, 1]])

J = np.zeros((M.shape[1], M.shape[1]))

for i in range(0, M.shape[1]):
    for j in range(0, M.shape[1]):
        J[i, j] = jaccard(M[:, i], M[:, j])

print(J[4])