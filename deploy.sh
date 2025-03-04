#!/bin/bash

# 获取当前目录的绝对路径
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# 创建必要的目录
mkdir -p "$SCRIPT_DIR/logs"
mkdir -p "$SCRIPT_DIR/data"

# 确保脚本有执行权限
chmod +x "$SCRIPT_DIR/run_crawler.py"

# 检查是否已经存在crontab项
CRON_CMD="5 * * * * cd $SCRIPT_DIR && /usr/bin/python3 $SCRIPT_DIR/run_crawler.py >> $SCRIPT_DIR/logs/cron.log 2>&1"
(crontab -l 2>/dev/null | grep -Fv "$SCRIPT_DIR/run_crawler.py"; echo "$CRON_CMD") | crontab -

# 创建requirements.txt（如果不存在）
if [ ! -f "$SCRIPT_DIR/requirements.txt" ]; then
    cat > "$SCRIPT_DIR/requirements.txt" << EOL
pandas
requests
openpyxl
EOL
fi

# 检查是否安装了pip3
if ! command -v pip3 &> /dev/null; then
    echo "正在安装pip3..."
    sudo apt-get update
    sudo apt-get install -y python3-pip
fi

# 安装Python依赖
echo "正在安装Python依赖..."
pip3 install -r "$SCRIPT_DIR/requirements.txt"

echo "部署完成！"
echo "已设置定时任务，每小时执行一次爬虫程序"
echo "日志文件将保存在: $SCRIPT_DIR/logs/"
echo "可以通过以下命令查看定时任务："
echo "crontab -l" 