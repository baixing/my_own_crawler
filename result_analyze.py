#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import os
from constants import RESULT_FILE

def analyze_results():
    """分析baidu_results.xlsx文件并生成统计结果"""
    try:
        # 读取源数据文件
        print("正在读取数据文件...")
        df = pd.read_excel(RESULT_FILE, engine='openpyxl')

        if df.empty:
            print("数据文件为空！")
            return

        # 将相关列转换为字符串类型
        df['status_code'] = df['status_code'].astype(str)
        df['expect_code'] = df['expect_code'].astype(str)
        df['is_valid_city'] = df['is_valid_city'].astype(str).str.lower()  # 转换为小写

        # 打印status_code的详细信息
        print("\nstatus_code的详细信息:")
        print("第一行status_code的值:", repr(df['status_code'].iloc[0]))
        print("第一行status_code的类型:", type(df['status_code'].iloc[0]))
        print("status_code的唯一值:")
        print([repr(x) for x in df['status_code'].unique()])
        print("\nstatus_code的值分布:")
        print(df['status_code'].value_counts())

        # 1. 获取第一条数据的时间
        first_time = df['time'].iloc[0]
        # 转换时间格式 (假设格式为 "03-04 14:51:09.221")
        time_parts = first_time.split()
        date = time_parts[0]  # "03-04"
        hour = time_parts[1].split(':')[0]  # "14"
        time_key = f"{date}-{hour}"  # "03-04-14"

        # 构建结果文件名
        date_parts = date.split('-')  # ["03", "04"]
        result_file = f"result_analyze.xlsx"

        # 2. 计算总行数
        total_count = len(df)

        # 3. 统计status_code为200的数量
        # 先清理一下数据，去除可能的空格
        df['status_code'] = df['status_code'].str.strip()
        status_200_mask = (df['status_code'] == '200')
        status_200_count = status_200_mask.sum()  # 改用sum()来计数
        print(f"\nstatus_code为200的行数: {status_200_count}")
        print("status_200_mask的前几个值:", status_200_mask.head())
        print("status_code等于'200'的比较结果:", (df['status_code'] == '200').head())
        if status_200_count == 0:
            print("检查第一个status_code为200的行:")
            print(df[df['status_code'].str.contains('200')].head())

        # 4. 统计status_code为4xx和5xx的数量
        status_45xx_count = len(df[df['status_code'].str.match(r'^[45]')])

        # 5. 统计expect_code不为3xx和4xx的数量
        non_34xx_mask = ~(df['expect_code'].str.match(r'^[34]', na=False) | (df['expect_code'] == '不重要') | (df['category'].isin(['nocategroy','noneed'])) )
        non_34xx_count = len(df[non_34xx_mask])
        
        # 打印所有唯一的request_type值，帮助调试
        print("\nrequest_type的唯一值:")
        print(df['request_type'].unique())

        # 6. 在第5个基础上，筛选is_valid_city为true的数量
        valid_city_mask = (non_34xx_mask) & \
                         (df['is_valid_city'].isin(['1','true'])) & \
                         (~df['request_type'].isin(['get_resource', '不常用接口']))
        valid_city_count = len(df[valid_city_mask])

        # 打印调试信息
        print(f"\n调试信息:")
        print(f"is_valid_city的唯一值: {df['is_valid_city'].unique()}")
        print(f"non_34xx_mask为True的数量: {non_34xx_mask.sum()}")
        print(f"is_valid_city为true的数量: {(df['is_valid_city'] == 'true').sum()}")
        print(f"组合条件为True的数量: {valid_city_mask.sum()}")

        # 7,8,9. 在第6个基础上的统计
        valid_city_df = df[valid_city_mask]
        # 7. 2xx和3xx数量
        status_23xx_count = len(valid_city_df[valid_city_df['status_code'].str.match(r'^[23]')])
        # 8. 2xx数量
        status_2xx_count = len(valid_city_df[valid_city_df['status_code'].str.match(r'^2')])
        # 9. 4xx和5xx数量
        status_45xx_valid_count = len(valid_city_df[valid_city_df['status_code'].str.match(r'^[45]')])

        # # 10. 统计异常数据：adid不为空，expect_code=200但status_code!=200的数量
        # abnormal_mask = (df['adid'].notna() & (df['adid'] != '')) & \
        #                (df['expect_code'] == '200') & \
        #                (df['status_code'] != '200')
        # abnormal_count = len(df[abnormal_mask])

        # 准备新的统计数据
        new_data = {
            'time': [time_key],
            'total_count': [total_count],
            '2xx量': [status_200_count],
            '45xx量': [status_45xx_count],
            # '剔除预期3xx4xx和不重要的请求': [non_34xx_count],
            # '剔除34xx预期和不重要的接口': [valid_city_count],
            # 'valid_city_23xx_count': [status_23xx_count],
            '类目/vad重要2xx量': [status_2xx_count],
            # 'valid_city_45xx_count': [status_45xx_valid_count],
            # 'abnormal_count': [abnormal_count]
        }
        new_df = pd.DataFrame(new_data)

        # 读取或创建结果文件
        if os.path.exists(result_file):
            result_df = pd.read_excel(result_file, engine='openpyxl')
            # 检查是否已存在相同时间的记录
            # 添加新记录
            result_df = pd.concat([result_df, new_df], ignore_index=True)
        else:
            # 创建新的DataFrame
            result_df = new_df
        
        # 保存结果
        result_df.to_excel(result_file, index=False, engine='openpyxl')
        print(f"分析完成！结果已保存到 {result_file}")
        
        # 打印当前统计结果
        print("\n当前统计结果：")
        for key, value in new_data.items():
            print(f"{key}: {value[0]}")
            
    except Exception as e:
        print(f"处理过程中出错: {e}")
        import traceback
        print(traceback.format_exc())

if __name__ == "__main__":
    analyze_results()