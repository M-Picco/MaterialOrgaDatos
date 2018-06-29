def h(x):
    return (3 * x + 7) % 11

for i in range(1, 11):
    print("{:2}: {}".format(i, bin(h(i))[2:].zfill(4)))