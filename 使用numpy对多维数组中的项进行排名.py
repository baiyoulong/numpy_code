import numpy as np

np.random.seed(10)
a = np.random.randint(20, size=[2, 5])
print(a)
print(a.ravel().argsort().argsort().reshape(a.shape))