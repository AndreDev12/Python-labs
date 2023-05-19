# Manipular imagen con Pyllow (PIL)
# Rotar la imagen a 45 grados. 

# Importar el módulo 'Image', luego con la función open()
# abrir la imagen, mediante la ruta asignada y colocar el
# formato de la iamgen
# Al final utilizar la función rotate() para girar la imagen en
# distinta posición.

from PIL import Image

img = Image.open('c:/Users/USER/Desktop/Laboratorio 07/devices.jpg')
imgrotate = img.rotate(45)
imgrotate.show()