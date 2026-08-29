@echo off
setlocal

set SCRIPT_DIR=%~dp0
for %%I in ("%SCRIPT_DIR%\..\..") do set PROJECT_ROOT=%%~fI

set VENV_PYTHON=%PROJECT_ROOT%\.venv\Scripts\python.exe

if not exist "%VENV_PYTHON%" (
    echo Portable-AI environment not found.
    echo.
    echo Expected:
    echo   %VENV_PYTHON%
    exit /b 1
)

cd /d "%PROJECT_ROOT%"

"%VENV_PYTHON%" -m portable_ai.gui.app

endlocal
