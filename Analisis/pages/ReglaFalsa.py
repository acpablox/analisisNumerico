import streamlit as st
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
#import wdb
#wdb.set_trace()it as st
st.header('Método de Regla Falsa')

a = st.number_input('Ingrese el valor de a')
b = st.number_input('Ingrese el valor de b')
tol = st.number_input('Ingrese el valor de la tolerancia (Mayor de 0 y menor de 1)')
if tol < 0 or tol > 1:
    st.write('La tolerancia debe ser mayor que cero y menor que uno')
niter = st.number_input('Ingrese la cantidad de iteraciones')
f = st.text_input('Ingrese la función')

N = []
Error = []
xn = []
fn = []
E = 1
n = 0
x = a
evala = eval(f)
x = b
evalb = eval(f)
xi = ((a * evalb) - (b * evala)) / (evalb - evala)
xa = xi
x = xi
evalxi = eval(f)
N.append(n)
xn.append(xi)
fn.append(evalxi)
Error.append(E)

if evalxi >= evala:
    if evalxi <= evalb:
        a = xi
    else:
        aux = b
        b = xi
        a = aux
else:
    a = a
    b = b

while tol < E and niter > n:
    x = a
    evala = eval(f)
    x = b
    evalb = eval(f)
    xi = ((a * evalb) - (b * evala)) / (evalb - evala)
    x = xi
    evalxi = eval(f)
    xn.append(xi)
    fn.append(evalxi)
    if n == 0:
        E = abs(xa-xi)
        Error.append(E)
    else:
        E = abs(xn[n] - xn[n - 1])
        Error.append(E)
    if evalxi >= evala:
        if evalxi <= evalb:
            a = xi
        else:
            aux = b
            b = xi
            a = aux
    else:
        a = a
        b = b

    x = a
    evala = eval(f)
    x = b
    evalb = eval(f)
    xiNew = ((a * evalb) - (b * evala)) / (evalb - evala)
    n = n + 1
    N.append(n)
if tol > E:
    st.write(xi,' es una aproximacion de la raiz de f(x)')
else:
    st.write('Fracasó en ',niter,' iteraciones')

xs = b +1
xi = a -1
x_vals = np.linspace(xi, xs, 100)
y_vals = [eval(f) for x in x_vals]

plt.plot(x_vals, y_vals,color = 'g',label = f)
plt.axhline(y=0, color='r', linestyle='--') 
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfica de'+f)
plt.grid(True)
plt.legend()
st.pyplot(plt)

st.write('TABLA')

d = {'Iteración': N,'Xn':xn,'fn':fn,'Error':Error}
tabla = pd.DataFrame(data = d)
st.table(tabla)
