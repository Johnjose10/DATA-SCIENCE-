import numpy as np
A= np.array([[2,3],[1,2]])
print(A)
U,S,VT=np.linalg.svd(A)
print("left singular matrix")
print(U)
print("singular matrix")
print(S)
print("right singular matrix")
print(VT)
sigma = np.zeros(((A.shape[0],A.shape[1])))
print(sigma)
np.fill_diagonal(sigma,S)
print(sigma)
B=U.dot(sigma.dot(VT))
print("reconstructer matrix:\n",B)



********OUTPUT*********

= RESTART: C:/Users/mlm/Desktop/mat.py
[[2 3]
 [1 2]]
left singular matrix
[[-0.85065081 -0.52573111]
 [-0.52573111  0.85065081]]
singular matrix
[4.23606798 0.23606798]
right singular matrix
[[-0.52573111 -0.85065081]
 [-0.85065081  0.52573111]]
[[0. 0.]
 [0. 0.]]
[[4.23606798 0.        ]
 [0.         0.23606798]]
reconstructer matrix:
 [[2. 3.]
 [1. 2.]]
