import numpy as np
from scipy.spatial.distance import cosine

def restar_prom_fila(mat):
    ret = mat
    for i in range(0, mat.shape[0]):
        ret[i,:] -= np.mean(ret[i,:])
    return ret

def restar_prom_col(mat):
    ret = mat
    for i in range(0, mat.shape[1]):
        ret[:,i] -= np.mean(ret[:,i])
    return ret

A = np.array([[1.0, 2, 3, 4, 5],
              [2  , 3, 2, 5, 3],
              [5  , 5, 5, 3, 2]])

A = restar_prom_fila(A)
print(A)
A = restar_prom_col(A)
print(A)