clc; clear all;              % Limpialas variables almacenadas y el command windows
I = imread('camino.jpg');    % Carga la imagen
ibn=im2bw(I,0.44);           % Binarización
figure (1)
imshow(I)                    % Muestra la imagen RGB
figure(2)
imshow(ibn)                  % Muestra la imagen binarizada
imtool(ibn)                  % Muestra las características de la imagen binarizada

% NOTA: Las imágenes deben estar en la misma carpeta que el programa que se ejecuta,
% además el número 0.46 es el porcentaje de binarización(se recomienda variarlo para observar que sucede).
