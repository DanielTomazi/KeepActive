@echo off
echo ========================================
echo  CRIANDO EXECUTAVEL DO KEEPACTIVE
echo ========================================
echo.

:: Verificar se o PyInstaller está instalado
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo Instalando PyInstaller...
    pip install pyinstaller
    if errorlevel 1 (
        echo ERRO: Falha ao instalar PyInstaller
        pause
        exit /b 1
    )
)

echo PyInstaller encontrado! Criando executavel...
echo.

:: Criar o executável
pyinstaller --onefile --name=KeepActive --distpath=dist --workpath=build --clean KeepActive.py

if errorlevel 1 (
    echo.
    echo ERRO: Falha ao criar executavel
    pause
    exit /b 1
)

echo.
echo ========================================
echo  EXECUTAVEL CRIADO COM SUCESSO!
echo ========================================
echo.
echo Localizacao: %cd%\dist\KeepActive.exe
echo.
echo Como usar:
echo   - Execute KeepActive.exe diretamente
echo   - Ou use: KeepActive.exe [intervalo] [distancia]
echo   - Exemplo: KeepActive.exe 60 50
echo.
pause
