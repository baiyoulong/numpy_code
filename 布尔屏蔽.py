import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(0, 2 * np.pi, 50)
print(len(a))
b = np.sin(a)
# print(b)
plt.plot(a, b)
mask = b >= 0
# print(mask)
print(len(a[mask]))
plt.plot(a[mask], b[mask], 'bo')
mask = (b >= 0) & (a <= np.pi / 2)
plt.plot(a[mask], b[mask], 'go')
plt.show()