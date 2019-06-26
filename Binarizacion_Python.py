import cv2

imagen = cv2.imread('opencv_logo.png')
Rango_bajo = 127
Rango_alto = 255

gray = cv2.imread('opencv_logo.png', cv2.IMREAD_GRAYSCALE)
ret,th1 = cv2.threshold(gray,Rango_bajo,Rango_alto,cv2.THRESH_BINARY)

cv2.imshow('Original',imagen)
cv2.imshow('Escala de grises',gray)
cv2.imshow('Binarizada',th1)

cv2.waitKey(0)