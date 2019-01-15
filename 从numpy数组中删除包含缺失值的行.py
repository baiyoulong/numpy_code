import numpy as np

# Input
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
iris_2d[np.random.randint(150, size=20), np.random.randint(4, size=20)] = np.nan

# Solution
# No direct numpy function for this.
# Method 1:
any_nan_in_row = np.array([~np.any(np.isnan(row)) for row in iris_2d])
a =iris_2d[any_nan_in_row][:5]
print(a)

# Method 2: (By Rong)
b = iris_2d[np.sum(np.isnan(iris_2d), axis = 1) == 0][:5]
print(b)