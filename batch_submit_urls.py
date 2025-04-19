#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import requests
import time
from datetime import datetime
import os
import logging
from constants import ALL_CITIES

def setup_logger(log_file):
    """
    设置日志记录器
    
    Args:
        log_file (str): 日志文件路径
    """
    # 创建日志记录器
    logger = logging.getLogger('baidu_submit')
    logger.setLevel(logging.INFO)
    
    # 创建文件处理器
    fh = logging.FileHandler(log_file, encoding='utf-8')
    fh.setLevel(logging.INFO)
    
    # 创建控制台处理器
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    
    # 创建格式化器
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    
    # 添加处理器到日志记录器
    logger.addHandler(fh)
    logger.addHandler(ch)
    
    return logger

def submit_urls_to_baidu(urls, city, logger):
    """
    提交URL列表到百度
    
    Args:
        urls (list): URL列表
        city (str): 城市名
        logger: 日志记录器
    
    Returns:
        dict: 包含提交结果的字典
    """
    api_url = f'http://data.zz.baidu.com/urls?site=https://{city}.baixing.com&token=8cpODGN0LWdMtXij'

    # 将URL列表用换行符连接成字符串
    post_data = '\n'.join(urls)

    # 设置请求头
    headers = {
        'Content-Type': 'text/plain'
    }

    try:
        # 发送POST请求
        logger.info(f"正在提交 {city} 的 {len(urls)} 条URL")
        response = requests.post(api_url, data=post_data, headers=headers)
        response.raise_for_status()
        return {
            'status': 'success',
            'result': response.json(),
            'city': city,
            'url_count': len(urls)
        }
    except Exception as e:
        logger.error(f"提交 {city} 的URL时出错: {str(e)}")
        return {
            'status': 'error',
            'error': str(e),
            'city': city,
            'url_count': len(urls)
        }

def process_city_urls(df, city, batch_size=100, logger=None):
    """
    处理单个城市的URL
    
    Args:
        df (DataFrame): 包含URL的DataFrame
        city (str): 城市名
        batch_size (int): 每批处理的URL数量
        logger: 日志记录器
        
    Returns:
        dict: 包含处理结果的统计信息
    """
    # 获取该城市的所有URL
    city_df = df[df['city'] == city]
    if city_df.empty:
        logger.info(f"城市 {city} 没有需要处理的URL")
        return {
            'processed_urls': 0,
            'success_urls': 0,
            'failed_urls': 0,
            'has_data': False
        }

    urls = city_df['url'].tolist()
    # 确保URL以https://开头
    urls = [f"https://{url}" if not url.startswith('http') else url for url in urls]

    # 分批处理URL
    total_urls = len(urls)
    processed = 0
    success_urls = 0
    failed_urls = 0

    logger.info(f"\n处理城市 {city} 的URL，共 {total_urls} 条")

    try:
        for i in range(0, total_urls, batch_size):
            batch_urls = urls[i:i + batch_size]
            logger.info(f"处理第 {i//batch_size + 1} 批，{len(batch_urls)} 条URL")
            result = submit_urls_to_baidu(batch_urls, city, logger)
            logger.debug(f"API响应: {result}")
            
            if result['status'] == 'error':
                logger.error(f"✗ 提交失败: {result['error']}")
                logger.warning(f"跳过城市 {city} 的剩余URL")
                failed_urls += len(urls[i:])  # 将剩余的URL都计入失败数
                return {
                    'processed_urls': processed,
                    'success_urls': success_urls,
                    'failed_urls': failed_urls,
                    'has_data': True,
                    'error': f"API错误: {result['error']}"
                }
            
            if result['status'] == 'success':
                if result['result']['remain'] == 0:
                    logger.warning(f"配额已用完，剩余：{result['result']['remain']}")
                    logger.warning(f"跳过城市 {city} 的剩余URL")
                    success_urls += len(batch_urls)  # 当前批次的URL计入成功
                    failed_urls += len(urls[i + batch_size:])  # 剩余的URL计入失败
                    return {
                        'processed_urls': processed + len(batch_urls),
                        'success_urls': success_urls,
                        'failed_urls': failed_urls,
                        'has_data': True,
                        'error': "配额用完"
                    }
                
                logger.info(f"✓ 成功提交 {result['url_count']} 条URL")
                logger.info(f"响应结果: {result['result']}")
                success_urls += len(batch_urls)
                processed += len(batch_urls)
                logger.info(f"进度: {processed}/{total_urls}")
            
            # 添加延时，避免请求过于频繁
            time.sleep(2)
        
        return {
            'processed_urls': processed,
            'success_urls': success_urls,
            'failed_urls': failed_urls,
            'has_data': True
        }
        
    except Exception as e:
        logger.error(f"处理城市 {city} 时发生错误: {str(e)}")
        failed_urls += len(urls) - processed  # 将未处理的URL计入失败数
        return {
            'processed_urls': processed,
            'success_urls': success_urls,
            'failed_urls': failed_urls,
            'has_data': True,
            'error': f"处理异常: {str(e)}"
        }

def main():
    """主函数"""
    # 获取当前日期和时间
    current_date = datetime.now().strftime('%Y%m%d')
    current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # 设置文件路径
    excel_file = f"category_ads_new.xlsx"
    log_file = f"baidu_submit_{current_time}.log"
    
    # 设置日志记录器
    logger = setup_logger(log_file)
    logger.info("开始处理URL提交任务")

    if not os.path.exists(excel_file):
        logger.error(f"错误: 找不到文件 {excel_file}")
        return

    try:
        # 读取Excel文件
        logger.info(f"正在读取文件: {excel_file}")
        df = pd.read_excel(excel_file)

        # 检查必要的列是否存在
        required_columns = ['city', 'url']
        if not all(col in df.columns for col in required_columns):
            raise ValueError(f"Excel文件必须包含以下列: {', '.join(required_columns)}")

        # 统计信息
        total_cities = len(ALL_CITIES)
        processed_cities = 0
        cities_with_data = 0
        total_processed_urls = 0
        total_success_urls = 0
        total_failed_urls = 0

        # 处理每个城市的URL
        for city in ALL_CITIES:
            result = process_city_urls(df, city, logger=logger)
            processed_cities += 1
            if result['has_data']:
                cities_with_data += 1
                total_processed_urls += result['processed_urls']
                total_success_urls += result['success_urls']
                total_failed_urls += result['failed_urls']

        # 打印最终统计信息
        logger.info("\n========== 处理完成统计 ==========")
        logger.info(f"总城市数量: {total_cities}")
        logger.info(f"处理的城市数量: {processed_cities}")
        logger.info(f"有数据的城市数量: {cities_with_data}")
        logger.info(f"处理的URL总数: {total_processed_urls}")
        logger.info(f"成功提交的URL数: {total_success_urls}")
        logger.info(f"失败的URL数: {total_failed_urls}")
        logger.info("================================")
        logger.info(f"日志文件已保存到: {log_file}")

    except Exception as e:
        logger.error(f"处理过程中出错: {e}")

if __name__ == "__main__":
    main()
