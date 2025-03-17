#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import pandas as pd
import time
from datetime import datetime, timedelta
from constants import ALL_CITIES


def get_ads_from_city(city):
    """获取指定城市的广告数据"""
    url = f"https://api.baixing.com.cn/v2/ad?city={city}&size=1000&page=1"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }

    payload = {}

    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        return response.json()
    except Exception as e:
        print(f"请求城市 {city} 时出错: {e}")
        return None


def process_city_data():
    """处理所有城市的数据"""
    # 创建一个空的DataFrame来存储结果
    result_df = pd.DataFrame(columns=['city', 'url', 'id', 'category', 'created'])

    # 获取24小时前的时间戳
    one_day_ago = int((datetime.now() - timedelta(days=1)).timestamp())

    # 当前时间作为文件名
    current_time = datetime.now().strftime("%Y%m%d")
    excel_file = f"category_ads_{current_time}.xlsx"

    print(f"开始处理城市数据，结果将保存到: {excel_file}")

    # 遍历所有城市
    for city in ALL_CITIES:
        print(f"\n正在处理城市: {city}")
        n = 0

        # 获取城市数据
        response_data = get_ads_from_city(city)
        if not response_data or 'data' not in response_data or 'items' not in response_data['data']:
            print(f"城市 {city} 数据获取失败或格式不正确，跳过")
            continue

        # 处理该城市的数据
        city_data = []
        for item in response_data['data']['items']:
            # 检查必要字段是否存在
            if not all(k in item for k in ['id', 'category', 'created']):
                continue

            # 检查创建时间是否在24小时内
            if int(item['created']) < one_day_ago:
                continue
            elif n >= 20:
                continue
            n = n+1

            # 构建URL
            url = f"{city}.baixing.com/{item['category']}/a{item['id']}.html"

            # 添加数据
            city_data.append({
                'city': city,
                'url': url,
                'id': item['id'],
                'category': item['category'],
                'created': item['created']
            })

        if city_data:
            # 将城市数据添加到总DataFrame
            city_df = pd.DataFrame(city_data)
            result_df = pd.concat([result_df, city_df], ignore_index=True)

            # 每处理完一个城市就保存一次
            result_df.to_excel(excel_file, index=False, engine='openpyxl')
            print(f"城市 {city} 处理完成，找到 {len(city_data)} 条24小时内的数据")
        else:
            print(f"城市 {city} 没有找到24小时内的数据")

        # 添加延时，避免请求过于频繁
        time.sleep(2)

    print(f"\n所有城市处理完成！")
    print(f"总共找到 {len(result_df)} 条数据")
    print(f"结果已保存到: {excel_file}")


if __name__ == "__main__":
    process_city_data()
