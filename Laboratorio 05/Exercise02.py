import cv2

def nothing(x):
    pass

img = cv2.imread('developers.jpg')
img = cv2.resize(img, (600, 300))

cv2.namedWindow('Canny')

cv2.createTrackbar('Lower', 'Canny', 0, 255, nothing)
cv2.createTrackbar('Upper', 'Canny', 0, 255, nothing)

switch = '0 : OFF \n  1 : ON'
cv2.createTrackbar(switch, 'Canny', 0, 1, nothing)

while True:
    lower = cv2.getTrackbarPos('Lower', 'Canny')
    upper = cv2.getTrackbarPos('Upper', 'Canny')
    s = cv2.getTrackbarPos(switch, 'Canny')

    if s == 0:
        edge = img
    else:
        edge = cv2.Canny(img, lower, upper)

    cv2.imshow('Image', img)
    cv2.imshow('Canny', edge)
    k=cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows


# # Importación de las librerías en Python
# from PIL import Image
# from cv2 import Canny
# import math

# import numpy as np

# # Selección de la imagen
# img = Image.open('developers.jpg').convert('L')
# # print(type(img))

# image_data=np.asarray(img)
# # print(type(image_data))

# ancho, alto = img.size

# #Implementación de las máscaras de Canny
# cannyX = [[-1.0,0.0,1.0], [-2.0,0.0,2.0],[-1.0,0.0,1.0]]

# cannyY = [[1.0,2.0,1.0], [0.0,0.0,0.0], [-1.0,-2.0,-1.0]]

# #Implementación de la matriz gaussiana
# gaussiano5 = [[2.0/115.0,4.0/115.0,5.0/115.0,4.0/115.0,2.0/115.0],
#               [4.0/115.0,9.0/115.0,12.0/115.0,9.0/115.0,4.0/115.0],
#               [5.0/115.0,12.0/115.0,15.0/115.0,12.0/115.0,5.0/115.0],
#               [4.0/115.0,9.0/115.0,12.0/115.0,9.0/115.0,4.0/115.0],
#               [2.0/115.0,4.0/115.0,5.0/115.0,4.0/115.0,2.0/115.0]
#               ]

# print(type(gaussiano5))
# result=np.asarray(gaussiano5)

# #Implementación de la función para filtrar imagen(5x5)
# def filtrar5x5(img,mascara):
#     arr=img.load()
#     for x in range(2,img.size[0]-2,1):
#         for y in range(2,img.size[1]-2,1):
#             valor=0
#             for i in range(-2,3):
#                 for j in range(-2,3):
#                     valor=valor + int(mascara[i][j]*img.getpixel((x+i,y+i)))
#             arr[x-1,y-1]=valor
#     return arr

# #Detalles finales
# I=Canny(img,cannyX,cannyY,gaussiano5)
# img.show()
# img.save('canny.tif') 