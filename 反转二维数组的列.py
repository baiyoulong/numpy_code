import numpy as np

arr = np.arange(9).reshape(3,3)
b = arr[:,::-1]
print(b)