@echo off
REM Script de teste para verificar formatação de decimais no CSV

echo ================================================
echo   Teste de Formatacao CSV - Java
echo ================================================

REM Compila o código
echo.
echo [1/3] Compilando...
call compilar.bat
if %ERRORLEVEL% NEQ 0 exit /b 1

REM Cria um teste simples com um único tamanho
echo.
echo [2/3] Executando teste com n=10000...
java Main 10000

REM Verifica o arquivo gerado
echo.
echo [3/3] Verificando formato do CSV gerado...
echo.
echo Conteudo do arquivo resultados_Java.csv:
echo ==========================================
type ..\..\resultados\estatisticas\resultados_Java.csv
echo ==========================================
echo.

REM Verifica se há vírgulas nos números (problema)
findstr /C:"," ..\..\resultados\estatisticas\resultados_Java.csv > temp_check.txt
set /p PRIMEIRA_LINHA=<temp_check.txt
del temp_check.txt

REM Análise simples
echo Analise:
echo - Se os numeros tiverem PONTO (.): Correto! 
echo - Se os numeros tiverem VIRGULA (,): Problema!
echo.

echo Teste concluido!
