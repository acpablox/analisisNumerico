import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

x = np.array([-2,-1,2,3])
y = np.array([12,6,-4,2])

n = len(x)
A = np.zeros((2 * (n - 1), 2 * (n - 1)))
b = np.zeros((2 * (n - 1), 1))
cua = x ** 2
cub = x ** 3
c = 0
h = 0
for i in range(n - 1):
    A[i, c] = x[i]
    A[i, c + 1] = 1
    b[i] = y[i]
    c += 2
    h += 1
    
c = 0
for i in range(1, n):
    A[h, c] = x[i]
    A[h, c + 1] = 1
    b[h] = y[i]
    c += 2
    h += 1

val = np.linalg.inv(A) @ b
Tabla = np.reshape(val, (n - 1,2))
    

st.write(Tabla)

# Generate x values for plotting
x_vals = np.linspace(x[0], x[-1], 100)

# Evaluate the interpolated function at x values
y_interp = np.zeros_like(x_vals)
for i in range(len(x) - 1):
    idx = (x_vals >= x[i]) & (x_vals <= x[i + 1])
    x_interval = x_vals[idx]
    y_interp[idx] = Tabla[i, 0] * x_interval + Tabla[i, 1]

# Plot the data points and interpolated function
puntos = plt.plot(x, y, 'ro', label='Data Points')
funcion = plt.plot(x_vals, y_interp, 'g-', label='Interpolated Function')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

st.plotly_chart(puntos)