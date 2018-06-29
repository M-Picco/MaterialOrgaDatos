import numpy as np

def calcular_clusteroide(cluster):
    sumdistmin, imin = 9999, -1
    for i, c in enumerate(cluster):
        sumdist = 0
        for p in cluster:
            sumdist += np.linalg.norm(p - c) ** 2
        if sumdist < sumdistmin:
            sumdistmin = sumdist
            imin = i
    return (imin, cluster[imin])

a = np.array([[1, 6]])
b = np.array([[3, 7]])
c = np.array([[4, 3]])
d = np.array([[7, 7]])
e = np.array([[8, 2]])
f = np.array([[9, 5]])

print('{{a,b,c,d}}: {0}, {1}'.format(*calcular_clusteroide([a, b, c, d])))
print('{{c,d,e,f}}: {0}, {1}'.format(*calcular_clusteroide([c, d, e ,f])))
print('{{b,c,d,e}}: {0}, {1}'.format(*calcular_clusteroide([b, c, d, e])))
print('{{c,d,e,f}}: {0}, {1}'.format(*calcular_clusteroide([c, d, e, f])))
print('{{a,b,e,f}}: {0}, {1}'.format(*calcular_clusteroide([a, b, e, f])))

