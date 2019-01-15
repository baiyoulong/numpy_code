import numpy as np

a = np.arange(15)

# method 1
index = np.where((a >= 5) & (a <= 10))
# print(index)
b = a[index]
print(a)
print(b)

# method 2
index = np.where(np.logical_and(a>=5, a<=10))
c = a[index]
print(c)

# method 3
d = a[(a >= 5) & (a <= 10)]
print(d)