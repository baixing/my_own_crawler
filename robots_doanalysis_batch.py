#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import time
import json
import pandas as pd
from datetime import datetime
import os
from constants import CITIES

# 城市列表

# 请求头
headers = {
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Connection': 'keep-alive',
    'Referer': 'https://ziyuan.baidu.com/robots/index?site=https://www.baixing.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'x-request-by': 'baidu.ajax',
    'x-requested-with': 'XMLHttpRequest',
    'Cookie': 'XFI=da60be90-f9a8-11ef-a410-6b9e62a76a75; XFCS=716FEEFF2C45594E00794CE3730A01E0AF75196CD560023C0AA4D16ED18D55E7; XFT=pJsm7K85UOACOLOCAtZ/a8fIbCSXri4lpvDkujmGscE=; PSTM=1728975980; BIDUPSID=93DA28675B56D16E886B3580C6E2258E; MAWEBCUID=web_kdLVFyFhFoMwyUuwBUQxDeCKjdpzIACSIpGYQTmmoeujjWVyKE; H_WISE_SIDS_BFESS=61781_61787_61802_61867; MCITY=-131%3A; BAIDUID=9BD1631F2A64AD6A4C0EF448323A7F36:SL=0:NR=10:FG=1; H_WISE_SIDS=61027_61682_62130_62168_62230_62136_62327_62340_62346_62328_62371; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; lastIdentity=PassUserIdentity; __cas__st__=NLI; __cas__id__=0; Hm_lvt_912efd4e2e75ff91305c5ebd0114ff98=1741149537; HMACCOUNT=7ABC0ABB0BFAEFDC; BDUSS=nZNa3ItQ0t6aEVMZHhZQUhlSFQ4cW00bnVXWmVCVGM1cG45NEZnTGN-YWVZdTluRUFBQUFBJCQAAAAAAAAAAAEAAACzlAeZQmFpeGluZzE4MDYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJ7Vx2ee1cdnb; BDUSS_BFESS=nZNa3ItQ0t6aEVMZHhZQUhlSFQ4cW00bnVXWmVCVGM1cG45NEZnTGN-YWVZdTluRUFBQUFBJCQAAAAAAAAAAAEAAACzlAeZQmFpeGluZzE4MDYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJ7Vx2ee1cdnb; XFT=nExH8A+pMwjiELSX0C1H5wUKqpWfgV2PennPdq7bPwE=; __cas__rn=0; BAIDUID_BFESS=9BD1631F2A64AD6A4C0EF448323A7F36:SL=0:NR=10:FG=1; BCLID=8212237013907198784; BCLID_BFESS=8212237013907198784; BDSFRCVID=N30OJeC62mDoUjJJvcMZ-qtAs2_6HqbTH6aovTgXxx4ouOUOyXvtEG0Pux8g0Kuhame0ogKK0mOTHUkF_2uxOjjg8UtVJeC6EG0Ptf8g0x5; BDSFRCVID_BFESS=N30OJeC62mDoUjJJvcMZ-qtAs2_6HqbTH6aovTgXxx4ouOUOyXvtEG0Pux8g0Kuhame0ogKK0mOTHUkF_2uxOjjg8UtVJeC6EG0Ptf8g0x5; H_BDCLCKID_SF=JnPHVIP-JCI3D-5vbR__KPkeK2Ta54cO2CoMsJO8fhjCMh7_bf--Dx-jMqQPJMTqK2Djs4j2048K_IQSKt5xy5K_hpQK-hOlLCTxa4_bBlKKJbQHQT3mjbvbbN3i-xrwb25lWb3cWKJV8UbS3tRPBTD02-nBat-OQ6npaJ5nJq5nhMJmb67JDbv0eG_qqTDJtJPfV-OSa-t_ej6P-trWMtCsqxby26nu-g39aJ5nJDoVshn-Xl5k54tIj2cD-UoeJG5qoUFKQpP-HJAwWM7YKpLuDM4jaxR8yNTGKl0MLP5Wbb0xynos-tu8DMnMBMPjamOnaU5o3fAKftnOM46JehL3346-35543bRTLnLy5KJWMDFmj5KWe5j0eHRQ-4Rhb4oeBn7MHJoHjtnYh4t_-P6M0qQCWMT-0bFHKbRV-xK5O4QnXjuVKJ0FKN5dtfvDKHn7_JjO-RjbVhQhbfJzK6tIQH5OKfQxtN4JXInjtpvh8qr6yfjobUPUDMc9LUvP22cdot5yBbc8eIna5hjkbfJBQttjQn3hfIkjXIKLJCLWhC-4j5t3KPkeK2T-e4jK26b0WJ08Kb7VbpuRDMnkbfJBDxcR2hQBWeQq3h6uH4jMEt84BTj1KtD7yajK2b5n5abOXIbObl7l8PTy5ROpQT8r5qAOK5OibCbKWRKMab3vOIJzXpO13tPzBN5thURB2DkO-4bCWJ5TMl5jDh3Mb6ksDhAtqtJHKbDqoC0aJfK; H_BDCLCKID_SF_BFESS=JnPHVIP-JCI3D-5vbR__KPkeK2Ta54cO2CoMsJO8fhjCMh7_bf--Dx-jMqQPJMTqK2Djs4j2048K_IQSKt5xy5K_hpQK-hOlLCTxa4_bBlKKJbQHQT3mjbvbbN3i-xrwb25lWb3cWKJV8UbS3tRPBTD02-nBat-OQ6npaJ5nJq5nhMJmb67JDbv0eG_qqTDJtJPfV-OSa-t_ej6P-trWMtCsqxby26nu-g39aJ5nJDoVshn-Xl5k54tIj2cD-UoeJG5qoUFKQpP-HJAwWM7YKpLuDM4jaxR8yNTGKl0MLP5Wbb0xynos-tu8DMnMBMPjamOnaU5o3fAKftnOM46JehL3346-35543bRTLnLy5KJWMDFmj5KWe5j0eHRQ-4Rhb4oeBn7MHJoHjtnYh4t_-P6M0qQCWMT-0bFHKbRV-xK5O4QnXjuVKJ0FKN5dtfvDKHn7_JjO-RjbVhQhbfJzK6tIQH5OKfQxtN4JXInjtpvh8qr6yfjobUPUDMc9LUvP22cdot5yBbc8eIna5hjkbfJBQttjQn3hfIkjXIKLJCLWhC-4j5t3KPkeK2T-e4jK26b0WJ08Kb7VbpuRDMnkbfJBDxcR2hQBWeQq3h6uH4jMEt84BTj1KtD7yajK2b5n5abOXIbObl7l8PTy5ROpQT8r5qAOK5OibCbKWRKMab3vOIJzXpO13tPzBN5thURB2DkO-4bCWJ5TMl5jDh3Mb6ksDhAtqtJHKbDqoC0aJfK; BA_HECTOR=8g0k2105a10hag0hal0l0h8l2m2trb1jsfrae1v; ZFY=ej1aiGfu5PLrSRu:APDozj2mgqsqRqAGvu:AP2yibUvS8:C; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=2; delPer=0; XFI=c51685e0-f98c-11ef-b48c-b1277f286d56; XFCS=6BADA4584C810E3F62250FDC31942C5A56438223ABDF9C0E6C1A4A186407E92E; __bid_n=1948269c0f54944678fab1; H_PS_PSSID=61027_61682_62168_62230_62136_62327_62340_62346_62328_62371_62421_62423; PHPSESSID=5gopfrlkcb72iqcoqf6017uus6; JSESSIONID=VDQznXYjrfbLuiEpC4mgbHgpBYu6NkKTbDuwMqM1; RT="z=1&dm=baidu.com&si=36462899-dc81-4b4e-a055-3f7acbd7ace0&ss=m7vlf32j&sl=y&tt=ql6&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=5h3v8"; SITEMAPZHITONGEXPIRE=1; Hm_lpvt_912efd4e2e75ff91305c5ebd0114ff98=1741168908; ab_sr=1.0.1_M2U1OGI2YmY5OTM1YzU2YjM4ZjM2YTRjOTdlZDg1NTI0MGFjOWNlZmNjZTk1NzU2NDg3ZGYzOTAwZmViMmMwNjJjYzhiMjFmMjA0NThmMDZlNzU4OGNiOWU4YjBhYmI4ZGZkYzA0YWYzYzk5MjA3OGQ4ZGIyZjdjYTU0ZWY3ODJmNjliOTQ0YzUxNDJlNDhjMWVkMDliZjliODJhOGViZDg2ODVkYzVhYjFkNTIwY2ZjMTFkMWEzOWJjMTY4ZjIz; SITEMAPZHITONG={"data":"ab252c71341c3b04c15924c3d3882b0c96c8741215fcc832a058d78921400a387aee5647302fbd82ee7d5d02bd41b7ff5493d322a455f0c05324e06cb92420a8ed43e1c9be1f212ce70444e99739cef835981e40b3c1f4c1817753aa25b09343dee8ae629c1a4b713b22a84973c58fb8a83683f506c5278f71f7595f47e7f8409fbd8addc7e5709a79e90503b7f11f05c1e478059f76914c43c20a7ac1fa11ce830747eb42c26431a39d141c1d38d0bdad30743afaf942dfb49b699c4e6454cad4d6f459fdacecda7a6fac3f566c753d97c0c93b96cc657e0d99fd22e15fc7c93cb60a9e054c51769827599eff2891f24c4b3708cd8ab37e251783a3a80377f04e63f6b148618b404767e8b680c0d355a361f196624d7dd00cd4467d731c8d9bf7938e48e91ceca9823d9a615ed56f7c055f445b442a4e1f375e8db6fcf6cdf90059c9aff75589c6a8dafc3b036153ed5c45a1e4ec80fa5e60fcadc2597ada72590f3dec515246e883a3a2e334e97e1a","key_id":"32","sign":"e5c2cd7f"}; BAIDUID=2F6CB9E7FD17A3039DB0526638F0983E:FG=1; BAIDUID_BFESS=2F6CB9E7FD17A3039DB0526638F0983E:FG=1'
}

