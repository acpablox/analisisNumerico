import streamlit as st
import pandas as pd
import numpy as np
import math
#import wdb
#wdb.set_trace()
#Parámetros
a = int(input('Ingrese el valor de a'))
b = int(input('Ingrese el valor de b'))
tol = float(input('Ingrese la tolerancia (entre 0 y 1)'))
niter = int(input('Ingrese la cantidad de iteraciones'))
fun = input('Ingrese la función')
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
print(E,N,xn,fn)

'''
d = {'Iteración': N,'Xn':xn,'fn':fn,'Error':E}
tabla = pd.DataFrame(data = d)
st.table(tabla)
''' 
 