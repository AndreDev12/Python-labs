# Ingresar texto dentro de la imagen

# Importar módulos Imagen, ImageDraw (dibujo de imagen), ImgeFont (fuente de imagen)
# Abrir imagen y empezar a escribir sobre ella.
# Se especifica el tipo de fuente. (Para el caso, arial tamaño (50 pixeles))
# Posteriormente en la función 'text' se le pasa sus argumentos
# (Las posiciones X y Y, en el texto que se desea escribir sobre la imagen,
# color de texto y fuente
# Al final se muestra la imagen con el texto.

from PIL import Image, ImageDraw, ImageFont

img = Image.open('c:/Users/USER/Desktop/Python-labs/Laboratorio 07/devices.jpg')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('arial.ttf', 50)
draw.text((20, 20), 'Programando en Python',
          fill='white', font=font)
img.show()