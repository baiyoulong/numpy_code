import numpy as np

def maxx(x, y):
    if x >y:
        return x
    else:
        return y

pair_max = np.vectorize(maxx, otypes=[float])

a = np.array([5,7,9,8,6,4,5])
b = np.array([6,3,4,8,9,7,1])

c = pair_max(a,b)
print(c)
