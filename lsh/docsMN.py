b = [1, 2, 3, 4, 6, 8, 12, 24]
r = b[:]
r.reverse()

c = int(input("ingresar c"))

fp = 0
fn = 0
N = 0.5
M = c * N if c > 0 else 0.2

for i in range(0, len(b)):
	fp = 1 - (1 - M**r[i])**b[i]
	fn = 1 - (1 - (1 - N)**r[i])**b[i]
	print("b={0}, r={1}, fp: {2} fn: {3}".format(b[i], r[i], fp, fn))
	
