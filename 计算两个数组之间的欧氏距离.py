import numpy as np

a = np.arange(1,6)
print(a)
b = np.arange(4,9)
print(b)

dist = np.linalg.norm(a - b)
print(dist)