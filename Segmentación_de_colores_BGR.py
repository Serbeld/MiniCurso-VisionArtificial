import cv2
import numpy as np
 
imagenBGR = cv2.imread('opencv_logo.png')
 
#Rango de colores detectados:
#Verdes:
verde_bajos = np.array([0,255,0], dtype=np.uint8)
verde_altos = np.array([0,255,0], dtype=np.uint8)
#Azules:
azul_bajos = np.array([255,0,0], dtype=np.uint8)
azul_altos = np.array([255,0,0], dtype=np.uint8)
#Rojos:
rojo_bajos1 = np.array([0,0,255], dtype=np.uint8)
rojo_altos1 = np.array([0,0,255], dtype=np.uint8)
#Negro:
nbajo = np.array([255,255,255], dtype=np.uint8)
nalto = np.array([255,255,255], dtype=np.uint8)

#Crear las mascaras
mascara_verde = cv2.inRange(imagenBGR, verde_bajos, verde_altos)
mascara_rojo = cv2.inRange(imagenBGR, rojo_bajos1, rojo_altos1)
mascara_azul = cv2.inRange(imagenBGR, azul_bajos, azul_altos)
fondo_negro = cv2.inRange(imagenBGR, nbajo, nalto)

#Juntar todas las mascaras
mask = cv2.add(fondo_negro,mascara_rojo)
mask = cv2.add(mask, mascara_verde)
mask = cv2.add(mask, mascara_azul)
 
#Mostrar la mascara final y la imagen
cv2.imshow('Rojo', mascara_rojo)
cv2.imshow('Verde', mascara_verde)
cv2.imshow('Azul', mascara_azul)
cv2.imshow('Finale', mask)
cv2.imshow('Imagen', imagenBGR)
 
#Salir con la letra "q"
while(True):
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break 
 
cv2.destroyAllWindows()