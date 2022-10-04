#!/bin/sh

# Entrypoint script for docker
echo "Starting entrypoint.sh..."

if [ -z "$TESTBED" ]
then
    echo "Starting production..."
    cd /src/ && uvicorn serve:app --workers 4 --port 7000 --host 0.0.0.0
else
    echo "Testbed mode"
    cd /src/ && uvicorn serve:app --reload --port 7000 --host 0.0.0.0
fi
