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
x0s.append(x0)
N.append(c)
Err.append(error)
while error > Tol and c < niter:
    DL = D-L
    DLinv = np.linalg.inv(DL)
    T = np.matmul(DLinv,U)
    C = np.matmul(DLinv,b)
    x1 = np.matmul(T,x0) + C
    x0s.append(x1)
    E = np.linalg.norm(x1 - x0, np.inf)
    error = E
    x0 = x1
    c += 1
    Err.append(error)
    N.append(c)
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