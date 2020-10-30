#Función de Membresía Triangular

import numpy as np
import skfuzzy as sk
import matplotlib.pyplot as plt

#se define un array x para el manejo del factor en un restaurante
x = np.arange(0, 11, 1)

#se define un array para la función miembro de tipo triangular
calidad = sk.trimf(x, [0, 5, 10])

#se grafica la función membresía
plt.figure()
plt.plot(x, calidad, 'b', linewidth=1.5, label='Servicio')

plt.title('Calidad del servicio en un Restaurante')
plt.ylabel('Membresía')
plt.xlabel("Nivel de Servicio")
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), ncol=1, fancybox=True, shadow=True)
plt.show()