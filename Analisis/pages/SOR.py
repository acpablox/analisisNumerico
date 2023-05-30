import numpy as np
import pandas as pd
import streamlit as st
import math

st.header('Método SOR')

# Parámetros
Tol = st.number_input('Ingrese la tolerancia')
if Tol < 0 or Tol > 1:
    st.write('La tolerancia debe ser mayor que cero y menor que uno')
niter = st.number_input('Ingrese la cantidad de iteraciones')
Astring = st.text_input('Ingrese el vector a')
size = int(st.number_input('Ingrese el tamaño del vector A'))
bString = st.text_input('Ingrese el vector b')
x0string = st.text_input('Ingrese el valor inicial')
w = st.number_input('Ingrese el valor de w (entre 0 y 2)')
if w < 0 or w > 2:
    st.write('w debe ser mayor o igual que 0 y menor o igual que 2')
# Inicia el método de Gauss-Seidel
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
aux = 1-w
Err.append(error)
N.append(c)
x0s.append(x0)
while error > Tol and c < niter:
    wL = np.multiply(w,L)
    DwL = D - wL
    auxD = np.multiply(aux,D)
    wU = np.multiply(w,U)
    DwLinv = np.linalg.inv(DwL)
    auxDwU = auxD + wU
    wDwLinv = np.multiply(w,DwLinv)
    T = np.matmul(DwLinv,auxDwU)
    C = np.matmul(wDwLinv,b)
    x1 = np.matmul(T,x0) + C
    x0s.append(x1)
    E = np.linalg.norm(x1 - x0, np.inf)
    error = E
    x0 = x1
    c += 1
    N.append(c)
    Err.append(error)
if error < Tol:
    s = x0
    n = c
    print("x0 =", s)
    print("es el resultado con una tolerancia de  =", Tol)
else:
    s = x0
    n = c
    print("Fracasó en", niter, "iteraciones")
print(Err,N,x0s)
max_len = max(len(N), len(Err), len(x0s))  # Find the maximum length
# Pad the lists with NaN values to ensure they have the same length
N.extend([np.nan] * (max_len - len(N)))
Err.extend([np.nan] * (max_len - len(Err)))
x0s.extend([np.full((size, 1), np.nan)] * (max_len - len(x0s)))
x0s_str = [str(arr) for arr in x0s]

# Create the DataFrame
d = {'Iteración': N, 'Xn': x0s_str, 'Error': Err}
tabla = pd.DataFrame(data=d)
st.table(tabla)
