import numpy as np

np.set_printoptions(suppress=False)
np.random.seed(100)
rand_arr = np.random.random([3, 3])/1e3
print(rand_arr)

np.set_printoptions(suppress=True, precision=6)
print(rand_arr)