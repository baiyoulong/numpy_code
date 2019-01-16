import numpy as np

np.random.seed(101)
arr = np.random.randint(1,4, size=6)
arr
# > array([2, 3, 2, 2, 2, 1])

# Solution:
def one_hot_encodings(arr):
    uniqs = np.unique(arr)
    out = np.zeros((arr.shape[0], uniqs.shape[0]))
    for i, k in enumerate(arr):
        out[i, k-1] = 1
    return out

a = one_hot_encodings(arr)
print(a)
# > array([[ 0.,  1.,  0.],
# >        [ 0.,  0.,  1.],
# >        [ 0.,  1.,  0.],
# >        [ 0.,  1.,  0.],
# >        [ 0.,  1.,  0.],
# >        [ 1.,  0.,  0.]])

# Method 2:
b = (arr[:, None] == np.unique(arr)).view(np.int8)
print(b)