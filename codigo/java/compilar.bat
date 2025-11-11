@echo off
REM Script de compilação para Selection Sort em Java
REM Versão otimizada

echo ================================================
echo   Compilando Selection Sort (Java)
echo ================================================

REM Limpa arquivos compilados antigos
echo.
echo [1/2] Limpando arquivos .class antigos...
del /Q *.class 2>nul

REM Compila todos os arquivos Java
echo [2/2] Compilando arquivos Java...
javac Main.java CarregaCSV.java SelectionSort.java

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ================================================
    echo   Compilacao concluida com sucesso!
    echo ================================================
    echo.
    echo Para executar: java Main
    echo.
) else (
    echo.
    echo ERRO: Falha na compilacao!
    exit /b 1
)
