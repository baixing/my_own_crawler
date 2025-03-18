#!/bin/bash

# 获取当前目录的绝对路径
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# 创建必要的目录
mkdir -p "$SCRIPT_DIR/logs"
mkdir -p "$SCRIPT_DIR/data"

# 确保脚本有执行权限
chmod +x "$SCRIPT_DIR/run_crawler.py"
chmod +x "$SCRIPT_DIR/run_submit.py"

# 检查是否已经存在crontab项
CRAWLER_CRON="5 */2 * * * cd $SCRIPT_DIR && /usr/bin/python3 $SCRIPT_DIR/run_crawler.py >> $SCRIPT_DIR/logs/cron.log 2>&1"
SUBMIT_CRON="20 */2 * * * cd $SCRIPT_DIR && /usr/bin/python3 $SCRIPT_DIR/run_submit.py >> $SCRIPT_DIR/logs/cron_submit.log 2>&1"

# 更新crontab
(crontab -l 2>/dev/null | grep -Fv "$SCRIPT_DIR/run_crawler.py" | grep -Fv "$SCRIPT_DIR/run_submit.py"; echo "$CRAWLER_CRON"; echo "$SUBMIT_CRON") | crontab -

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
echo "已设置定时任务："
echo "1. 爬虫程序：每2小时执行一次"
echo "2. URL提交程序：每天0点和12点执行"
echo "日志文件将保存在: $SCRIPT_DIR/logs/"
echo "爬虫日志: cron.log"
echo "URL提交日志: cron_submit.log"
echo "可以通过以下命令查看定时任务："
echo "crontab -l" 