#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import requests
import time
import os
import shutil
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from constants import RESULT_FILE

def check_ad_exist(ad_id):
    """检查广告是否存在"""
    url = f"https://api.baixing.com.cn/v2/ad/{ad_id}"
    try:
        response = requests.get(url)
        data = response.json()
        return ad_id, 'yes' if data.get('code') == 200 else 'no'
    except Exception as e:
        print(f"检查广告 {ad_id} 时出错: {e}")
        return ad_id, 'pending'

def process_pending_ads(batch_size=50, max_workers=10):
    """批量处理待检查的广告"""
    date = time.strftime("%m-%d %H:%M:%S", time.localtime())
    date_parts = date.split('-')  # ["03", "04"]
    hour = date.split(':')[0]

    try:
        # 读取Excel文件
        print("正在读取数据文件...")
        df = pd.read_excel(RESULT_FILE, engine='openpyxl')
        
        # 获取需要处理的行
        pending_mask = (df['ad_isexist'] == 'pending') & (df['adid'].notna()) & (df['adid'] != '')
        pending_rows = df[pending_mask]
        
        if pending_rows.empty:
            print("没有需要处理的pending广告")
            return
        
        total = len(pending_rows)
        print(f"找到 {total} 条需要处理的记录")
        
        # 创建广告ID到索引的映射
        id_to_idx = {row['adid']: idx for idx, row in pending_rows.iterrows()}
        
        # 分批处理
        ad_ids = list(id_to_idx.keys())
        results = {}
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            for i in range(0, len(ad_ids), batch_size):
                batch = ad_ids[i:i + batch_size]
                futures = {executor.submit(check_ad_exist, ad_id): ad_id for ad_id in batch}
                
                # 使用tqdm显示进度
                with tqdm(total=len(batch), desc=f"处理批次 {i//batch_size + 1}") as pbar:
                    for future in as_completed(futures):
                        ad_id, result = future.result()
                        results[ad_id] = result
                        pbar.update(1)
                
                # 更新这一批次的结果到DataFrame
                for ad_id, result in results.items():
                    idx = id_to_idx[ad_id]
                    if result == 'yes':
                        df.at[idx, 'expect_code'] = '200'
                    print(ad_id,result)
                    df.at[idx, 'ad_isexist'] = result

                # 保存更新
                print(f"保存批次 {i//batch_size + 1} 的处理结果...")
                safe_save_excel(df, RESULT_FILE)

                # 清空当前批次的结果
                results.clear()
                
                # 短暂延时，避免下一批次请求过于频繁
                time.sleep(1)
        
        print("所有pending广告处理完成！")
        
    except Exception as e:
        print(f"处理过程中出错: {e}")
        import traceback
        print(traceback.format_exc())

def safe_save_excel(df, file_path):
    """安全地保存Excel文件"""
    # 确保临时文件和备份文件使用正确的扩展名
    temp_path = file_path.replace('.xlsx', '_temp.xlsx')
    backup_path = file_path.replace('.xlsx', '_backup.xlsx')
    
    try:
        # 先保存到临时文件
        df.to_excel(temp_path, index=False, engine='openpyxl')
        
        # 如果原文件存在，创建备份
        if os.path.exists(file_path):
            shutil.copy2(file_path, backup_path)
        
        # 将临时文件改名为目标文件
        shutil.move(temp_path, file_path)
        
        # 删除备份文件
        if os.path.exists(backup_path):
            os.remove(backup_path)
            
        return True
    except Exception as e:
        print(f"保存文件失败: {e}")
        # 如果保存失败，尝试恢复备份
        if os.path.exists(backup_path):
            shutil.copy2(backup_path, file_path)
            print("已恢复备份文件")
        # 清理临时文件
        if os.path.exists(temp_path):
            os.remove(temp_path)
        return False

if __name__ == "__main__":
    process_pending_ads() 