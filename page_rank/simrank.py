import numpy as np

b = 0.7
A = np.array([[0  , 0  , 0  , 1/2, 0],
              [1/3, 0  , 1/2, 1/2, 0],
              [1/3, 1/2, 0  , 0  , 1],
              [1/3, 1/2, 0  , 0  , 0],
              [0  , 0  , 1/2, 0  , 0]])

tpr = np.array([[1], [0], [0], [0], [0]])
pr = np.empty((5, 1))
pr_prev = np.zeros((5, 1))

while not np.allclose(pr, pr_prev):
    pr_prev = pr
    pr = b * A.dot(pr) + (1 - b) * tpr

print("SIMPR(A): %f" % (pr[0]))
print("SIMPR(B): %f" % (pr[1]))
print("SIMPR(C): %f" % (pr[2]))
print("SIMPR(D): %f" % (pr[3]))
print("SIMPR(E): %f" % (pr[4]))