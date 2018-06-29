import numpy as np

A = np.array([[0  , 0, 1],
              [0.5, 0, 0],
              [0.5, 1, 0]])

pr = np.ones((3, 1))
pr_prev = np.zeros((3, 1))

steps = [pr]

while not np.allclose(pr, pr_prev):
    pr_prev = pr
    pr = A.dot(pr)
    steps.append(pr)

print("4ta iteracion")
print(steps[4])
print("5ta iteracion")
print(steps[5])
print("Convergencia:")
print(pr)