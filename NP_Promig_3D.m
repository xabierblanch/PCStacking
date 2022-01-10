%% INICIALITZACIÓ DE L'SCRIPT
tic
clc
clear all
%close all

%% CÀRREGA DE DADES I GENERACIÓ DE MATRIUS

path = pwd;
path2 = 'Fitxers entrada';
cd(path2);
fitxers = dir("*NP_Random*");

for i=1:length(fitxers(:,1))
    NP(i).NP = importdata([path,'\',path2,'\',fitxers(i).name]);
end

total=i+1;
NP(total).NP = NP(1).NP;
for i=2:length(fitxers(:,1))
    NP(total).NP = [NP(total).NP; NP(i).NP];
end

for i=1:length(fitxers(:,1))
    Matriu_major(i) = length(NP(i).NP);
end
ref = find(max(Matriu_major));

%% CALCUL VECTORS ROTACIÓ

% PUNT DEL NP
X = NP(ref).NP(:,1);
Y = NP(ref).NP(:,2);
Z = NP(ref).NP(:,3);
PUNT=[X,Y,Z];

NORMAL=[NP(ref).NP(:,4),NP(ref).NP(:,5),NP(ref).NP(:,6)];
A=NORMAL(:,1);
B=NORMAL(:,2);
C=NORMAL(:,3);

% OBTENCIÓ DELS VECTORS QUE CONFORMEN EL PLA PERPEPENDICULAR A LA NORMAL
% VECTOR 1
V2=B.*A./(C-1);
V3=A;
V1=(B.*V2+C.*V3)./-A;
V = [V1,V2,V3];

%VECTOR 2
W1=V2.*C-V3.*B;
W2=V3.*A-V1.*C;
W3=V1.*B-V2.*A;
W = [W1,W2,W3];

%% PARÀMETRES DE CERCA DE PUNTS

Dist_XY = 0.05;
Dist_Z = 0.5;
V_Tall = 0.5; %buscar bé aquest paràmetre

%% LOOP DE CERCA DE PUNTS

parfor i=1:length(PUNT)
    % MATRIU DE ROTACIO
    R =  [V(i,:); W(i,:); NORMAL(i,:)];

    index=find(NP(total).NP(:,1)>(X(i)-V_Tall) & NP(total).NP(:,1)<(X(i)+V_Tall) & NP(total).NP(:,2)>(Y(i)-V_Tall) & NP(total).NP(:,2)<(Y(i)+V_Tall) & NP(total).NP(:,3)>(Z(i)-V_Tall) & NP(total).NP(:,3)<(Z(i)+V_Tall) );
    punts_interes=NP(total).NP(index,1:3);
    punts_interes_R = inv(R)*punts_interes';
    Punt_R = inv(R)*[X(i),Y(i),Z(i)]';

    index=find(punts_interes_R(1,:)>Punt_R(1)-Dist_XY  & punts_interes_R(1,:)<Punt_R(1)+Dist_XY & punts_interes_R(2,:)>Punt_R(2)-Dist_XY & punts_interes_R(2,:)<Punt_R(2)+Dist_XY & punts_interes_R(3,:)>Punt_R(3)-Dist_Z & punts_interes_R(3,:)<Punt_R(3)+Dist_Z);
    punts_inside = punts_interes(index,:);
    
    X_mean=mean(punts_interes(index,1));
    Y_mean=mean(punts_interes(index,2));
    Z_mean=mean(punts_interes(index,3));

    matriu_resultat(i,:)=[X_mean,Y_mean,Z_mean];
end

%% GUARDAT DEL FITXER

cd(path)
dlmwrite(['NP_Promig.txt'],matriu_resultat);

%% FINALITZACIÓ DE L'SCRIPT
toc