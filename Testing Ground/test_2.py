import numpy as np



A = np.array(((0, 1),(0, 1)))
B = np.array((3, 4))

print(np.matmul(A, B.transpose()).transpose())

print(A)
