import numpy as np

x = np.array([-2.3, -1, 2, 3])
A = np.column_stack([x**3, x**2, x, np.ones(len(x))])

print(list(x**3))