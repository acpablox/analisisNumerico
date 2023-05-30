import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from sympy import symbols
st.header('Método de diferencias divididas')

xString = st.text_input('Ingrese las coordenadas de x')
yString = st.text_input('Ingrese las coordenadas de y')
x = np.fromstring(xString, dtype = float, sep = ' ')
y = np.fromstring(yString, dtype = float, sep = ' ')
n = len(x)
size = n-1
tabla = np.zeros((n, n+1))
tabla[:, 0] = x
tabla[:, 1] = y

for i in range(1, n):
    for j in range(2, n+1):
        if tabla[i][j-1] == 0 or tabla[i-1][j-1] == 0:
            tabla[i][j] = 0
            continue
        tabla[i][j] = (tabla[i][j-1]-tabla[i-1][j-1])/(x[j-1]-tabla[0][0])
st.write('Tabla de diferencias divididas')
st.write(tabla)

tamano = len(tabla)
coef=[]
for i in range(tamano):
    p = list(tabla[i])
    k = p[i+1]
    coef.append(k)
print(coef)


n = len(x)
pol = np.ones(1)
acum = pol
pol = coef[0] * acum

for i in range(n-1):
    pol = np.concatenate(([0], pol))
    acum = np.convolve(acum, [1, -x[i]])
    pol = pol + coef[i+1] * acum
st.write('Coeficientes:')
st.write(pol)

funcion = ''
for i in range(size):
    if pol[i] >= 0:
        funcion += '+'+str(pol[i])+'*x^'+str(size-i)+' '
    else:
        funcion += str(pol[i])+'*x^'+str(size-i)+' '
if pol[len(pol)-1] >= 0:
    funcion += '+'+str(pol[len(pol)-1])
else:
    funcion += str(pol[len(pol)-1])

st.write('Polinomio:')
st.write(funcion)

x_values = np.linspace(x[0], x[-1], 100)  # Generate 100 points between x[0] and x[-1]

x_sym = symbols('x')
y_sym = eval(funcion.replace('^', '**').replace('x', 'x_sym')).evalf()

fig, ax = plt.subplots()
ax.plot(x_values, [y_sym.subs(x_sym, x_val) for x_val in x_values], label='Funcion')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
ax.grid(True)
st.pyplot(fig)
