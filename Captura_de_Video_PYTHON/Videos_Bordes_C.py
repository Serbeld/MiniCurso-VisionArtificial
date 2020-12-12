# encoding: utf-8 

# Tomar_Video.py
# Este código va orientado a la toma de imágenes de video mediante la librería open cv en Python...

# Programador Sergio Luis Beleño Díaz
# 05.Junio.2019

#Para empezar se importa la librería de Open cv para visión Artificial

import cv2

# Asignamos la cámara ingresando cv2.VideoCapture(0)
# Si quiere asignar una segunda cámara externa puede usar cv2.VideoCapture(1)
cap = cv2.VideoCapture(0)

codec = cv2.VideoWriter_fourcc(*'XVID')
salida = cv2.VideoWriter('videoSalida1.avi', codec, 24,(640,480))

while(True):

	# Toma parámetros de captura de la cámara
	[rec, camara] = cap.read()

	camara = cv2.resize(camara, (640,480), interpolation = cv2.INTER_CUBIC)

	# Convertimos en escala de grise
	gris = cv2.cvtColor(camara, cv2.COLOR_BGR2GRAY)

	# Aplicar suavizado Gaussiano
	gaussiana = cv2.GaussianBlur(gris, (3,3), 1)

	canny = cv2.Canny(gaussiana, 60, 61)  

	# Muestra la imagen tomada en una ventana
	camara[canny <= 0] = 0
	camara[canny > 0] = 255
	salida.write(camara)
	cv2.imshow(' Canny', camara)


	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		
cap.release()
salida.release()
cv2.destroyAllWindows()