import numpy as np

N = 4

b = 0.7

A = np.array([[0  , 1, 0, 0],
              [0.5, 0, 0, 0],
              [0.5, 0, 0, 1],
              [0  , 0, 1, 0]])

tpr = np.array([[2/3], [1/3], [0], [0]])
pr = np.ones((4, 1)) / 4
pr_prev = np.zeros((4, 1))

while not np.allclose(pr, pr_prev):
    pr_prev = pr
    pr = b * (A.dot(pr)) + (1 - b) * tpr

print("TSPR(2): %f" % (pr[1]))
print("TSPR(4): %f" % (pr[3]))
print("TSPR(3): %f" % (pr[2]))
print("TSPR(1): %f" % (pr[0]))