import numpy as np

np.random.seed(100)
a = np.random.randint(1, 10, [5, 3])

np.amax(a, axis=1)
b = np.apply_along_axis(np.max, arr=a, axis=1)
print(b)

c = np.apply_along_axis(lambda x:np.min(x)/np.max(x), arr=a, axis=1)
print(c)