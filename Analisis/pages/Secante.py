import streamlit as st
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
#import wdb
#wdb.set_trace()

st.header('Método de la Secante')

#Parámetros
a = st.number_input('Ingrese el valor de a')
b = st.number_input('Ingrese el valor de b')
tol = st.number_input('Ingrese la tolerancia (entre 0 y 1)')
if tol < 0 or tol > 1:
    st.write('La tolerancia debe ser mayor que cero y menor que uno')
niter = st.number_input('Ingrese la cantidad de iteraciones')
fun = st.text_input('Ingrese la función')
# Inicia el método de Secante
E = []
N = []
xn = []
fn = []
x0 = a
x1 = b
x = x0
eval0 = eval(fun)
x = x1
eval1 = eval(fun)
error = abs(x1 - x0)
c = 0
N.append(c)
E.append(error)
p = x1 - ((eval1) * (x1 - x0)) / (eval1 - eval0)
xn.append(p)
x = p
evalp = eval(fun)
fn.append(evalp)
while error > tol and c <= niter:
    x0 = x1
    x1 = p
    if c == 0:
        error = abs(x1-x0)
        E.append(error)
    x = x0
    eval0 = eval(fun)
    x = x1 
    eval1 = eval(fun)
    p = x1 - ((eval1) * (x1 - x0)) / (eval1 - eval0)
    x = p
    evalp = eval(fun)
    error = abs(p-x1)
    c = c+1
    N.append(c)
    E.append(error)
    xn.append(p)
    fn.append(evalp)
E.pop()
if error < tol:
    print(p,'es una aproximacion de la raiz de',fun)
else:
    print('Fracaso en',niter,'iteraciones')

    
xs = b + 2
xi = a -2
x_vals = np.linspace(xi, xs, 100)
y_vals = [eval(fun) for x in x_vals]

plt.plot(x_vals, y_vals,color = 'g',label = fun)
plt.axhline(y=0, color='r', linestyle='--')  
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfica de'+fun)
plt.grid(True)
plt.legend()
st.pyplot(plt)
    
    

st.subheader('TABLA')

d = {'Iteración': N,'Xn':xn,'fn':fn,'Error':E}
tabla = pd.DataFrame(data = d)
st.table(tabla)
