import numpy as np

np.set_printoptions(precision=2)
np.random.seed(100)
a = np.random.uniform(1,50,20)

np.clip(a, a_min=10, a_max=30)
print(np.where(a < 10, 10, np.where(a >30, 30, a)))