@echo off
setlocal

set SCRIPT_DIR=%~dp0

for %%I in ("%SCRIPT_DIR%\..\..") do (
    set PROJECT_ROOT=%%~fI
)

echo === Portable-AI Windows Setup ===
echo.
echo Project root:
echo   %PROJECT_ROOT%
echo.

where python >nul 2>nul

if errorlevel 1 (
    echo Python was not found.
    echo.
    echo Install Python 3.13 or newer and try again.
    exit /b 1
)

for /f %%I in (
    'python -c "import sys; print(sys.version_info.major * 100 + sys.version_info.minor)"'
) do set PYTHON_VERSION=%%I

if %PYTHON_VERSION% LSS 313 (
    echo Python 3.13 or newer is required.
    echo.
    python --version
    exit /b 1
)

echo Python:
python --version
echo.

cd /d "%PROJECT_ROOT%"

if not exist ".venv\Scripts\python.exe" (
    echo Creating virtual environment...
    python -m venv .venv
) else (
    echo Using existing virtual environment.
)

set VENV_PYTHON=%PROJECT_ROOT%\.venv\Scripts\python.exe

echo.
echo Installing Portable-AI...

"%VENV_PYTHON%" -m pip install --upgrade pip
"%VENV_PYTHON%" -m pip install -e .

echo.
echo Portable-AI setup complete.

endlocal
