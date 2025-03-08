#!/bin/bash

# 定义颜色
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 定义变量
APP_NAME="baixing_monitor"
PORT=8081
VENV_PATH="venv"
PID_FILE="monitor.pid"
LOG_FILE="monitor.log"

echo -e "${GREEN}开始部署 ${APP_NAME}...${NC}"

# 检查 Python 版本
echo -e "${YELLOW}检查 Python 环境...${NC}"
python3 --version || {
    echo -e "${RED}未找到 Python3${NC}"
    exit 1
}

# 检查必要的包是否安装
echo -e "${YELLOW}检查必要的包...${NC}"
pip3 --version || {
    echo -e "${RED}未找到 pip3${NC}"
    exit 1
}

# 检查虚拟环境
if [ ! -d "$VENV_PATH" ]; then
    echo -e "${YELLOW}创建虚拟环境...${NC}"
    python3 -m venv $VENV_PATH || {
        echo -e "${RED}创建虚拟环境失败${NC}"
        exit 1
    }
fi

# 激活虚拟环境
echo -e "${YELLOW}激活虚拟环境...${NC}"
source $VENV_PATH/bin/activate || {
    echo -e "${RED}激活虚拟环境失败${NC}"
    exit 1
}

# 检查 requirements.txt 是否存在
if [ ! -f "requirements.txt" ]; then
    echo -e "${YELLOW}创建 requirements.txt...${NC}"
    echo "flask==2.0.1
requests==2.26.0
python-dotenv==0.19.0" > requirements.txt
fi

# 安装依赖
echo -e "${YELLOW}安装依赖...${NC}"
pip install -r requirements.txt || {
    echo -e "${RED}安装依赖失败${NC}"
    exit 1
}

# 检查必要的文件是否存在
echo -e "${YELLOW}检查必要文件...${NC}"
for file in "app.py" "baidu_tongji_api.py"; do
    if [ ! -f "$file" ]; then
        echo -e "${RED}错误: 找不到 $file${NC}"
        exit 1
    fi
done

# 检查是否有旧进程在运行
if [ -f "$PID_FILE" ]; then
    OLD_PID=$(cat $PID_FILE)
    if ps -p $OLD_PID > /dev/null; then
        echo -e "${YELLOW}停止旧进程 (PID: $OLD_PID)...${NC}"
        kill $OLD_PID
        sleep 2
    fi
    rm $PID_FILE
fi

# 清理旧的日志文件
if [ -f "$LOG_FILE" ]; then
    echo -e "${YELLOW}备份旧日志文件...${NC}"
    mv $LOG_FILE "${LOG_FILE}.$(date +%Y%m%d_%H%M%S).bak"
fi

# 启动应用
echo -e "${YELLOW}启动应用...${NC}"
nohup python app.py --port $PORT > $LOG_FILE 2>&1 & echo $! > $PID_FILE

# 等待应用启动
echo -e "${YELLOW}等待应用启动...${NC}"
sleep 5

# 检查应用是否成功启动
if ps -p $(cat $PID_FILE) > /dev/null; then
    # 检查端口是否在监听
    if lsof -i :$PORT > /dev/null 2>&1; then
        echo -e "${GREEN}应用已成功启动 (PID: $(cat $PID_FILE))${NC}"
        echo "日志文件: $LOG_FILE"
        echo "访问地址: http://localhost:$PORT"
        
        # 显示最近的日志
        echo -e "${YELLOW}最近的日志输出:${NC}"
        tail -n 10 $LOG_FILE
    else
        echo -e "${RED}应用启动失败: 端口 $PORT 未被监听${NC}"
        echo -e "${YELLOW}查看日志内容:${NC}"
        cat $LOG_FILE
        exit 1
    fi
else
    echo -e "${RED}应用启动失败，进程未运行${NC}"
    echo -e "${YELLOW}查看日志内容:${NC}"
    cat $LOG_FILE
    exit 1
fi

# 创建停止脚本
cat > stop_monitor.sh << EOL
#!/bin/bash
if [ -f "$PID_FILE" ]; then
    PID=\$(cat $PID_FILE)
    if ps -p \$PID > /dev/null; then
        echo "停止应用 (PID: \$PID)..."
        kill \$PID
        rm $PID_FILE
        echo "应用已停止"
    else
        echo "应用未运行"
        rm $PID_FILE
    fi
else
    echo "PID文件不存在，应用可能未运行"
fi
EOL

chmod +x stop_monitor.sh

echo -e "${GREEN}部署完成！${NC}"
echo "使用 ./stop_monitor.sh 可以停止应用" 