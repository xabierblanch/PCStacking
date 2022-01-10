% Escript que va calculant iterativament "i" NP i calcula la mitja
% respecte aquests NP.

% i = 2 -> Es generen 2 NP autom�ticament i es calcula la mitja d'aquests 2
% NP

% i = 3 -> Es generen 3 NP autom�ticament i es calcula la mitja d'aquests 3
% NP


%% INICIALITZACI� DE L'SCRIPT
tic
clc
clear all

path=pwd;

for i=2:10
NP_Sintetic_function(i);
cd(path);
NP_Promig_3D_function(i)
end

%% COMPARACIONS AUTOM�TIQUES AMB M3C2 (CLOUDCOMPARE)
%S'ha de posar el mateix valor m�xim que al for
system('X:\3_PROCESSAT\1_REFINAT\4_NP_Sintetic\Comparacions M3C2 Inicials\Script_Comparacio_DEFORMATION_2.bat');
%% OBTENCI� DE LA DESVIACI� STANDAR RESULTAT DEL M3C2
path = pwd;
path2 = 'Comparacions M3C2 Inicials';
cd(path2);
fitxers = dir("*M3C2_NP_Promig*");

for i=1:length(fitxers(:,1))
    NP(i).NP = importdata([path,'\',path2,'\',fitxers(i).name]);
    S(i,1) = std(NP(i).NP(:,7),'omitnan');
    S(i,2) = i;
end

f=fit(S(:,2),S(:,1),'poly2'); hold on;
plot(f,S(:,2),S(:,1))