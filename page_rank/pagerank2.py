import numpy as np

b = 0.7
A = np.array([[0  , 0  , 0  , 1/2, 0],
              [1/3, 0  , 1/2, 1/2, 0],
              [1/3, 1/2, 0  , 0  , 0],
              [1/3, 1/2, 0  , 0  , 0],
              [0  , 0  , 1/2, 0  , 0]])

tpr = np.ones((5, 1)) / 5
pr = np.ones((5, 1))
pr_prev = np.zeros((5, 1))

steps = [pr]

while not np.allclose(pr, pr_prev):
    pr_prev = pr
    pr = b * A.dot(pr) + (1 - b) * tpr
    steps.append(pr)

print("1era iteracion")
print(steps[1])
print("Convergencia:")
print(pr)