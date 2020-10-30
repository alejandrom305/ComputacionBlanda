#Función de Membresía Sigmoide

import numpy as np
import skfuzzy as sk
import matplotlib.pyplot as plt

#se define la variable independiente
x = np.arange(-11, 11, 1)

#se define la variable dependiente sigmoide de membresía
vd_sigmoide= sk.sigmf(x, 0, 1)

#se grafica la función membresía
plt.figure()
plt.plot(x, vd_sigmoide, 'b', linewidth=1.5, label='Servicio')

plt.title('Calidad del servicio en un Restaurante')
plt.ylabel('Membresía')
plt.xlabel("Nivel de Servicio")
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), ncol=1, fancybox=True, shadow=True)
plt.show()