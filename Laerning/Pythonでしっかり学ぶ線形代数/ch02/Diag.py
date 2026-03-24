import numpy as np

n = 3 #正方行列の次元数
I = np.eye(n) # 単位行列（Identity Matrix）:Iはeye(アイ)と発音されるからっていうオヤジなジョーク
J = np.eye(n, k = 1)
K = np.eye(n, k = -1)
A = np.arange(n**2).reshape((n,n))
d = np.diag(A)
B = np.diag(d)

print('I=', I, 'J=', J, 'K=', K, 'd=np.diag(A)=', d, 'np.diag(d)=', B,   
      sep = '\n')