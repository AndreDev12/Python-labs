# Reconocimiento de imágenes en cortado y minimizado
import cv2;
import numpy as np

img = cv2.imread('/Desktop/Sistemas inteligentes/Laboratorio 04/ProDjango.jpg', 0) # Leemos la imagen
h,w,canal=img.shape # Ancho y altura de la forma de la imagen

#Interpolación
img_mitad=cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

#Cortar una parte de la imagen:
img_piece = img[0:int(h/2), 0:int(w/2)] #Cortar la imagen 01

img_piece2 = img[int(h/2):h, int(w/2):w] #Cortar la imagen 02

cv2.imshow('imagen principal', img)
cv2.imshow('imagen minimizado', img_mitad)

cv2.waitKey(3000) #Esperar la tecla en 0 segundos
cv2.destroyAllWindows() #Eliminar las ventanas
