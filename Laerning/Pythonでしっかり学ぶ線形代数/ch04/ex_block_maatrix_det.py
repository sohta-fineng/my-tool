import numpy as np
import numpy.linalg as LA

A = np.random.uniform(low =  -10, high = 10, size = (2, 2))

rng = np.random.default_rng()
B = rng.uniform(low = -10, high = 10, size = (2, 2))
C = rng.uniform(low = -10, high = 10, size = (2, 2))

O = np.zeros((2, 2))

M = np.block([[A, C], [O, B]])

print('A=', A, 'B=', B, 'C=', C, 
      'M=', M,
      'det(M)=', LA.det(M),
      '=', LA.det(A)*LA.det(B),
      sep = '\n')