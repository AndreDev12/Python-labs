# Filtros con Pyllow (PIL)

# Importar el módulo "Image", luego con la función open()
# abrir la imagen, mediante la ruta asignada y colocar el
# formato de la imagen
# Al final utilizar la función imagenFilter (filtro de imagen)

# ImageFilter (filtro de imagen) tiene los siguientes filtros:
# BLUR
# CONTOUR 
# DETAIL 
# EDGE_ENHANCE 
# EDGE_ENHANCE_MORE 
# EMBOSS 
# FIND_EDGES 
# SMOOTH 
# SMOOTH_MORE 
# SHARPE
from PIL import Image, ImageFilter

img = Image.open('c:/Users/USER/Desktop/Python-labs/Laboratorio 07/devices.jpg')
f = img.filter(ImageFilter.EMBOSS)
f.show()