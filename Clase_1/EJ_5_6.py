import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('datostabla.txt', dtype=float)

x = np.array(data[:,0])
y = np.array(data[:,1])
l = len(x)
sumax = sum(x)
sumay = sum(y)
sigmax2 = sum(x*x)
sigmay2 = sum(y*y)
sigmaxy = sum(x*y)
prox = sumax/l
proy = sumay/l
m = (sumax*sumay - l*sigmaxy)/(sumax**2-l*sigmax2)
b = proy - m*prox

plt.plot(x, y, "o", label='Datos tabla')
plt.plot(x, m*x+b, label='Ajuste lineal')
plt.xlabel('X', fontsize=10)
plt.ylabel('Y', fontsize=10)
plt.title('Prueba ajuste')
plt.grid()
plt.legend()
plt.show()
