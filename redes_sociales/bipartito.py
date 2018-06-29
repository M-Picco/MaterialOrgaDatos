import numpy as np

A = [0, 1, 2, 3, 4, 5]
B = [0, 1, 2, 3, 4, 5]

dic = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: []
}

for i in A:
    for j in B:
        if (i - j) % 2 == 0 or (i - j) % 3 == 0:
            dic[i].append(j)
            #print("%d %d" % (i, j))

# for k in dic:
#     print("{0}: {1}".format(k, dic[k]))
pairs = [(3,4), (0,3), (1,3), (0,1)]

for t in pairs:
    intersection = np.intersect1d(dic[t[0]], dic[t[1]])
    print("{0} {1}: {2}".format(t[0], t[1], intersection))