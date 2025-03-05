#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名: baixing_seo_processor.py
# 功能: 下载SEO日志，提取包含baidu的行，并转换为Excel格式

import os
import requests
import tarfile
import subprocess
import pandas as pd
import json
import re
from datetime import datetime
from constants import OLD_CATEGORIES, LEVEL1_CATEGORIES, CATEGORY_TO_LEVEL1, NO_IMPORTANT_PATH,FOUR_XX_PATH


def contains_any(lst, elements):
    return bool(set(lst) & set(elements))


def download_file(url, save_path):
    """从指定URL下载文件"""
    print(f"正在从 {url} 下载文件...")
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        total_size = int(response.headers.get("content-length", 0))
        block_size = 8192
        downloaded = 0

        with open(save_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=block_size):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    # 显示下载进度
                    done = int(50 * downloaded / total_size)
                    print(
                        f"\r下载进度: [{'=' * done}{' ' * (50 - done)}] {downloaded}/{total_size} 字节",
                        end="",
                    )

        print("\n下载完成!")
        return True
    except Exception as e:
        print(f"下载失败: {e}")
        return False


def extract_tarfile(tar_path, extract_dir):
    """解压缩tar.gz文件"""
    print(f"正在解压缩 {tar_path} 到 {extract_dir}...")
    try:
        if not os.path.exists(extract_dir):
            os.makedirs(extract_dir)

        with tarfile.open(tar_path, "r:gz") as tar:
            tar.extractall(path=extract_dir)

        print("解压缩完成!")
        return True
    except Exception as e:
        print(f"解压缩失败: {e}")
        return False


def grep_baidu(directory, output_file):
    """使用grep查找包含baidu的行"""
    print(f"正在查找包含'baidu'的行...")
    try:
        # 使用grep递归搜索目录中所有文件
        cmd = f"grep -r 'baidu' {directory} > {output_file}"
        subprocess.run(cmd, shell=True, check=True)

        # 检查结果文件大小
        file_size = os.path.getsize(output_file)
        print(f"查找完成! 找到的结果已保存到 {output_file} (大小: {file_size} 字节)")
        return True
    except Exception as e:
        print(f"查找失败: {e}")
        return False


def get_valid_cities():
    """获取所有有效城市的英文名列表"""
    try:
        url = "https://api.baixing.com.cn/v2/city"
        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        data = response.json()

        # 提取所有城市的英文名
        valid_cities = []
        for province in data.get('data', []):
            for city in province.get('cities', []):
                if 'englishname' in city:
                    valid_cities.append(city['englishname'].lower())

        return valid_cities
    except Exception as e:
        print(f"获取城市列表失败: {e}")
        return []


