### ALEJANDRO MARTINEZ CORRALES --- Código: 1093230409
import numpy as np

data = np.genfromtxt("web_traffic.tsv", delimiter="\t")
print(data[:10], '\n')
# Número de datos
print(data.shape)

# Se divide el array en dos vectores columnas: x, y
x = data[:,0]
y = data[:,1]
# Se muestran los valores en x, y
print(x, '\n')
print(y, '\n')

# Dimensión de los vectores x, y

print(x.ndim, '\n')
print(y.ndim, '\n')
# Elementos contenidos en los vectores x, y
print(x.shape, '\n')
print(y.shape)

# Investigamos el número de valores nan que contiene el vector y

print(np.sum(np.isnan(y)))

# Número de elementos en x, y, antes de ser comprimidos

print(x.shape, '\n')
print(y.shape, '\n')
# Se eliminan los elementos nan tanto de x como de y
x = x[~np.isnan(y)]
y = y[~np.isnan(y)]
# Se cuenta el número de elementos tanto de x como de y
print(x.shape, '\n')
print(x.shape, '\n')

import matplotlib.pyplot as plt
# Dibuja los puntos (x,y) con círculos de tamaño 10
plt.scatter(x, y, s=10)
# Títulos de la gráfica
plt.title("Tráfico Web en el último mes")
plt.xlabel("Tiempo")
plt.ylabel("Accesos/Hora")
plt.xticks([w*7*24 for w in range(10)],['semana %i' % w for w in range(10)])
plt.autoscale(tight=True)
# dibuja una cuadrícula punteada ligeramente opaca
plt.grid(True, linestyle='-', color='0.75')
# Muestra el gráfico
plt.show()