#Función de Membresía Trapezoidal

import numpy as np
import skfuzzy as sk
import matplotlib.pyplot as plt

#se define la variable independiente
x = np.arange(0, 11, 1)

#se define la variable dependiente trapezoidal de membresía
vd_trapezoidal= sk.trapmf(x, [0, 0, 5, 5])

#se grafica la función membresía
plt.figure()
plt.plot(x, vd_trapezoidal, 'b', linewidth=1.5, label='Servicio')

plt.title('Calidad del servicio en un Restaurante')
plt.ylabel('Membresía')
plt.xlabel("Nivel de Servicio")
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), ncol=1, fancybox=True, shadow=True)
plt.show()