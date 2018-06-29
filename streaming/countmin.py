import numpy as np

S = [2,3,1,8,6,4,9,7,10,6]

h = lambda a, x: (a * x) % 7

M = np.zeros((3, 7))

for s in S:
    M[0, h(2, s)] += 1
    M[1, h(3, s)] += 1
    M[2, h(4, s)] += 1

print(M)

def E(x):
    t = [M[0, h(2, x)], M[1, h(3, x)], M[2, h(4, s)]]
    print("E({}) = {}".format(x, int(min(t))))
    
for i in range(1, 11):
    E(i)