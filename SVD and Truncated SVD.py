import numpy as np 
from scipy.linalg import svd 
X = np.array([[1, 2, 1, 2], [0, 1, 0, 1], [1, 0, 1, 0], [1, 2, 3, 4] ]) # SVD: X = U*s*V^T 
U, s, VT = svd(X)
recovered_X = U.dot(np.diag(s)).dot(VT) 
print('\n X = \n', X) 
print('\nU = \n', U) 
print('s = \n', s) 
print('VT = \n', VT)


