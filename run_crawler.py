#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import logging
from datetime import datetime
import subprocess
import time
import glob

# 设置日志
def setup_logging():
    """设置日志配置"""
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    timestamp = datetime.now().strftime("%Y%m%d")
    log_file = os.path.join(log_dir, f"crawler_{timestamp}.log")
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(sys.stdout)
        ]
    )

def find_latest_excel():
    """查找最新生成的Excel文件"""
    # 查找当前目录下所有的*_result.xlsx文件
    excel_files = glob.glob("*_result.xlsx")
    if not excel_files:
        return None
    
    # 按文件修改时间排序，返回最新的
    return max(excel_files, key=os.path.getmtime)

def update_constants_file(excel_file):
    """更新constants.py中的RESULT_FILE值"""
    with open('constants.py', 'r') as f:
        lines = f.readlines()
    
    with open('constants.py', 'w') as f:
        for line in lines:
            if line.startswith('RESULT_FILE'):
                f.write(f"RESULT_FILE = '{excel_file}'\n")
            else:
                f.write(line)

def run_script(script_name):
    """运行指定的Python脚本"""
    try:
        logging.info(f"开始执行 {script_name}")
        result = subprocess.run(
            [sys.executable, script_name],
            check=True,
            capture_output=True,
            text=True
        )
        logging.info(f"{script_name} 执行成功")
        if result.stdout:
            logging.info(f"输出: {result.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"{script_name} 执行失败: {str(e)}")
        logging.error(f"错误输出: {e.stderr}")
        return False

def main():
    """主函数，协调整个爬虫流程"""
    setup_logging()
    start_time = time.time()
    
    try:
        # 1. 运行nginx日志处理脚本
        logging.info("开始处理nginx日志...")
        if not run_script('ngix_log.py'):
            raise Exception("nginx日志处理失败")

        # 等待文件生成并列出当前目录文件
        time.sleep(5)
        logging.info("当前目录文件列表:")
        for file in os.listdir('.'):
            if file.endswith('.xlsx'):
                logging.info(f"- {file} (修改时间: {datetime.fromtimestamp(os.path.getmtime(file))})")
        
        # 查找最新生成的Excel文件
        excel_file = find_latest_excel()
        if not excel_file:
            raise Exception("未找到生成的Excel文件")
        
        logging.info(f"找到最新的Excel文件: {excel_file}")
        
        # 2. 更新constants.py中的RESULT_FILE
        logging.info(f"更新RESULT_FILE为: {excel_file}")
        update_constants_file(excel_file)
        
        # 3. 依次执行其他脚本
        scripts = [
            # 'process_ad_exist.py',
            # 'process_ad_exist_in_b.py',
            'result_analyze.py'
        ]
        
        for script in scripts:
            if not run_script(script):
                raise Exception(f"{script} 执行失败")
            time.sleep(2)  # 等待每个脚本执行完成
        
        execution_time = time.time() - start_time
        logging.info(f"所有任务执行完成，总耗时: {execution_time:.2f} 秒")
        
    except Exception as e:
        logging.error(f"执行过程中出错: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 