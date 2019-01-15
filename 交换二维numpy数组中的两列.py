import numpy as np

a = np.arange(9).reshape(3,3)
b = a[:,[1,0,2]]
print(a)
print(b)