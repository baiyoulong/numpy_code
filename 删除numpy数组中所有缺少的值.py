import numpy as np

a = np.array([1,2,3,np.nan,5,6,7,np.nan])
b = a[~np.isnan(a)]
print(b)