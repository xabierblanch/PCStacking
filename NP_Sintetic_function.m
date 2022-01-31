function num = NP_Sintetic_function(num)

%% Original ABF, modificat per XBG (Script ràpid de test)

%% Inicialització de l'Script
% tic
% beep
% clear all
% clc

%%
%NÚMERO DE MODELS A GENERAR
%num=20;

%% Define puntos de la malla (regluar size, a = pixel size)
a=0.03; 
[x_mesh,y_mesh] = meshgrid(-2:a:2, -2:a:2);
x=reshape (x_mesh,[],1);
y=reshape (y_mesh,[],1);

%% Define la funcion a interpolar y añadir ruido gaussiano
z = 2*exp(-x.^2-y.^6); 
z=abs(z);

path2 = 'Fitxers entrada';
cd(path2);

NP_S= [x,y,z]; dlmwrite('NP_Sintetic.txt',NP_S);

for i=1:num
    z1=z+random('norm', 0, 0.05, length(z),1); 
    x1=x+random('norm', 0, 0.05, length(z),1);
    y1=y+random('norm', 0, 0.05, length(z),1);
    normals1 = pcnormals(pointCloud([x1,y1,z1]),8);
    % Exportar nubes de puntos
    NP_1= [x1,y1,z1,normals1(:,1),normals1(:,2),normals1(:,3)]; dlmwrite(['NP_Random_' num2str(i) '.txt'],NP_1);
end

%% compute volume and plot
% volume=a*a*sum(z)
% 
% plot3(x,y,z,'r.');
% plot3(x1,y1,z1,'r.');
%hold on; plot3(x,y,PC_2(:,3),'b.'); 

end
