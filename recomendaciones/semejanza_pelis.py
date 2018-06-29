import numpy as np
from scipy.spatial.distance import cosine

def prom(arr):
    cant = 0
    sum = 0
    for v in arr:
        if v > 0:
            sum += v
            cant += 1
    return sum / cant
    
def restar_prom_col(mat):
    ret = mat.copy()
    for j in range(0, mat.shape[1]):
        prom_col = prom(ret[:,j])
        for i in range(0, mat.shape[0]):
            if ret[i,j] > 0:
                ret[i,j] -= prom_col
    return ret

def dist_coseno(u, v):
    nu = np.linalg.norm(u)
    nv = np.linalg.norm(v)
    return 1 - np.round(np.dot(u, v) / (nu * nv), decimals=3)

A = np.array([[4.0, 5, 0, 5, 1, 0, 3, 2], 
              [0  , 3, 4, 3, 1, 2, 1, 0],
              [2  , 0, 1, 3, 0, 4, 5, 3]])

A_centrada = restar_prom_col(A)

sims = []
for j in range(0, A_centrada.shape[1]):
    sims.append(dist_coseno(A_centrada[:,0], A_centrada[:,j]))

claves = { 0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h' }

print('A centrada:')
print(A_centrada)
print('')
print('Similitudes:')
print(sims)
print('')
print('Ordenando de min a max:')
print(np.sort(sims))
vclaves = []
for c in np.argsort(sims):
    vclaves.append(claves[c])
print(vclaves)
