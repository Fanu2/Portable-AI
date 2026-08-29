#!/usr/bin/env bash

set -e

SCRIPT_DIR="$(
    cd "$(dirname "$0")"
    pwd
)"

PROJECT_ROOT="$(
    cd "$SCRIPT_DIR/../.."
    pwd
)"

PYTHON="${PYTHON:-python3}"

echo "=== Portable-AI Linux Setup ==="
echo
echo "Project root:"
echo "  $PROJECT_ROOT"
echo

if ! command -v "$PYTHON" >/dev/null 2>&1; then
    echo "Python was not found."
    echo
    echo "Install Python 3.13 or newer and try again."
    exit 1
fi

PYTHON_VERSION="$(
    "$PYTHON" -c \
    'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")'
)"

PYTHON_MAJOR="$(
    "$PYTHON" -c \
    'import sys; print(sys.version_info.major)'
)"

PYTHON_MINOR="$(
    "$PYTHON" -c \
    'import sys; print(sys.version_info.minor)'
)"

if [ "$PYTHON_MAJOR" -lt 3 ] || \
   { [ "$PYTHON_MAJOR" -eq 3 ] && \
     [ "$PYTHON_MINOR" -lt 13 ]; }; then

    echo "Python 3.13 or newer is required."
    echo "Found: Python $PYTHON_VERSION"
    exit 1
fi

echo "Python:"
"$PYTHON" --version
echo

cd "$PROJECT_ROOT"

if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    "$PYTHON" -m venv .venv
else
    echo "Using existing virtual environment."
fi

VENV_PYTHON="$PROJECT_ROOT/.venv/bin/python"

echo
echo "Installing Portable-AI..."

"$VENV_PYTHON" -m pip install --upgrade pip
"$VENV_PYTHON" -m pip install -e .

echo
echo "Portable-AI setup complete."
