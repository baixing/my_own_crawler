#!/bin/bash
if [ -f "monitor.pid" ]; then
    PID=$(cat monitor.pid)
    if ps -p $PID > /dev/null; then
        echo "停止应用 (PID: $PID)..."
        kill $PID
        rm monitor.pid
        echo "应用已停止"
    else
        echo "应用未运行"
        rm monitor.pid
    fi
else
    echo "PID文件不存在，应用可能未运行"
fi
