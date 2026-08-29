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

VENV_PYTHON="$PROJECT_ROOT/.venv/bin/python"

if [ ! -x "$VENV_PYTHON" ]; then
    echo "Portable-AI environment not found."
    echo
    echo "Expected:"
    echo "  $VENV_PYTHON"
    exit 1
fi

cd "$PROJECT_ROOT"

exec "$VENV_PYTHON" \
    -m portable_ai.gui.app
