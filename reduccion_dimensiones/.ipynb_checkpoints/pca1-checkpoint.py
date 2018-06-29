import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

A = np.matrix('1 6 2 3 2; 3 4 6 1 2; 5 1 10 4 2; 6 0 11 2 2')

# standarizo la informacion
std_A = np.matrix(StandardScaler().fit_transform(A.getA()))

# matriz de covarianza calculada para datos standard (equivale a https://en.wikipedia.org/wiki/Covariance_matrix#Correlation_matrix)
rows = np.size(A, 0)
cov_std_A = (std_A.transpose() * std_A) / (rows) 

print('cov_std_A')
print(cov_std_A)
