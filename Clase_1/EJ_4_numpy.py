import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('datostabla.txt', dtype=float)
#print(data)

#Gráficos

N=10
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2
plt.scatter(data[:,0], data[:,1],s=area, c=colors, alpha=0.5)
plt.xlabel('X', fontsize=10)
plt.ylabel('Y', fontsize=10)
plt.title('Prueba Scatter')
plt.grid()
plt.show()