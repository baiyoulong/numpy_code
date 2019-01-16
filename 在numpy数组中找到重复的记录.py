import numpy as np

np.random.seed(100)
a = np.random.randint(0,5,10)
out = np.full(a.shape[0], True)
unique_positions = np.unique(a, return_index=True)[1]
out[unique_positions] = False
print(out)