import numpy as np
from scipy.spatial.distance import cosine

def prom_global(mat):
    c, s = 0, 0
    for i in range(0, mat.shape[0]):
        for j in range(0, mat.shape[1]):
            if mat[i, j] != -1:
                c += 1
                s += mat[i,j]
    return s / c

def prom(arr):
    c, s = 0, 0
    for v in arr:
        if v != -1:
            c += 1
            s += v
    return s / c

A = np.array([[ 4, 5,-1, 5, 1, -1, 3, 2],
              [-1, 3, 4, 3, 1,  2, 1,-1],
              [ 2,-1, 1, 3,-1,  4, 5, 3.0]])

u = prom_global(A)

# promedios y desviaciones
u_usuarios = []
d_usuarios = []
for i in range(0, A.shape[0]):
    u_usuarios.append(prom(A[i, :]))
    d_usuarios.append(u - u_usuarios[i])
u_peliculas = []
d_peliculas = []
for j in range(0, A.shape[1]):
    u_peliculas.append(prom(A[:, j]))
    d_peliculas.append(u - u_peliculas[j])

# centro la matriz y calculo semejantes
A_centrada = A.copy()
for i in range(0, A_centrada.shape[0]):
    A_centrada[i, :] -= prom(A_centrada[i, :])
for j in range(0, A_centrada.shape[1]):
    A_centrada[:, j] -= prom(A_centrada[:, j])

sims = []
for col in A_centrada.T:
    sims.append(cosine(A_centrada[:, 0], col))

cols_semejantes = np.argsort(sims)[1:4]
sims_semejantes = np.sort(sims)[1:4]

print(sims)
print(cols_semejantes)
print(sims_semejantes)

cols_semejantes = [3, 6, 1]
sims = [sims[3], sims[6], sims[1]]

# desviacion de peliculas semejantes
acum = 0
for i in range(0, len(cols_semejantes)):
    j = cols_semejantes[i]
    s = sims_semejantes[i]

    acum += A[1, j] - (u + d_usuarios[1] + d_peliculas[j])

d_usuario_pelicula = acum / sum(sims)

r_usuario = u + d_usuarios[1] + d_peliculas[0] + d_usuario_pelicula

print('Rusuario = %f' % (r_usuario))