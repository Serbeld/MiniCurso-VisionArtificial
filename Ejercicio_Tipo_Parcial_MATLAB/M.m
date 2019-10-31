%% detectar areas de color 

close all; clear; clc;

RGB = imread('1.jpeg');

RGB = imresize(RGB,0.4); % Re-escala la imagen en un 40% para consumir menos recursos computacionales

% R = RGB(:,:,1); % Para componentes en Rojo
G = RGB(:,:,2); % Para componentes en Verde
% B = RGB(:,:,3); % Para componentes en Azul

imshow(G) % Muestra su componente en verde

%% Binarización

imagen = im2bw(G,0.3); % Binariza la imagen en su componente en un 30%
imagen = not(imagen); % Invierte los pixeles de la imagen

figure(1)
imshow(imagen); % Muestra la imagen binarizada

%% Areas

%% Cuenta la cantidad de elementos y elimina los elementos que tengan un area menor a 1000 px

[L, num] = bwlabel(imagen);
% Substrae las propiedades basicas de los elementos de la imagen
ncajas = regionprops(L,'basic');

Aoff = find([ncajas.Area]<1000); % Encuentra los objetos de pixeles que estan por debajo de 1000px

% Elimina los objetos por debajo de 1000px como el ruido de la imagen
 for n = 1:size(Aoff,2)
     d = round(ncajas(Aoff(n)).BoundingBox);
     imagen(d(2):d(2)+d(4),d(1):d(1)+d(3)) = 0;
 end

%% cuenta los elementos en la imagen que quedaron 

[L, num] = bwlabel(imagen);
% Substrae las propiedades basicas de los elementos de la imagen
ncajas = regionprops(L,'basic'); 

% Grafica texto y recuadro

hold on

for k = 1:length(ncajas)
    
    caja = ncajas(k).BoundingBox; % Recuadro
    
    % Imprime el area de cada elemento de la imagen en el Command Window
    area = ncajas(k).Area 
    
    % Basura con un area menor a 10000px
    if area < 10000
        rectangle('position',[caja(1),caja(2),caja(3),caja(4)],'edgecolor','b','LineWidth',4)
        text(caja(1)+caja(3)/2,caja(2)+caja(4)/2,'Basura','Color','b','FontSize',12,'HorizontalAlignment','center','FontWeight','bold')
    
    % Bolso con un area mayor a 10000px y menor a 21000px
    elseif area > 10000 && area < 21000
        rectangle('position',[caja(1),caja(2),caja(3),caja(4)],'edgecolor','b','LineWidth',4)
        text(caja(1)+caja(3)/2,caja(2)+caja(4)/2,'Bolso','Color','b','FontSize',12,'HorizontalAlignment','center','FontWeight','bold')

    % Manto con un area mayor a 21000
    elseif area > 21000
        rectangle('position',[caja(1),caja(2),caja(3),caja(4)],'edgecolor','b','LineWidth',4)
        text(caja(1)+caja(3)/2,caja(2)+caja(4)/2,'Manta','Color','b','FontSize',12,'HorizontalAlignment','center','FontWeight','bold')
        
    end
    
end
    
