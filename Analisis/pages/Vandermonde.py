import numpy as np
import matplotlib.pyplot as plt

x = np.array([-2, -1, 2, 3])
y = np.array([12.13533528, 6.367879441,  -4.610943901,  2.085536923])
size = int(input('Ingrese el grado de la ecuación'))
Apro = []
for i in range(size,0,-1):
    p = list(x**i)
    Apro.append(p)
Apro.append(np.ones(len(x)))
A = np.column_stack(Apro)
b = y
Ainv = np.linalg.inv(A)
a = np.matmul(Ainv,b)
p = 0
xpol = np.arange(-2, 3.01, 0.01)
for i in range(size+1):
    p =+ a[i] * xpol**(size-i)
print(p)
p = a[0] * xpol**3 + a[1] * xpol**2 + a[2] * xpol + a[3]
print(p)
plt.plot(x, y, 'r*', label='Data Points')
plt.plot(xpol, p, 'g-', label='Polynomial Fit')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()