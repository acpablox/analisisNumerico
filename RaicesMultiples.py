import streamlit as st
import numpy as np
import pandas as pd
import math
import sympy as sp
# Parámetros
a = int(input('Ingrese el valor de a'))
tol = float(input('Ingrese el valor de la tolerancia (entre 0 y 1)'))
niter = int(input('Ingrese la cantidad de iteraciones'))
f = input('Ingrese la funcion')
# Inicia el método de raíces múltiples
x = sp.symbols('x')
fun = sp.sympify(f)
E =[]
N = []
xn = []
fn = []

x0 = a
x1 = 0
eval0 = fun.subs(x,x0)
dfun = fun.diff(x)
eval1 = dfun.evalf(subs = {x:x0})
d2fun = dfun.diff(x)
eval2 = d2fun.evalf(subs = {x:x0})
error = 1
E.append(error)
c = 0
N.append(c)
xn.append(x0)
fn.append(eval0)
while error > tol and c<=niter:
    x1 = x0 - (eval0*eval1)/((eval1**2)-eval0*eval2)
    error = abs(x1-x0)
    x0 = x1
    eval0 = fun.evalf(subs = {x:x0})
    eval1 = dfun.evalf(subs={x:x0})
    eval2 = d2fun.evalf(subs={x:x0})
    c += 1
    E.append(error)
    N.append(c)
    xn.append(x0)
    fn.append(eval0)
if error<=tol:
    print(x1,'es una aproximacion de la raiz multiple')
else:
    print('Fracaso en',niter,'iteraciones')
print(E,N,xn,fn)
