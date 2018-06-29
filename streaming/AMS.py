import numpy as np

MAX = 75

def gettimestamp(t):
    s = t % 10
    if s == 0:
        s = 10
    c = t // 10 
    if t % 10 != 0:
        c += 1
    return (t, s, c)
vals = [0] * 10
for i in range(1, MAX + 1):
    vals[i % 10] += 1
M2 = 0
for acumulado in vals:
    M2 += acumulado ** 2

print("M2: {}".format(M2))

# for i in range(0, 10):
#     timestamps = []
#     Ms = []
#     for j in range(0, 3):
#         x = np.random.randint(1, MAX + 1)
#         tupla = gettimestamp(x)
#         timestamps.append(tupla)
#         Ms.append((x * (2 * tupla[2] - 1)))
#     print("{}: med={} prom={} M2/med={} M2/prom={}".format(timestamps,  np.round(np.median(Ms), decimals=3), 
#                                                                         np.round(np.mean(Ms), decimals=3), 
#                                                                         np.round(M2 / np.median(Ms), decimals=3), 
#                                                                         np.round(M2 / np.mean(Ms), decimals=3)))

grupos = {
    'a': [4, 31, 72],
    'b': [14, 35, 42],
    'c': [17, 43, 51],
    'd': [5, 33, 67]
    # '0': [1, 33, 75],
    # '1': [30,40,50],
    # '2': [50, 60, 70],
    # '3': [10, 20, 30]
}

for k in grupos:
    vals = grupos[k]
    timestamps = []
    Ms = []
    for x in vals:
        tupla = gettimestamp(x)
        timestamps.append(tupla)
        Ms.append((x * (2 * tupla[2] - 1)))
    print("{}: med={} prom={} M2/med={} M2/prom={}".format(timestamps,  np.round(np.median(Ms), decimals=3), 
                                                                        np.round(np.mean(Ms), decimals=3), 
                                                                        np.round(M2 / np.median(Ms), decimals=3), 
                                                                        np.round(M2 / np.mean(Ms), decimals=3)))
