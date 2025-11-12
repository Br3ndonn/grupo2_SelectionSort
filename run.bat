@echo off
chcp 65001 > nul
echo =========================================
echo COMPILAÇÃO E EXECUÇÃO - PROJETO EADII
echo =========================================

:: ==============================
:: COMPILA JAVA
:: ==============================
echo Compilando o projeto Java...
javac -d codigo\java\out codigo\java\src\*.java

if %errorlevel% neq 0 (
    echo Erro na compilação Java!
    pause
    exit /b %errorlevel%
)

echo Compilação Java concluída com sucesso!
echo -----------------------------------------

echo ▶Executando o programa Java...
call java -cp codigo\java\out Main

echo -----------------------------------------

:: ==============================
:: COMPILA C
:: ==============================
echo 🔹 Compilando o projeto C...

if not exist codigo\c\build mkdir codigo\c\build

gcc codigo\c\src\main.c ^
    codigo\c\src\selection_sort.c ^
    codigo\c\src\lista.c ^
    codigo\c\src\carrega_csv.c ^
    -I codigo\c\include ^
    -O3 -march=native -ffast-math -funroll-loops ^
    -o codigo\c\build\meu_programa.exe

if %errorlevel% neq 0 (
    echo erro na compilação C!
    pause
    exit /b %errorlevel%
)

echo Compilação C concluída com sucesso!
echo -----------------------------------------

echo ▶Executando o programa C...
call codigo\c\build\meu_programa.exe

echo -----------------------------------------

:: ==============================
:: EXECUTA PYTHON
:: ==============================
echo Executando o programa Python...
call python codigo\python\main.py

echo =========================================
echo EXECUÇÃO COMPLETA!
echo =========================================
pause