def get_robots_analysis(city):
    """获取指定城市的robots分析数据"""
    url = f"https://ziyuan.baidu.com/robots/doanalysis?site=https%3A%2F%2F{city}.baixing.com&act=&tid="
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 检查请求是否成功
        return response.json()
    except Exception as e:
        print(f"获取 {city} 数据失败: {str(e)}")
        return None

def load_existing_data():
    """加载已存在的数据"""
    file_path = "robots_analysis_results/robots_analysis.xlsx"
    if os.path.exists(file_path):
        try:
            df = pd.read_excel(file_path)
            # 将city和status列的数据转换为字典，方便查询
            return {row['city']: row['status'] for _, row in df.iterrows()}
        except Exception as e:
            print(f"读取已存在数据失败: {str(e)}")
    return {}

def main():
    # 加载已存在的数据
    existing_data = load_existing_data()
    
    # 存储所有城市的结果
    all_results = []
    
    # 如果有已存在的数据，先加载进来
    if os.path.exists("robots_analysis.xlsx"):
        try:
            df_existing = pd.read_excel("robots_analysis.xlsx")
            all_results = df_existing.to_dict('records')
        except Exception as e:
            print(f"加载已存在数据失败: {str(e)}")
    
    # 遍历所有城市
    for i, city in enumerate(CITIES):
        # 检查城市是否已存在且状态为1
        if city in existing_data and existing_data[city] == 1:
            print(f"跳过 {city} - 已存在且状态为1")
            continue
            
        time.sleep(10)
        print(f"正在处理 {city} ({i+1}/{len(CITIES)})...")
        
        result = get_robots_analysis(city)
        if result:
            # 提取需要的数据
            try:
                data = {
                    'city': city,
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'status': result.get('status', ''),
                    'msg': result.get('msg', ''),
                }
                
                # 如果有详细数据，添加到结果中
                if 'data' in result:
                    data.update({
                        'total': result['data'].get('total', 0),
                        'allowed': result['data'].get('allowed', 0),
                        'disallowed': result['data'].get('disallowed', 0)
                    })
                
                # 如果城市已存在，更新数据而不是添加新记录
                existing_index = next((i for i, x in enumerate(all_results) if x['city'] == city), None)
                if existing_index is not None:
                    all_results[existing_index] = data
                else:
                    all_results.append(data)
                
                # 每处理10个城市保存一次结果
                if (i + 1) % 10 == 0 or i == len(CITIES) - 1:
                    df = pd.DataFrame(all_results)
                    df.to_excel("robots_analysis.xlsx", index=False)
                    print(f"已保存结果到: robots_analysis.xlsx")
            
            except Exception as e:
                print(f"处理 {city} 数据时出错: {str(e)}")
        
        # 添加延时，避免请求过于频繁
        time.sleep(2)

    # 最后保存一次
    df = pd.DataFrame(all_results)
    df.to_excel("robots_analysis.xlsx", index=False)
    print("所有城市处理完成！")

if __name__ == "__main__":
    main() 