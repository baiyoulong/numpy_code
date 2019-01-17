import numpy as np

x = np.array([1, 2, 1, 1, 3, 4, 3, 1, 1, 2, 1, 1, 2])
n = 5

# method1
a = [i for i, v in enumerate(x) if v == 1][n-1]
print(a)

b = np.where(x == 1)[0][n-1]
print(b)