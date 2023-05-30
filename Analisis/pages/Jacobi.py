import numpy as np
import pandas as pd
import streamlit as st
import math
st.header('Método de Jacobi')
# Parámetros
Tol = st.number_input('Ingrese la tolerancia')
if Tol < 0 or Tol > 1:
    st.write('El valor de la tolerancia debe ser mayor a cero y menor que uno')
niter = st.number_input('Ingrese la cantidad de iteraciones')
Astring = st.text_input('Ingrese el vector a')
size = int(st.number_input('Ingrese el tamaño del vector A'))
bString = st.text_input('Ingrese el vector b')
x0string = st.text_input('Ingrese el valor inicial')
# Inicia el método de Jacobi
A = np.fromstring(Astring, dtype= float,sep=' ').reshape(size,size)
b = np.fromstring(bString, dtype = float, sep = ' ').reshape(size,1)
x0 = np.fromstring(x0string,dtype=float,sep=' ').reshape(size,1)
x0s = []
N = []
Err = []
c = 0
error = Tol + 1
D = np.diag(np.diag(A))
L = -np.tril(A, -1)
U = -np.triu(A, 1)
x0s.append(x0)
N.append(c)
Err.append(error)
while error > Tol and c < niter:
    Dinv = np.linalg.inv(D)
    LU = L+U
    T = np.matmul(Dinv,LU)
    C = np.matmul(Dinv,b)
    x1 = np.matmul(T,x0)+ C
    x0s.append(x1)
    E = np.linalg.norm(x1 - x0, ord=np.inf)
    error = E
    x0 = x1
    c += 1
    Err.append(error)
    N.append(c)
if error < Tol:
    s = x0
    n = c
    print('s =', s)
    print('es una aproximación de la solución del sistema con una tolerancia =', Tol)
else:
    s = x0
    n = c
    print('Fracasó en', niter, 'iteraciones')
print(Err,N,x0s)

max_len = max(len(N), len(Err), len(x0s))  
N.extend([np.nan] * (max_len - len(N)))
Err.extend([np.nan] * (max_len - len(Err)))
x0s.extend([np.full((size, 1), np.nan)] * (max_len - len(x0s)))
x0s_str = [str(arr) for arr in x0s]

d = {'Iteración': N, 'Xn': x0s_str, 'Error': Err}
tabla = pd.DataFrame(data=d)
st.table(tabla)
