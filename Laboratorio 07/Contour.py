from PIL import Image, ImageFilter

img = Image.open('c:/Users/USER/Desktop/Python-labs/Laboratorio 07/devices.jpg')
f = img.filter(ImageFilter.CONTOUR)
f.show()