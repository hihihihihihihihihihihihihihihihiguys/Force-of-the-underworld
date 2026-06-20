cd "C:\Users\walke\OneDrive\Desktop\Force of the underworld"

@echo off
setlocal

:: ===== CONFIG =====
set PROJECT_NAME=my_project
set PYTHON_CMD=python

echo ==============================
echo Smart Python venv setup
echo ==============================

:: ===== CHECK PYTHON =====
%PYTHON_CMD% --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python not found. Installing via winget...
    winget install Python.Python.3.12

    echo Waiting for install to complete...
    timeout /t 5 >nul

    :: try again
    %PYTHON_CMD% --version >nul 2>&1
    if %errorlevel% neq 0 (
        echo Python install failed or PATH not updated.
        echo Restart terminal and run again.
        exit /b
    )
) else (
    echo Python already installed. Skipping install.
)

:: ===== CREATE VENV =====
if not exist "venv\" (
    echo Creating virtual environment...
    %PYTHON_CMD% -m venv venv
) else (
    echo venv already exists. Skipping creation.
)

:: ===== ACTIVATE VENV =====
call venv\Scripts\activate.bat

:: ===== UPGRADE PIP =====
echo Upgrading pip...
python -m pip install --upgrade pip

:: ===== OPTIONAL PACKAGES =====
echo Installing base packages...
pip install wheel setuptools

echo ==============================
echo Setup complete!
echo venv is active.
echo ==============================

python -m src.game