#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from constants import ID2CITY

def process_weizhan_urls():
    """处理微站数据，添加URL列"""
    try:
        # 读取Excel文件
        input_file = "weizhan_domain_city.xlsx"
        print(f"正在读取文件: {input_file}")
        df = pd.read_excel(input_file)
        
        # 确保必要的列存在
        if 'domain' not in df.columns or 'city' not in df.columns:
            print("错误：Excel文件必须包含 'domain' 和 'city' 列")
            return
            
        # 添加URL列
        print("正在生成URL...")
        def generate_url(row):
            # 从ID2CITY获取实际的城市值
            actual_city = ID2CITY.get(row['city'])
            if actual_city:
                return f"https://{row['domain']}.{actual_city}.baixing.com"
            else:
                print(f"警告: 城市ID {row['city']} 在ID2CITY中未找到对应值")
                return None
                
        df['url'] = df.apply(generate_url, axis=1)
        
        # 保存结果
        output_file = "weizhan_domain_city_with_urls.xlsx"
        df.to_excel(output_file, index=False, engine='openpyxl')
        
        print(f"\n处理完成！")
        print(f"总共处理了 {len(df)} 条数据")
        print(f"成功生成URL的数量: {df['url'].notna().sum()}")
        print(f"结果已保存到: {output_file}")
        
        # 打印一些统计信息
        print("\n城市统计:")
        city_counts = df['city'].value_counts()
        for city, count in city_counts.items():
            actual_city = ID2CITY.get(city, "未知")
            print(f"{city} ({actual_city}): {count}条数据")
            
    except Exception as e:
        print(f"处理数据时出错: {e}")

if __name__ == "__main__":
    process_weizhan_urls() 