%% Ejercicio_tipo_Parcial

close all; clear; clc;
RGB = imread('E1.jpg');
RGB = imresize(RGB,0.6); % 50%
B = RGB(:,:,3); % componentes en Azul

% Binarización

imagen = im2bw(B,0.1); % Binariza la imagen en su componente  
imagen = not(imagen); % Invierte los pixeles de la imagen

% Proms
RGB = double(RGB);

R = RGB(:,:,1);
G = RGB(:,:,2);
B = RGB(:,:,3);

RP = ((12+0+6+58+0)/5);
GP = ((44+63+80+176+62)/5);
BP = ((59+107+153+214+121)/5);

RD = R-RP;
GD = G-GP;
BD = B-BP;

% INDEX
D = (RD.^2+GD.^2+BD.^2).^(1/2);

%% BIN Azul

D(D > 70) = -1;
D(D > -1) = 255;
D(D == -1) = 0;   

% Filtro closing
se = strel('cube',10);
D = imclose(D, se);

figure(1)

%% Areas

% Elimina Pixeles

% NEGRO
[elementosennegro, num] = bwlabel(imagen);
cajanegra = regionprops(elementosennegro,'basic');

Aoff = find([cajanegra.Area]<1000); 
 for n = 1:size(Aoff,2)
     d = round(cajanegra(Aoff(n)).BoundingBox);
     imagen(d(2):d(2)+d(4),d(1):d(1)+d(3)) = 0;
 end

% AZUL
 [elementosenazul, num] = bwlabel(D);
recuadro = regionprops(elementosenazul,'basic');

Aoff = find([recuadro.Area]<1000); 

for n = 1:size(Aoff,2)
     d = round(recuadro(Aoff(n)).BoundingBox);
     D(d(2):d(2)+d(4),d(1):d(1)+d(3)) = 0;
 end
 
%% Dilata
 imagen = imdilate(imagen,se);
 D = imdilate(D,se);
 
%% Elementos de la imagen 

[elementosennegro, num] = bwlabel(imagen);
cajanegra = regionprops(elementosennegro,'basic'); 

 [elementosenazul, num] = bwlabel(D);
recuadro = regionprops(elementosenazul,'basic');

% Muestra la imagen 
imshow(uint8(RGB)); 

%% Bounding Boxes

hold on

%%
for k = 1:length(cajanegra)
    
    caja = cajanegra(k).BoundingBox; % Carcasa negro
    recuadro1 = recuadro(k).BoundingBox;  % Carcasa azul
    
    area = cajanegra(k).Area 
    areaazul = recuadro(k).Area
    
    if areaazul > 3000 
        rectangle('position',[recuadro1(1),recuadro1(2),recuadro1(3),recuadro1(4)],'edgecolor','b','LineWidth',4)
        text(recuadro1(1)+recuadro1(3)/2,recuadro1(2)+recuadro1(4)/2,'Azul','Color','b','FontSize',14,'HorizontalAlignment','center','FontWeight','bold')
    end
    
    if area > 3000 
        rectangle('position',[caja(1),caja(2),caja(3),caja(4)],'edgecolor','w','LineWidth',4)
        text(caja(1)+caja(3)/2,caja(2)+caja(4)/2,'Negra','Color','w','FontSize',14,'HorizontalAlignment','center','FontWeight','bold')

    end
    
end
    
hold off
