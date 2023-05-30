import pandas as pd
import numpy as np
import math
import streamlit as st
import matplotlib.pyplot as plt
#import wdb
#wdb.set_trace()
st.header('Método de Bisección')
# Parámetros
Xi = st.number_input('Ingrese el valor de a')
Xs = st.number_input('Ingrese el valor de b')
Tol = st.number_input('Ingrese el valor de la tolerancia (Mayor que 0 y menor que 1)')
if Tol < 0 or Tol > 1:
	st.write('Valor incorrecto de Tolerancia')
Niter = st.number_input('Ingrese la cantidad de iteraciones')
Fun = st.text_input('Ingrese la función')
# Inicia el método de bisección
fm=[]
E=[]
x=Xi
fi=eval(Fun)
x=Xs
fs=eval(Fun)
N = []
xm = []
if fi==0:
	N = [0]
	s=Xi
	xm.append(Xi)
	E=[1]
	fm.append(fi)
	st.write(str(Xi), "es raiz de f(x)")
elif fs==0:
	N = [0]
	s=Xs
	xm.append(Xs)
	E = [1]
	fm.append(fs)
	st.write(str(Xs), "es raiz de f(x)")
elif fs*fi<0:
	c=0
	N.append(c)
	Xm=(Xi+Xs)/2
	xm.append(Xm)
	x=Xm                 
	fe=eval(Fun)
	fm.append(fe)
	E.append(1)
	while E[c]>Tol and fe!=0 and c<Niter:
		if fi*fe<0:
			Xs=Xm
			x=Xs                 
			fs=eval(Fun)
		else:
			Xi=Xm
			x=Xi
			fs=eval(Fun)
		Xa=Xm
		Xm=(Xi+Xs)/2
		xm.append(Xm)
		x=Xm 
		fe=eval(Fun)
		fm.append(fe)
		Error=abs(Xm-Xa)
		E.append(Error)
		c=c+1
		N.append(c)
	if fe==0:
		s=x
		st.write(str(s)," es raiz de f(x)")
	elif Error<Tol:
		s=x
		st.write(str(s)," es una aproximacion de un raiz de f(x) con una tolerancia ", str(Tol))
		print("Fm",fm)
		print("Error",fm)
	else:
		s=x
		st.write("Fracaso en ",str(Niter), " iteraciones ") 
else:
	st.write("El intervalo es inadecuado")

# Create a range of x values for the graph
xs = Xs +100
xi = Xi -100
x_vals = np.linspace(xi, xs, 100)
y_vals = [eval(Fun) for x in x_vals]

# Plot the function graph
plt.plot(x_vals, y_vals)
plt.axhline(y=0, color='r', linestyle='--')  # Add x-axis line
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph of f(x)')
st.pyplot(plt)

	
d = {'Iteración': N,'Xn':xm,'fn':fm,'Error':E}
tabla = pd.DataFrame(data = d)
st.table(tabla)
