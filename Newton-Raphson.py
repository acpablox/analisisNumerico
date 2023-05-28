import streamlit as st
import pandas as pd
import numpy as np
import math
#import wdb
#wdb.set_trace()
st.header('Método de Newton - Raphson')
# Parámetros
X0 = st.number_input('X0')
Tol = st.number_input('Tolerancia (mayor que 0 y menor que 1)')
Niter = st.number_input('Número de iteraciones')
Fun = st.text_input('Ingrese la función')
df = st.text_input('Ingrese la derivada de la función anterior')

# Comienza el método de Newton - Raphson
fn=[]
xn=[]
E=[]
N=[]
x=X0
f=eval(Fun)
derivada=eval(df)
c=0
Error=100               
fn.append(f)
xn.append(x)
E.append(Error)
N.append(c)
while Error>Tol and f!=0 and derivada!=0  and c<Niter:
  x=x-f/derivada
  derivada=eval(df)
  f=eval(Fun)
  fn.append(f)
  xn.append(x)
  c=c+1
  Error=abs(xn[c]-xn[c-1])
  N.append(c)
  E.append(Error)
if f==0:
    s=x
    st.write(str(s)+'es raíz de f(x)')
    print(s,"es raiz de f(x)")
elif Error<Tol:
    s=x
    st.write(str(s)+' es una aproximación de una raiz de f(x) con una tolerancia de '+str(Tol))
    print("N",N)
    print("xn",xn)
    print("fn",fn)
    print("Error",E)
else:
    s=x
    st.write('Fracasó en '+str(Niter)+' iteraciones')

d = {'Iteración': N,'Xn':xn,'fn':fn,'Error':E}
tabla = pd.DataFrame(data = d)
st.table(tabla)