## Crear un gráfico histograma
import numpy as np
import matplotlib.pyplot as plt

# Definir datos
x1 = [0.25, 1.25, 2.25, 3.25, 4.25]
y1 = [10, 55, 80, 32, 40]
x2 = [0.75, 1.75, 2.75, 3.75, 4.75]
y2 = [42, 26, 10, 29, 66]

# Aplicar configuración de características del gráfico
plt.scatter(x1, y1, label='Datos 1', color='red')
plt.scatter(x2, y2, label='Datos 2', color='purple')

# Definiendo el título y nombres d elos ejes
plt.title('Gráficos de dispersión')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')

# Mostrar leyenda y figura(gráfica)
plt.legend()
plt.show()