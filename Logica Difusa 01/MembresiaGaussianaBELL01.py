#Función de Membresía Gaussiana BELL

import numpy as np
import skfuzzy as sk
import matplotlib.pyplot as plt

#se define la variable independiente
x = np.arange(0, 11, 0.6)

#se define la variable dependiente gaussiana de membresía
vd_gaussiana_bell= sk.gbellmf(x, 2, 3, 5)

#se grafica la función membresía
plt.figure()
plt.plot(x, vd_gaussiana_bell, 'b', linewidth=1.5, label='Servicio')

plt.title('Calidad del servicio en un Restaurante')
plt.ylabel('Membresía')
plt.xlabel("Nivel de Servicio")
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), ncol=1, fancybox=True, shadow=True)
plt.show()