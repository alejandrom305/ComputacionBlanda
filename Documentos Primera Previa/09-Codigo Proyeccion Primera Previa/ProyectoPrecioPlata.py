import os
import math
from utils import DATA_DIR, CHART_DIR
import numpy as np

np.seterr(all='ignore')

import scipy as sp
import matplotlib.pyplot as plt

#leer el documento
data = np.genfromtxt(os.path.join(DATA_DIR, "precioplata.tsv"), delimiter="\t")

# Se establece el tipo de dato
data = np.array(data, dtype=np.float64)
print(data[:10])
print(data.shape)


colors = ['g', 'k', 'b', 'm', 'r']
linestyles = ['-', '-.', '--', ':', '-']
x = data[:, 0]
y = data[:, 1]



def plot_models(x, y, models, fname, mx=None, ymax=None, xmin=None):
    
    ''' dibujar datos de entrada '''
    # Crea una nueva figura, o activa una existente.
    # num = identificador, figsize: anchura, altura
    plt.figure(num=None, figsize=(8, 6))
    
    # Borra el espacio de la figura
    plt.clf()
    
    # Un gráfico de dispersión de y frente a x con diferentes tamaños y colores de marcador (tamaño = 10)
    plt.scatter(x, y, s=10)
    
    # Títulos de la figura
    # Título superior
    plt.title("Precio de la plata desde 2005 a 2020")
    
    # Título en la base
    plt.xlabel("Tiempo")
    
    # Título lateral
    plt.ylabel("Precio Plata ($)")

    # Titulo de la base de X
    plt.xticks(
        [w * 365 * 3 for w in range(10)], 
        ['Trienio %i' % w for w in range(10)])


    if models:
        if mx is None:
            mx = np.linspace(0, x[-1], 1000)
    
        for model, style, color in zip(models, linestyles, colors):
            # print "Modelo:",model
            # print "Coeffs:",model.coeffs

            plt.plot(mx, model(mx), linestyle=style, linewidth=2, c=color)

        plt.legend(["d=%i" % m.order for m in models], loc="upper left")

    plt.autoscale(tight=True)
    plt.ylim(ymin=0)
    if ymax:
        plt.ylim(ymax=ymax)
    if xmin:
        plt.xlim(xmin=xmin)
    plt.grid(True, linestyle='-', color='0.75')                 
    plt.savefig(fname)

#Primera mirada de datos
plot_models(x, y, None, os.path.join(CHART_DIR, "1400_01_01.png"))          

#Crea y dibuja los datos
fp1, res1, rank1, sv1, rcond1 = np.polyfit(x, y, 1, full=True)
print("Parámetros del modelo fp1: %s" % fp1)
print("Error del modelo fp1:", res1)
f1 = sp.poly1d(fp1)
fp2, res2, rank2, sv2, rcond2 = np.polyfit(x, y, 2, full=True)
print("Parámetros del modelo fp2: %s" % fp2)
print("Error del modelo fp2:", res2)
f2 = sp.poly1d(fp2)
f3 = sp.poly1d(np.polyfit(x, y, 3))
f10 = sp.poly1d(np.polyfit(x, y, 10))

#Graficar
plot_models(x, y, [f1], os.path.join(CHART_DIR, "1400_01_02.png"))
plot_models(x, y, [f1, f2], os.path.join(CHART_DIR, "1400_01_03.png"))

#Punto de inflexion para ajustar y dibujar
inflexion = math.floor(5 * 365 * 3)
xa = x[:int(inflexion)]
ya = y[:int(inflexion)]
xb = x[int(inflexion):]
yb = y[int(inflexion):]


#Se grafican 2 lineas rectas
fa = sp.poly1d(np.polyfit(xa, ya, 1))
fb = sp.poly1d(np.polyfit(xb, yb, 1))

plot_models(x, y, [fa, fb], os.path.join(CHART_DIR, "1400_01_05.png"))

#Función de error
def error(f, x, y):
    return np.sum((f(x) - y) ** 2)

#Desde las lineas siguientes, se imprimen los errores:
print("Errores para el conjunto completo de datos:")
for f in [f1, f2, f3, f10]:
    print("Error d=%i: %f" % (f.order, error(f, x, y)))

print("Errores solamente después del punto de inflexión")
for f in [f1, f2, f3, f10]:
    print("Error d=%i: %f" % (f.order, error(f, xb, yb)))

print("Error de inflexión=%f" % (error(fa, xa, ya) + error(fb, xb, yb)))



""" Se extrapola de modo que se proyecten una prediccion respuestas en el futuro """
plot_models(x, y, [f1, f2, f3, f10], 
    os.path.join(CHART_DIR, "1400_01_06.png"),
    mx=np.linspace(0 * 365 * 3, 8 * 365 * 3, 100),
    ymax=6000, xmin=0 * 365 * 3)                                    

print("Entrenamiento de datos únicamente despúes del punto de inflexión")
fb1 = fb
fb2 = sp.poly1d(np.polyfit(xb, yb, 2))
fb3 = sp.poly1d(np.polyfit(xb, yb, 3))
fb10 = sp.poly1d(np.polyfit(xb, yb, 10))

print("Errores después del punto de inflexión")
for f in [fb1, fb2, fb3, fb10]:
    print("Error d=%i: %f" % (f.order, error(f, xb, yb)))

# Gráficas después del punto de inflexión
plot_models(
    x, y, [fb1, fb2, fb3, fb10,],
    os.path.join(CHART_DIR, "1400_01_07.png"),
    mx=np.linspace(0 * 365 * 3, 8 * 365 * 3, 100),
    ymax=6000, xmin=0 * 365 * 3)

# Separa el entrenamiento de los datos de prueba
frac = 0.3
split_idx = int(frac * len(xb))
shuffled = sp.random.permutation(list(range(len(xb))))
test = sorted(shuffled[:split_idx])
train = sorted(shuffled[split_idx:])
fbt1 = sp.poly1d(np.polyfit(xb[train], yb[train], 1))
fbt2 = sp.poly1d(np.polyfit(xb[train], yb[train], 2))
print("fbt2(x)= \n%s" % fbt2)
print("fbt2(x)-5,000= \n%s" % (fbt2-5000))
fbt3 = sp.poly1d(np.polyfit(xb[train], yb[train], 3))
fbt10 = sp.poly1d(np.polyfit(xb[train], yb[train], 10))

print("Prueba de error para después del punto de inflexión")
for f in [fbt1, fbt2, fbt3, fbt10]:
    print("Error d=%i: %f" % (f.order, error(f, xb[test], yb[test])))

plot_models(
    x, y, [fbt1, fbt2, fbt3, fbt10],
    os.path.join(CHART_DIR, "1400_01_08.png"),
    mx=np.linspace(0 * 365 * 3, 8 * 365 * 3, 100),
    ymax=6000, xmin=0 * 365 * 3)

from scipy.optimize import fsolve
print(fbt2)
print(fbt2 - 5000)
alcanzado_max = fsolve(fbt3 - 5000, x0=800) / (365 * 3)
print("\nLa plata alcanzara el precio de 5,000 pesos por gramo en el Trienio %f" % alcanzado_max[0])

alcanzado_max2 = fsolve(fbt1 - 5000, x0=800) / (365 * 3)
print("\nLa plata alcanzara el precio de 5,000 pesos por gramo en el Trienio %f" % alcanzado_max2[0])