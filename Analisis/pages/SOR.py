import numpy as np
import pandas as pd
import streamlit as st
import math
# Parámetros
Tol = float(input('Ingrese la tolerancia'))
niter = int(input('Ingrese la cantidad de iteraciones'))
Astring = input('Ingrese el vector a')
size = int(input('Ingrese el tamaño del vector A'))
bString = input('Ingrese el vector b')
x0string = input('Ingrese el valor inicial')
w = float(input('Ingrese el valor de w (entre 0 y 2)'))
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
    print("s =", s)
    print("It is an approximation of the solution with a tolerance =", Tol)
else:
    s = x0
    n = c
    print("Failed after", niter, "iterations")
print(Err,N,x0s)