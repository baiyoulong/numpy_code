import numpy as np

np.random.seed(100)
a = np.random.uniform(1,50,20)
print(a)

# Solution:
print(a.argsort())
# > [18 7 3 10 15]

# Solution 2:
b = np.argpartition(-a, 5)[:5]
print(b)
# > [15 10  3  7 18]

# Below methods will get you the values.
# Method 1:
c = a[a.argsort()][-5:]
print(c)

# Method 2:
d = np.sort(a)[-5:]
print(d)

# Method 3:
e = np.partition(a, kth=-5)[-5:]
print(e)

# Method 4:
f = a[np.argpartition(-a, 5)][:5]
print(f)