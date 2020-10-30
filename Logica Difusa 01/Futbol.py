#Paquetes Requeridos
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
#%matplotlib inline

#Definiendo los rangos de velocidad de 0 a 80
x= np.arange(30, 80, 0.1)

#Definiendo las funciones miembro triangulares
lento = fuzz.trimf(x, [30, 30, 50])
medio = fuzz.trimf(x, [30, 50, 70])
medio_rapido = fuzz.trimf(x, [50, 60, 80])
rapido = fuzz.trimf(x, [60, 80, 80])

#Dibujando las funciones de membresía
plt.figure()
plt.plot(x, rapido, 'b', linewidth=1.5, label='Rapido')
plt.plot(x, medio_rapido, 'k', linewidth=1.5, label='Medio_Rapido')
plt.plot(x, medio, 'm', linewidth=1.5, label='Medio')
plt.plot(x, lento, 'r', linewidth=1.5, label='Lento')
plt.title('Penalti Difuso')
plt.ylabel('Membresía')
plt.xlabel("Velocidad (kilometros por Hora)")
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), ncol=1, fancybox=True, shadow=True)
plt.show()



