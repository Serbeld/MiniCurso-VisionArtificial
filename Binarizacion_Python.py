import cv2

imagen = cv2.imread('opencv_logo.png')
Rango_de_binarizacion = 40
PixelON = 255

gray = cv2.imread('opencv_logo.png', cv2.IMREAD_GRAYSCALE)
ret,binarizada = cv2.threshold(gray,Rango_de_binarizacion,PixelON,cv2.THRESH_BINARY)
print((ret))

cv2.imshow('Original',imagen)
cv2.imshow('Escala de grises',gray)
cv2.imshow('Binarizada',binarizada)

cv2.waitKey(0)
