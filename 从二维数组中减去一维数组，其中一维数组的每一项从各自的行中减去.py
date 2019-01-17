import numpy as np

a_2d = np.array([[3,3,3],[4,4,4],[5,5,5]])
b_1d = np.array([1,2,3])
print(a_2d - b_1d[:, None])