def convert_to_excel(text_file, excel_file):
    """将文本文件转换为Excel格式，提取时间、状态码、城市、请求地址和请求路径"""
    print(f"正在将 {text_file} 转换为Excel格式...")
    try:
        # 获取有效城市列表
        valid_cities = get_valid_cities()
        print(f"获取到 {len(valid_cities)} 个有效城市")

        # 读取文本文件
        with open(text_file, "r", encoding="utf-8", errors="replace") as f:
            lines = f.readlines()

        # 处理数据
        data = []
        for line in lines:
            try:
                # 分割行内容，首先去除文件路径部分
                log_content = line.split(':', 1)[1].strip()

                # 提取时间
                # 格式示例: Mar  3 14:51:09
                time_parts = log_content.split()[:3]
                month = time_parts[0]
                day = time_parts[1]
                time = time_parts[2]
                # 将月份名转换为数字
                month_map = {
                    'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04',
                    'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08',
                    'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'
                }
                month_num = month_map[month]
                # 格式化日期（补零）
                day = day.zfill(2)

                # 使用空格分割，但保留引号内的内容
                parts = []
                current_part = ''
                in_quotes = False
                for char in log_content:
                    if char == '"':
                        in_quotes = not in_quotes
                        current_part += char
                    elif char.isspace() and not in_quotes:
                        if current_part:
                            parts.append(current_part)
                            current_part = ''
                    else:
                        current_part += char
                if current_part:
                    parts.append(current_part)

                # 提取状态码和毫秒
                # 找到包含tengine[的部分之后的内容
                log_parts = log_content.split('tengine[')[1].split(':', 1)[1].strip().split()
                # 第一个是时间戳，提取毫秒部分
                timestamp = log_parts[0]
                milliseconds = timestamp.split('.')[1][:3] if '.' in timestamp else '000'
                # 第二个数字是状态码
                status_code = log_parts[1]

                # 合并时间和毫秒
                formatted_time = f"{month_num}-{day} {time}.{milliseconds}"

                # 提取请求地址和城市
                host = None
                city = None
                for part in parts:
                    if '.baixing.com' in part:
                        host = part.strip('"')
                        # 修改城市提取逻辑，获取最靠近baixing.com的域名部分
                        domains = host.split('.')
                        for i, domain in enumerate(domains):
                            if domain == 'baixing':
                                city = domains[i - 1] if i > 0 else ''
                                break
                        break

                # 提取请求路径
                request_path = None
                for part in parts:
                    if part.startswith('"GET ') or part.startswith('"POST '):
                        request_path = part.split()[1]
                        break

                # 检查城市是否在有效列表中
                is_valid_city = 'true' if city and city.lower() in valid_cities else 'false'
                # 判断请求类型
                request_type = 'None'  # 默认类型
                original_path = request_path
                expect_code = 'Non expect'
                category = '不重要'
                belong_to_level1 = 'None'

                # request_path
                # 检查category,expect_code,belong_to_level1

                domains = host.split('.')
                baixing_index = domains.index('baixing') if 'baixing' in domains else -1
                if baixing_index > 1:  # 如果baixing前面超过1段domain
                    expect_code = '404'
                elif re.search(r'/m\d+/', request_path) or re.search(r'/m\d+-m\d+/', request_path)  or contains_any(request_path, FOUR_XX_PATH):
                    expect_code = '404'
                elif host == 'mpapi.baixing.com':
                    expect_code = '404'


                else:
                # 移除开头的/和结尾的/
                    if '?' in original_path:
                        request_path = original_path.split('?')[0]

                    if request_path in ['/', '/m/', '/m']:
                        request_type = 'main'
                        category = 'all'
                        expect_code = '404'
                    elif '/m/' in request_path:
                        expect_code = '301'
                    else:
                        clean_path = request_path.strip('/')
                        if clean_path:
                            # print(clean_path)
                            parts = clean_path.split('/')

                            if parts[0] == 'm' and len(parts) > 1:
                                category = parts[1]  # 取/m/后的第一个部分
                            else:
                                category = parts[0]  # 取第一个部分
                            if category and '_' in category:
                                expect_code = '404'

                        if contains_any(request_path, NO_IMPORTANT_PATH) or category == 'arch':
                            request_type = 'NotImportant'
                        elif category in ['resumes', 'resume']:
                            request_type = 'resume'
                        # 检查是否是一级类目
                        elif category in LEVEL1_CATEGORIES:
                            request_type = 'old_Level1_category'
                            belong_to_level1 = category
                        # 检查是否是旧类目
                        elif category in OLD_CATEGORIES:
                            request_type = 'old_categroy'
                            belong_to_level1 = CATEGORY_TO_LEVEL1.get(category, 'None')
                        else:
                            category = '不合法类目'
                        if request_type in ['old_categroy', 'old_Level1_category', 'main']:
                            request_type = 'ImportantInfo'
                        if (expect_code == 'Non expect' and
                            request_type not in ('NotImportant') and
                            status_code == '404' and
                            '.html' in request_path) and is_valid_city == 'true':
                            # 提取帖子ID
                            match = re.search(r'/[^/]+/(?:a)?(\d+)\.html', request_path)
                            if match:
                                expect_code = '404'
                print(expect_code)
                data.append(
                        [formatted_time, status_code, city, is_valid_city, host, original_path,request_path, request_type, category,belong_to_level1,expect_code])

            except Exception as e:
                print(f"处理行时出错: {e}")
                continue

        # 创建DataFrame
        df = pd.DataFrame(data, columns=['time', 'status_code', 'city', 'is_valid_city', 'host', 'original_path','request_path',
                                         'request_type', 'category', 'belong_to_level1',
                                         'expect_code'])

        # 保存为Excel
        df.to_excel(excel_file, index=False, engine="openpyxl")

        # 获取第一行的时间并格式化文件名
        first_time = df['time'].iloc[0]  # 格式如 "03-04 14:51:09.221"
        time_parts = first_time.split()
        date = time_parts[0]  # "03-04"
        hour = time_parts[1].split(':')[0]  # "14"
        date_parts = date.split('-')  # ["03", "04"]
        current_dir_excel = f"{date_parts[0]}_{date_parts[1]}_{hour}_result.xlsx"

        # 复制一份Excel文件到当前目录
        df.to_excel(current_dir_excel, index=False, engine="openpyxl")

        print(f"转换完成! Excel文件已保存为 {excel_file}")
        print(f"同时在当前目录保存了一份副本: {current_dir_excel}")
        return True
    except Exception as e:
        print(f"转换失败: {e}")
        return False


def main():
    """主函数"""
    # 创建时间戳文件夹
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    work_dir = f"baixing_seo_{timestamp}"
    if not os.path.exists(work_dir):
        os.makedirs(work_dir)

    # 设置文件路径
    url = "http://examine.baixing.com/logs/baixing_seo.tar.gz"
    tar_file = os.path.join(work_dir, "baixing_seo.tar.gz")
    extract_dir = os.path.join(work_dir, "extracted")
    baidu_log = os.path.join(work_dir, "baidu_results.txt")
    excel_file = os.path.join(work_dir, "baidu_results.xlsx")

    # 执行任务
    if download_file(url, tar_file):
        if extract_tarfile(tar_file, extract_dir):
            if grep_baidu(extract_dir, baidu_log):
                convert_to_excel(baidu_log, excel_file)

    print(f"\n所有任务完成! 结果保存在目录: {work_dir}")
    print(f"Excel文件路径: {excel_file}")


if __name__ == "__main__":
    main()
