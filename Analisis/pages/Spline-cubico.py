import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

st.header('Spline Cúbico')

xString = st.text_input('Ingrese las coordenadas de x (en orden de mayor a menor)')
yString = st.text_input('Ingrese las coordenadas de y')

x = np.fromstring(xString, dtype = float, sep = ' ')
y = np.fromstring(yString, dtype = float, sep = ' ')

n = len(x)
A = np.zeros((4 * (n - 1), 4 * (n-1)))
b = np.zeros((4 * (n - 1), 1))
cua = x ** 2
cub = x ** 3
c = 0
h = 0
for i in range(n - 1):
    A[i, c] = cub[i]
    A[i, c + 1] = cua[i]
    A[i, c + 2] = x[i]
    A[i, c + 3] = 1
    b[i] = y[i]
    c += 4
    h += 1

c = 0

for i in range(1, n):
    A[h, c] = cub[i]
    A[h, c + 1] = cua[i]
    A[h, c + 2] = x[i]
    A[h, c + 3] = 1
    b[h] = y[i]
    c += 4
    h += 1

c = 0

for i in range(1, n - 1):
    A[h, c] = 3 * cua[i]
    A[h, c + 1] = 2 * x[i]
    A[h, c + 2] = 1
    A[h, c + 4] = -3 * cua[i]
    A[h, c + 5] = -2 * x[i]
    A[h, c + 6] = -1
    b[h] = 0
    c += 4
    h += 1

c = 0

for i in range(1, n - 1):
    A[h, c] = 6 * x[i]
    A[h, c + 1] = 2
    A[h, c + 4] = -6 * x[i]
    A[h, c + 5] = -2
    b[h] = 0
    c += 4
    h += 1

A[h, 0] = 6 * x[0]
A[h, 1] = 2
b[h] = 0
h += 1
A[h, c] = 6 * x[-1]
A[h, c + 1] = 2
b[h] = 0

val = np.linalg.inv(A) @ b
Tabla = np.reshape(val, (n - 1,4))
Tabla = np.transpose(Tabla)

st.write('La siguiente tabla muestra las funciones, donde la primera columna corresponde a los x y la segunda columna al término independiente')
st.subheader('TABLA')
st.write(Tabla)

xpol = np.linspace(min(x), max(x), 100)

yInt = np.zeros_like(xpol)
for i in range(len(x) - 1):
    idx = (xpol >= x[i]) & (xpol <= x[i + 1])
    xintervalo = xpol[idx]
    yInt[idx] = Tabla[i, 0] * xintervalo + Tabla[i, 1]
st.subheader('Gráfica')
fig, ax = plt.subplots()
puntos = ax.plot(x, y, 'r*', label='Puntos')
funcion = ax.plot(xpol, yInt, 'g-', label='Funcion interpolada')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
ax.grid(True)

st.pyplot(fig)
