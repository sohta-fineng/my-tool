import numpy as np

A = np.array([[1, 3, -5], [-4, 6, 2]])
B = np.array([[2, -3], [-1, 4], [5, 6]])

print((A @ B).T,
      (B.T) @ (A.T),
      sep = '\n')