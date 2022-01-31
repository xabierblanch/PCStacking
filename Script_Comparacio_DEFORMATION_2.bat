@echo off
SETLOCAL ENABLEDELAYEDEXPANSION
for /l %%x in (2, 1, 10) do (
set A=00%%x
set A=!A:~-3!
"C:\Program Files\CloudCompare\CloudCompare" -SILENT -AUTO_SAVE OFF -C_EXPORT_FMT ASC -o  "X:\3_PROCESSAT\1_REFINAT\4_NP_Sintetic\NP_Sintetic.txt" -o "X:\3_PROCESSAT\1_REFINAT\4_NP_Sintetic\NP_Promig_%%x_NP.txt" -M3C2 "X:\3_PROCESSAT\1_REFINAT\4_NP_Sintetic\Comparacions M3C2 Inicials\m3c2_params.txt" -SAVE_CLOUDS FILE "'X:\3_PROCESSAT\1_REFINAT\4_NP_Sintetic\NP_Sintetic.txt' 'X:\3_PROCESSAT\1_REFINAT\4_NP_Sintetic\NP_Promig_%%x_NP.txt' 'X:\3_PROCESSAT\1_REFINAT\4_NP_Sintetic\Comparacions M3C2 Inicials\M3C2_NP_Promig_!A!_NP_to_NP_Sintetic.txt'"
)   
ENDLOCAL

