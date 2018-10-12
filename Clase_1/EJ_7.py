import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy.misc import derivative

x = sp.Symbol('x')
def funcion(x):
   return x**3+x**2-4*x+4

def der(x):
   return derivative(funcion, x)


#datosDerivada = open("datosDerivada.txt", 'w')
#datos = der(x)

#np.savetxt(datosDerivada, datos, fmt='%f', header='d/dx')

a = np.linspace(-10, 10)
plt.plot(a, funcion(a),'c', label='Función')
plt.plot(a, der(a),'m', label='Derivada')

plt.xlabel('X', fontsize=10)
plt.ylabel('Y', fontsize=10)
plt.title('Polinomio y Derivada')
plt.grid()
plt.legend()
plt.show()

