import numpy as np
from math import sqrt

puntos = [[28, 145], [65, 140], [50, 130], [55, 118], [38, 115], [50, 90], [63, 88], [43, 83], [50, 60], [50, 30]]
centroides = [(25, 125, []), (44, 105, []), (29, 97, []), (35, 63, []), (55, 63, []), (42, 57, []), (23, 40, []), (64, 37, []), (32, 22, []), (55, 20, [])]

def norm(u, v):
    dx = v[0] - u[0]
    dy = v[1] - u[1]
    return sqrt(dx**2 + dy**2)

def asignar_centroides(puntos, centroides):
    for p in puntos:
        dmin, imin = 9999, -1
        for i, c in enumerate(centroides):
            if norm(p, c) < dmin:
                dmin = norm(p, c)
                imin = i
        centroides[imin][2].append(p)

def recalcular_centroides(centroides):
    nuevos_centroides = []
    for c in centroides:
        accx, accy, n = c[0], c[1], len(c[2]) + 1
        for p in c[2]:
            accx += p[0]
            accy += p[1]
        nuevos_centroides.append((accx / n, accy / n, []))
    return nuevos_centroides
        
asignar_centroides(puntos, centroides)
print('Asigno puntos a centroides')
print(centroides)

nuevos_centroides = recalcular_centroides(centroides)

print('')

print('Centroides nuevos')
print(nuevos_centroides)        

print('')

print('Reasigno puntos a nuevos centroides')
#asignar_centroides(puntos, nuevos_centroides)
asignar_centroides([[65, 140]], nuevos_centroides)
print(nuevos_centroides)