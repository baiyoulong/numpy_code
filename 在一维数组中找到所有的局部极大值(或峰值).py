import numpy as np

a = np.array([1,3,7,1,2,6,0,1])
doublediff = np.diff(np.sign(np.diff(a)))
peak_locations = np.where(doublediff == -2)[0] + 1
print(peak_locations)