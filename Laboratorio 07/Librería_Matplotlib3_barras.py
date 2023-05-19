# Crear un gráfico lineal 02
import numpy as np
import matplotlib.pyplot as plt

# Definir datos
x1=[3, 4, 5, 6]
y1=[5, 6, 3, 4]
x2=[2, 5, 8]
y2=[3, 4, 3]

# Aplicar configuración de características del gráfico
plt.bar(x1, y1, label='linea 1', linewidth=4, color='blue')
plt.bar(x2, y2, label='linea 2', linewidth=4, color='green')

# Definiendo el título y nombres de los ejes
plt.title('Diagrama de barras')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')

# Mostrar leyenda, cuadrícula y figura(gráfica)
plt.legend()
plt.grid()
plt.show()