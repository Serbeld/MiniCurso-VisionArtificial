# encoding: utf-8

# Tomar_vide_termo.py
# Este código va orientado a la toma de imágenes de video mediante la librería open cv en Python...

# Programador Sergio Luis Beleño Díaz
# 23.Enero.2020

# Para empezar se importa la librería de Open cv para visión Artificial

import cv2
import os

# Asignamos la cámara ingresando cv2.VideoCapture(0)
# Si quiere asignar una segunda cámara externa puede usar cv2.VideoCapture(1)
cap = cv2.VideoCapture(0)

while (True):

    # Toma parámetros de captura de la cámara
    [rec, camara] = cap.read()
    #camara = cv2.cvtColor(camara,cv2.COLOR_BGR2BGRA)
    #camara = cv2.cvtColor(camara,cv2.COLOR_BGR2GRAY)
    #camara = cv2.cvtColor(camara,cv2.COLOR_BGR2HLS)
    #camara = cv2.cvtColor(camara,cv2.COLOR_BGR2HLS_FULL)
    #camara = cv2.cvtColor(camara,cv2.COLOR_BGR2HSV)
    #camara = cv2.cvtColor(camara,cv2.COLOR_HSV2BGR)

    camara = cv2.cvtColor(camara,cv2.COLOR_BGR2HSV_FULL)
    
    #print((camara[:,:,2][:,:]))

    for i in range(0,480):
        for j in range(0,640):
            if(camara[:,:,0][i,j]  >= 40 and camara[:,:,2][i,j] >= 80):              #Blue and Red equal Magent
                camara[:,:,0][i,j] = int(camara[:,:,0][i,j]/20) #Blue
                camara[:,:,2][i,j] = 180

    #camara[:,:,0] =  camara[:,:,0]/255
    #camara = cv2.cvtColor(camara,cv2.COLOR_BGR2LAB)
    #camara = cv2.cvtColor(camara,cv2.COLOR_BGR2LUV)

    # Muestra la imagen tomada en una ventana
    cv2.imshow('Nombre de la ventana de video', camara)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        # Crea la imagen
        cv2.imwrite('Imagen_termo.png',camara)
        break

cap.release()
cv2.destroyAllWindows()