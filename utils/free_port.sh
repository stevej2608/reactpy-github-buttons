#!/bin/bash

# Script to free a port by killing the process using it
# Usage: ./free_port.sh [port_number]
# Default port: 8000

PORT=${1:-8000}

echo "Checking for process using port $PORT..."

# Try to find the process using the port
PID=$(ps aux | grep -E "(pytest|python)" | grep -v grep | awk '{print $2}' | head -1)

if [ -z "$PID" ]; then
    # Try alternative method with lsof if available
    if command -v lsof &> /dev/null; then
        PID=$(lsof -ti:$PORT 2>/dev/null)
    fi
fi

if [ -z "$PID" ]; then
    # Try with fuser if available
    if command -v fuser &> /dev/null; then
        PID=$(fuser $PORT/tcp 2>/dev/null | awk '{print $1}')
    fi
fi

if [ -z "$PID" ]; then
    echo "No process found using port $PORT"
    exit 0
fi

echo "Found process(es) using port $PORT: $PID"
echo "Killing process(es)..."

for pid in $PID; do
    kill -9 $pid 2>/dev/null
    if [ $? -eq 0 ]; then
        echo "Successfully killed process $pid"
    else
        echo "Failed to kill process $pid (may require sudo)"
    fi
done

echo "Port $PORT should now be free"
