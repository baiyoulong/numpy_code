import numpy as np

dt64 = np.datetime64('2018-02-25 22:10:10')

from datetime import datetime
dt64.tolist()

dt64.astype(datetime)
print(dt64)