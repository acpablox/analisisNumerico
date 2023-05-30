import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.header('Método de VanderMonde')

xString = st.text_input('Ingrese las coordenadas de x (en orden de menor a mayor)')
yString = st.text_input('Ingrese las coordenadas de y')
x = np.fromstring(xString, dtype = float, sep = ' ')
y = np.fromstring(yString, dtype = float, sep = ' ')
size = int(st.number_input('Ingrese el grado de la ecuación'))
Apro = []
for i in range(size,0,-1):
    p = list(x**i)
    Apro.append(p)
Apro.append(np.ones(len(x)))
A = np.column_stack(Apro)
b = y
Ainv = np.linalg.inv(A)
a = np.matmul(Ainv,b)
print(a)
p = 0
xpol = np.arange(x[0], x[len(x)-1], 0.01)
for i in range(size+1):
    p += a[i] * xpol**(size-i)
funcion = ''
print(p)
for i in range(size,0,-1):
    funcion += str(a[size-i])+'x^'+str(i)+' '
if a[len(a)-1] != 0:
    funcion += str(a[len(a)-1])
st.write(funcion)
fig, ax = plt.subplots()
puntos = ax.plot(x,y,'r*',label='Puntos')
funcion = ax.plot(xpol,p,'g-',label='Funcion interpolada')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
ax.grid(True)
st.pyplot(fig)
