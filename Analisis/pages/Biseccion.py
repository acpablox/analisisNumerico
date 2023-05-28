import pandas as pd
import numpy as np
import math
import streamlit as st
#import wdb
#wdb.set_trace()

# Parámetros
Xi = st.number_input('Ingreae el valor de a')
Xs = st.number_input('Ingrese el valor de b')
Tol = st.number_input('Ingrese el valor de la tolerancia (Mayor que 0 y menor que 1)')
Niter = st.number_input('Ingrese la cantidad de iteraciones')
Fun = st.text_input('Ingrese la función')
# Inicia el método de bisección
fm=[]
E=[]
x=Xi
fi=eval(Fun)
x=Xs
fs=eval(Fun)

if fi==0:
	s=Xi
	E=0
	st.write(str(Xi), "es raiz de f(x)")
elif fs==0:
	s=Xs
	E=0
	st.write(str(Xs), "es raiz de f(x)")
elif fs*fi<0:
	c=0
	Xm=(Xi+Xs)/2
	x=Xm                 
	fe=eval(Fun)
	fm.append(fe)
	E.append(100)
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
		x=Xm 
		fe=eval(Fun)
		fm.append(fe)
		Error=abs(Xm-Xa)
		E.append(Error)
		c=c+1
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



