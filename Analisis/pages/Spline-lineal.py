import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
xString = st.text_input('Ingrese las coordenadas de x')
yString = st.text_input('Ingrese las coordenadas de y')

x = np.fromstring(xString, dtype = float, sep = ' ')
y = np.fromstring(yString, dtype = float, sep = ' ')

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

# Valores de x
xpol = np.linspace(x[0], x[-1], 100)

# Evaluate the interpolated function at x values
yInt = np.zeros_like(xpol)
for i in range(len(x) - 1):
    idx = (xpol >= x[i]) & (xpol <= x[i + 1])
    xintervalo = xpol[idx]
    yInt[idx] = Tabla[i, 0] * xintervalo + Tabla[i, 1]
'''
# Plot the data points and interpolated function
puntos = plt.plot(x, y, 'r*', label='Puntos')
funcion = plt.plot(xpol, yInt, 'g-', label='Funcion interpolada')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
'''
d = {'x':x,'y':y}
chart_data = pd.DataFrame(data=d)
st.line_chart(data = chart_data)

