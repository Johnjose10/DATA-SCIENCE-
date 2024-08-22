import numpy as np
n=np.random.randint(20,size=(2,2))
print(n)

print("determinant")
print(np.linalg.det(n))

print("inverse")
print(np.linalg.inv(n))

print("matrix Rank")
print(np.linalg.matrix_rank(n))


*******OUTPUT*******


PS C:\Users\mlm> & "C:/Program Files/Python312/python.exe" c:/Users/mlm/Desktop/JOHN/randomvalue.py
[[14  3]
 [ 7 10]]
determinant
118.99999999999993
inverse
[[ 0.08403361 -0.02521008]
 [-0.05882353  0.11764706]]
matrix Rank
2
PS C:\Users\mlm> 
