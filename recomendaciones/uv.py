import numpy as np

M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype='float64')
V = np.array([[5, 5, 5]], dtype='float64')

U = np.array([np.round(np.linalg.svd(M)[0][:,0], decimals=3)], dtype='float64').T

print(U)
print(V)
print(M)

alfa = 0.1

err = np.linalg.norm(M - U * V)
while err > 1e-4:
    for i in range(0, U.shape[0]):
        for j in range(0, V.shape[1]):
            print("U[i, 0]={} M[i, j]={} V[0, j]={}", U[i,0], M[i,j], V[0,j])

            eij = np.abs(M[i, j] - U[i, 0] * V[0, 1])

            U[i, 0] = U[i, 0] + alfa * eij * V[0, j]
            V[0, j] = V[0, j] + alfa * eij * U[i, 0]

    err = np.linalg.norm(M - U * V)
