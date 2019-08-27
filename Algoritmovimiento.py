# Importación de librerías
import numpy as np
import cv2
import time
from os import remove

# Capturamos el vídeo
cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorKNN(history=20, dist2Threshold=5000, detectShadows=False)

cv2.ocl.setUseOpenCL(False)


fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('video.avi',fourcc, 20.0, (640,480))

cont = 0
time2 = 0

while(1):

	ret, frame = cap.read()

	# Aplicamos el algoritmo
	fgmask = fgbg.apply(frame)
	Moments = cv2.moments(fgmask)

	while (Moments["m00"] >= 100000):
		ret, frame = cap.read()

		# Aplicamos el algoritmo
		fgmask = fgbg.apply(frame)
		Moments = cv2.moments(fgmask)
		#print(Moments["m00"])
		
		# Define el codec y crea el objeto VideoWrite
		out.write(frame)

		cv2.imshow('Camara',frame)
		cv2.imshow('Umbral',fgmask)

		k = cv2.waitKey(10) & 0xff

		if k == ord("s"):
			cont = 1 + cont
			cap.release()
			out.release()
			break
		
	cv2.destroyAllWindows()


cap.release()
out.release()
cv2.destroyAllWindows()