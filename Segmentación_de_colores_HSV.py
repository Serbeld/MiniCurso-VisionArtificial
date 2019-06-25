import cv2
import numpy as np
 
imagen = cv2.imread('opencv_logo.png')
hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
 
#Rango de colores detectados:
#Verdes:
verde_bajos = np.array([49,50,50], dtype=np.uint8)
verde_altos = np.array([107, 255, 255], dtype=np.uint8)
#Azules:
azul_bajos = np.array([100,65,75], dtype=np.uint8)
azul_altos = np.array([130, 255, 255], dtype=np.uint8)
#Rojos:
rojo_bajos1 = np.array([0,65,75], dtype=np.uint8)
rojo_altos1 = np.array([12, 255, 255], dtype=np.uint8)
#Negro:
nbajo = np.array([255,255,255], dtype=np.uint8)
nalto = np.array([255,255,255], dtype=np.uint8)

#Crear las mascaras
mascara_verde = cv2.inRange(hsv, verde_bajos, verde_altos)
mascara_rojo1 = cv2.inRange(hsv, rojo_bajos1, rojo_altos1)
mascara_azul = cv2.inRange(hsv, azul_bajos, azul_altos)
fondo_negro = cv2.inRange(hsv, nbajo, nalto)

#Juntar todas las mascaras
mask = cv2.add(fondo_negro,mascara_rojo1)
mask = cv2.add(mask, mascara_verde)
mask = cv2.add(mask, mascara_azul)
 
#Mostrar la mascara final y la imagen
cv2.imshow('Rojo', mascara_rojo1)
cv2.imshow('Verde', mascara_verde)
cv2.imshow('Azul', mascara_azul)
cv2.imshow('Finale', mask)
cv2.imshow('Imagen', imagen)
 
#Salir con la letra "q"
while(True):
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break 
 
cv2.destroyAllWindows()