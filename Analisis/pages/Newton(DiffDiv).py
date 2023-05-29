import numpy as np

x = np.array([1,1.2,1.4,1.6,1.8,2])
y = np.array([0.6747,0.8491,1.1214,1.4921,1.9607,2.5258])
n = len(x)
size = n-1
tabla = np.zeros((n, n+1))
tabla[:, 0] = x
tabla[:, 1] = y

for i in range(1, n):
    for j in range(2, n+1):
        if tabla[i][j-1] == 0 or tabla[i-1][j-1] == 0:
            tabla[i][j] = 0
            continue
        tabla[i][j] = (tabla[i][j-1]-tabla[i-1][j-1])/(x[j-1]-tabla[0][0])

print(tabla)

tamano = len(tabla)
coef=[]
for i in range(tamano):
    p = list(tabla[i])
    k = p[i+1]
    coef.append(k)
print(coef)


n = len(x)
pol = np.ones(1)
acum = pol
pol = coef[0] * acum

for i in range(n-1):
    pol = np.concatenate(([0], pol))
    acum = np.convolve(acum, [1, -x[i]])
    pol = pol + coef[i+1] * acum

print(pol)

funcion = ''
for i in range(size):
    funcion += str(pol[i])+'x^'+str(size-i)+' '
funcion += str(pol[len(pol)-1])
print(funcion)

