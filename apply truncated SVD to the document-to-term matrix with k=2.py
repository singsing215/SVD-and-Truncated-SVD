import numpy as np 
import matplotlib.pyplot as pt
from scipy.linalg import svd 

X = np.array([[1, 2, 1, 2], [0, 1, 0, 1], [1, 0, 1, 0], [1, 2, 3, 4] ]) # SVD: X = U*s*V^T 
U, s, VT = svd(X)
recovered_X = U.dot(np.diag(s)).dot(VT) 
print('\n X = \n', X) 

# Truncated SVD: to k dim 
#err = [0,0,0] 
k=2
recovered_X= U[:,:k].dot(np.diag(s)[:k,:k]).dot(VT [:k, :])
print("\n X_%d = \n" %k , recovered_X) 
    
'''
    print("norm(X,X%d) = %3.2f" %(k,np.linalg.norm(X-recovered_X))) 
    err[k-1] = np.linalg.norm(X-recovered_X);
pt.plot([1,2,3],err, "ro-") 
pt.bar([1,2,3],err) 
pt.xlabel("k - dimension") 
pt.ylabel("Norm(X,X_k)")
'''