@echo off
chcp 65001 >nul
color 0A
title Sistema de Diagnóstico de PC

echo ================================================
echo    SISTEMA DE DIAGNÓSTICO DE PC - BATCH
echo ================================================
echo.

echo [INFO] Coletando informações do sistema...
echo.

echo --- INFORMAÇÕES DO SISTEMA ---
systeminfo | findstr /C:"Nome do host" /C:"Nome do sistema" /C:"Tipo de sistema" /C:"Processador"
echo.

echo --- MEMÓRIA RAM ---
systeminfo | findstr /C:"Memória Física Total" /C:"Memória Física Disponível"
echo.

echo --- DISCOS ---
wmic logicaldisk get caption,description,freespace,size,volumename
echo.

echo --- PROCESSOS COM MAIOR USO DE MEMÓRIA ---
tasklist /FO TABLE | findstr /V "Image"
echo.

echo --- TEMPERATURA E SAÚDE ---
wmic /namespace:\\root\wmi PATH MSAcpi_ThermalZoneTemperature get CurrentTemperature 2>nul
if errorlevel 1 (
    echo [AVISO] Não foi possível obter temperatura do sistema
)
echo.

echo ================================================
echo Diagnóstico concluído!
echo ================================================
echo.
echo Pressione qualquer tecla para sair...
pause >nul
