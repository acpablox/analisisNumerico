import streamlit as st
import pandas as pd
import numpy as np
import math
#import wdb
#wdb.set_trace()it as st

a = st.number_input('Ingrese el valor de a')
b = st.number_input('Ingrese el valor de b')
tol = st.number_input('Ingrese el valor de la tolerancia (Mayor de 0 y menor de 1)')
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
        continue
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

    
    E = abs(xiNew - xi)
    Error.append(E)

    n = n + 1
    N.append(n)
if tol > E:
    st.write(xi,' es una aproximacion de la raiz de f(x)')
else:
    st.write('Fracasó en ',niter,' iteraciones')

st.write(N,Error,xn,fn)

d = {'Iteración': N,'Xn':xn,'fn':fn,'Error':Error}
tabla = pd.DataFrame(data = d)
st.table(tabla)