import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sympy as sy
st.title('Solución numérica de ecuaciones no lineales, solución de sistemas de ecuaciones e interpolación')

st.subheader('Esta página web fue diseñada con el fin de resolver problemas acerca de los diferentes temas tratados en el semestre de una manera intuitiva y clara, de tal manera que quien le dé uso tenga claridad de la solución obtenida y de sus errores en caso tal de tenerlos.')

st.write('A continuación se presentan los 3 temas con sus respectivos métodos:')

st.write('Métodos de solución de ecuaciones no lineales: ')
st.write('Bisección, Punto Fijo, Regla Falsa, Newton-Raphson, Secante y Raíces Múltiples')

st.write('Métodos de sistemas de ecuaciones:')
st.write('Jacobi, Gauss-Seidel y SOR')

st.write('Métodos de interpolación: ')
st.write('VanderMonde, Newton (Diferencias Divididas), Spline lineal y Spline Cúbico')
