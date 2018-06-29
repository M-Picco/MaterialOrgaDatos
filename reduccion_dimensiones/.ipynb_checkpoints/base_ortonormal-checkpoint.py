import numpy as np

v = np.array([2/7, 3/7, 6/7])
#A = np.matrix([[1.125, .5, -.625], [.702, -.702, .117], [.890, -.346, -.297], [.312, .156, -.937]])
#A = np.matrix([[2.250, -.500, -.750], [.608, -.459, -.119], [-.937, .312, .156], [-.288, -.490, .772]])
A = np.matrix([[2.250, -.500, -.750], [.702, -.702, .117], [1.125, .500, -.625], [.975, .700, -.675] ])

for i in range(0, A.shape[0]):
	u = np.asarray(A)[i]
	res = np.dot(v, u)
	if (res < 1e-5) and (np.isclose(np.linalg.norm(u), 1, atol=0.01)):
		print(u)
		break
