@echo off
REM ============================================================
REM Script para compilar e executar experimentos C e Java
REM ============================================================

echo.
echo ============================================================
echo   EXPERIMENTOS - SELECTION SORT (C e Java)
echo ============================================================
echo.
REM ============================================================
REM PARTE 2: JAVA
REM ============================================================
echo.
echo.
echo [2/2] Compilando e executando Java...
echo ------------------------------------------------------------
cd codigo\java

echo Compilando Java...
javac Main.java CarregaCSV.java SelectionSort.java

if %ERRORLEVEL% NEQ 0 (
    echo [ERRO] Falha na compilacao de Java
    cd ..\..
    pause
    exit /b 1
)

echo.
echo Executando experimentos em Java...
echo.
java Main

if %ERRORLEVEL% NEQ 0 (
    echo [ERRO] Falha na execucao de Java
    cd ..\..
    pause
    exit /b 1
)

cd ..\..
REM ============================================================
REM PARTE 1: C
REM ============================================================
echo [1/2] Compilando e executando C...
echo ------------------------------------------------------------
cd codigo\c

echo Compilando com -O3...
gcc -std=c11 -O3 -march=native -Wall -Wextra -o main.exe main.c selection_sort.c -lm

if %ERRORLEVEL% NEQ 0 (
    echo [ERRO] Falha na compilacao de C
    cd ..\..
    pause
    exit /b 1
)

echo.
echo Executando experimentos em C...
echo.
main.exe

if %ERRORLEVEL% NEQ 0 (
    echo [ERRO] Falha na execucao de C
    cd ..\..
    pause
    exit /b 1
)

cd ..\..



REM ============================================================
REM RESUMO
REM ============================================================
echo.
echo.
echo ============================================================
echo   EXPERIMENTOS CONCLUIDOS!
echo ============================================================
echo.
echo Resultados salvos em:
echo   - resultados/estatisticas/resultados_C.csv
echo   - resultados/estatisticas/resultados_Java.csv
echo.

pause
