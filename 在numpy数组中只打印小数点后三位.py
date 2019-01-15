import numpy as np

rand_arr = np.random.random((5,3))
print(rand_arr)
rand_arr = np.random.random([5,3])
# print(rand_arr)
np.set_printoptions(precision=3)
b = rand_arr[:4]
print(b)