# encoding: utf-8 

# Tomar_Video.py

# Este código va orientado a la toma de imágenes de video mediante 
# la librería open cv en Python...

# Programador Sergio Luis Beleño Díaz
# 05.Junio.2019

'''
Para empezar se importan las librerías de Open cv para visión 
Artificial y se utiliza la librería numpy para la optimización 
de datos al trabajar con las matrices que componen a la imagen 
obtenida pixel por pixel
'''

import cv2

# Asignamos la camara ingresando cv2.VideoCapture(0)
# Si quiere asignar una segunda camara externa puede usar cv2.VideoCapture(1)
cap = cv2.VideoCapture(0)

while(True):

	# Toma parametros de captura de la camara
	[rec, camara] = cap.read()

	# Muestra la imagen tomada en una ventana
	cv2.imshow('Nombre de la ventana de video', camara)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
