@echo off
REM Turkish Bot Setup Script for Windows

echo.
echo ========================================
echo  Turkish Bot - Python Setup
echo ========================================
echo.

REM Clone the repository
echo [1/5] Clonando repositorio...
git clone https://github.com/miguellimarodriguez19-afk/Turkish-bott-py.git
cd Turkish-bott-py

REM Create virtual environment
echo.
echo [2/5] Criando ambiente virtual...
python -m venv venv

REM Activate virtual environment
echo.
echo [3/5] Ativando ambiente virtual...
call venv\Scripts\activate.bat

REM Install dependencies
echo.
echo [4/5] Instalando dependencias...
pip install -r requirements.txt

REM Create .env file
echo.
echo [5/5] Criando arquivo .env...
copy .env.example .env
echo.
echo ========================================
echo  Setup Completo! 
echo ========================================
echo.
echo Proximos passos:
echo 1. Abra o arquivo .env
echo 2. Coloque seu DISCORD_TOKEN
echo 3. Execute: python main.py
echo.
echo Ambiente virtual ja esta ativado!
echo.
pause
