# Manipular imagen con Pyllow (PIL)
# Rotar la imagen a 90 grados. 

# Importar el módulo 'Image', luego con la función open()
# abrir la imagen, mediante la ruta asignada y colocar el
# formato de la iamgen
# Al final utilizar la función rotate() para girar la imagen en
# distinta posición.

from PIL import Image

img = Image.open('c:/Users/USER/Desktop/Python-labs/Laboratorio 07/devices.jpg')
imgrotate = img.rotate(90)
imgrotate.show()