import numpy as np

# method 1
rand_arr = np.random.randint(low=5, high=10, size=(5,3))+ np.random.random((5,3))
print(rand_arr)

# method 2
rand_arr = np.random.uniform(5, 10, size=(5,3))
print(rand_arr)