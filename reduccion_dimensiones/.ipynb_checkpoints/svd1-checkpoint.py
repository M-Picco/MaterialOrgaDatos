import numpy as np

A = np.matrix('3 1 1 0; 2 1 0 2; 3 3 0 1; 0 1 2 0; 2 0 2 2')

u, s, vt = np.linalg.svd(A)

print("u")
print(u)
print("s")
print(s)
print("v")
print(vt.transpose())
