import numpy as np

x = np.arange(1, 13).reshape(4,3)
# print(x)
v = np.array([1,0,1])
y = np.empty_like(x)
# print(y)

for i in range(4):
    y[i, :] = x[i, :] + v

print(y)

x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = x + v  # Add v to each row of x using broadcasting
print(y)