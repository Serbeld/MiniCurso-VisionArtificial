%Segmentación de colores RGB
clc;clear all;
RGB = imread('segmenta.jpg');           %carga la imagen
R = RGB;, R(:,:,[2,3]) = 0;             % Imagen con G y B nulas
G = RGB;, G(:,:,[1,3]) = 0;             % Imagen con R y B nulas
B = RGB;, B(:,:,[1,2]) = 0;             % Imagen con R y G nulas
f1 = figure(1);, set(f1, 'color', 'w');, clf; % Crea Figura
subplot(1,4,1);                         % Selecciona el 1 subplot
imshow(RGB); title('Imagen Color');     % Visualiza imagen color
subplot(1,4,2);                         % Selecciona el 2 subplot
imshow(R); title('Componente Rojo');    % Visualiza componente R
subplot(1,4,3);                         % Selecciona el 3 subplot
imshow(G); title('Componente Verde');   % Visualiza componente G
subplot(1,4,4);                         % Selecciona el 4 subplot
imshow(B); title('Componente Azul');    % visualiza componente B

%% Binarización
i = imread('segmenta.jpg');             % Carga la imagen RGB
R=i(:,:,1);                             % Toma la componente en rojo de la matriz RGB
bw=im2bw(R,0.8);                        % binarización de la componente en rojo
figure (2)
imshow(i);                              % muestra la imagen RGB
figure(3)
imshow(R);                              % muestra la imagen de la componente roja
figure (4)
imshow(bw)                              % muestra la imagen binarizada
