clc; clear all;              % Limpialas variables almacenadas y el command windows
I = imread('camino.jpg');    % Carga la imagen
ibn=im2bw(I,0.44);           % Binarizaci�n
figure (1)
imshow(I)                    % Muestra la imagen RGB
figure(2)
imshow(ibn)                  % Muestra la imagen binarizada
imtool(ibn)                  % Muestra las caracter�sticas de la imagen binarizada