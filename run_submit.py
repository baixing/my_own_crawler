#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import logging
from datetime import datetime
import subprocess
import time

def setup_logging():
    """设置日志配置"""
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    timestamp = datetime.now().strftime("%Y%m%d")
    log_file = os.path.join(log_dir, f"submit_task_new.log")
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(sys.stdout)
        ]
    )
    return log_file

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
        if e.stdout:
            logging.error(f"标准输出: {e.stdout}")
        if e.stderr:
            logging.error(f"错误输出: {e.stderr}")
        return False

def main():
    """主函数，协调整个提交流程"""
    log_file = setup_logging()
    start_time = time.time()
    
    try:
        logging.info("=== 开始执行URL提交任务 ===")
        
        # 1. 执行爬虫脚本
        logging.info("步骤1: 执行分类广告爬虫...")
        if not run_script('spider_category_newest_ads.py'):
            raise Exception("分类广告爬虫执行失败")
        
        # 等待Excel文件生成
        time.sleep(5)
        
        # 2. 执行URL提交脚本
        logging.info("步骤2: 执行URL提交...")
        if not run_script('batch_submit_urls.py'):
            raise Exception("URL提交脚本执行失败")
        
        execution_time = time.time() - start_time
        logging.info(f"=== 所有任务执行完成 ===")
        logging.info(f"总耗时: {execution_time:.2f} 秒")
        logging.info(f"日志文件保存在: {log_file}")
        
    except Exception as e:
        logging.error(f"执行过程中出错: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 