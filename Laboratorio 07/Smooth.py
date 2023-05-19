from PIL import Image, ImageFilter

img = Image.open('c:/Users/USER/Desktop/Laboratorio 07/devices.jpg')
f = img.filter(ImageFilter.SMOOTH)
f.show()