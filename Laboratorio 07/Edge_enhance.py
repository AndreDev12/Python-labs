from PIL import Image, ImageFilter

img = Image.open('c:/Users/USER/Desktop/Laboratorio 07/devices.jpg')
f = img.filter(ImageFilter.EDGE_ENHANCE)
f.show()