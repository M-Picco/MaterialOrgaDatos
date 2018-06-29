import numpy as np

def minkowsky(x, y, p):
	if len(x) != len(y):
		raise Error('different size')
	if p == 0:
		raise Error('p = 0')	

	acum = 0
	for i in range(0, len(x)):
		acum += np.abs(x[i] - y[i]) ** p

	return acum ** (1/float(p))

def cosine(x, y):
	cos_x_y = x.dot(y) / (np.abs(x) * np.abs(y))
	return 1 - np.cos(x, y)

v1 = [-0.03523597, 0.32230245, -0.12863445, -0.05499823, 0.44394174, -0.64023494]
v2 = [-0.42261242, -0.94746882, -0.42385565, -0.57185003, 0.30857046, -0.06489488]
v3 = [0.64302075, 0.42868685, 0.30156031, -0.69333788, -0.32130466, -0.12057523]
v4 = [0.83048764, -0.31629304, -0.29266495, -0.83020893, 0.81144827, 0.27869104]
v5 = [-0.291947, 0.47880295, -0.20378554, -0.45709396, -0.56440462, -0.40772986]

mink_12 = minkowsky(v1, v2, 0.25)
print('minkowsky p=0.25 v1 y v2 {0}'.format(mink_12))
