import streamlit as st
import pandas as pd
import numpy as np
import math
#import wdb
#wdb.set_trace()
st.header('Método de Punto Fijo')
# Parámetros
X0 = st.number_input('Ingrese el X0')
Tol = st.number_input('Ingrese la tolerancia (Mayor que 0 y menor que 1)')
Niter = st.number_input('Ingrese el número de iteraciones')
Fun = st.text_input('Ingrese la función f')
g = st.text_input('Ingrese la función g')

# Inicia el método de punto fijo
fn=[]
xn=[]
E=[]
N=[]
x=X0
f=eval(Fun)
c=0
Error=100               
fn.append(f)
xn.append(x)
E.append(Error)
N.append(c)
while Error>Tol and f!=0 and c<Niter:
	x=eval(g)
	fe=eval(Fun)
	fn.append(fe)
	xn.append(x)
	c=c+1
	Error=abs(xn[c]-xn[c-1])
	N.append(c)
	E.append(Error)	
if fe==0:
    s=x
    st.write(str(s)+" es raiz de f(x)")
elif Error<Tol:
    s=x
    st.write(str(s)+" es una aproximacion de un raiz de f(x) con una tolerancia "+ str(Tol))
    print("N",N)
    print("xn",xn)
    print("fn",fn)
    print("Error",E)
else:
    s=x
    st.write("Fracaso en "+ str(Niter)+ " iteraciones ") 

d = {'Iteración': N,'Xn':xn,'fn':fn,'Error':E}
tabla = pd.DataFrame(data = d)
st.table(tabla)
