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