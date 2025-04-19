#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from datetime import datetime, timedelta

class BaiduTongji:
    def __init__(self):
        # API配置
        self.api_url = 'https://api.baidu.com/json/tongji/v1/ReportService/getData'
        self.headers = {
            'Content-Type': 'application/json',
            'Cookie': 'BAIDUID=2F6CB9E7FD17A3039DB0526638F0983E:FG=1; BAIDUID_BFESS=2F6CB9E7FD17A3039DB0526638F0983E:FG=1'
        }
        self.username = 'Baixing1'
        self.access_token = 'eyJhbGciOiJIUzM4NCJ9.eyJzdWIiOiJhY2MiLCJhdWQiOiLnmb7luqbnu5_orqEiLCJ1aWQiOjMxODM0OTgsImFwcElkIjoiMTNiZDUwNDlhNjc2ZDEwNzM3OTU5OTMyMTAyZWM1NTciLCJpc3MiOiLllYbkuJrlvIDlj5HogIXkuK3lv4MiLCJwbGF0Zm9ybUlkIjoiNDk2MDM0NTk2NTk1ODU2MTc5NCIsImV4cCI6MTc0NzY3MTcyNCwianRpIjoiLTkwOTA2OTUyNzQzODk5NzA5MzMifQ.6_D0hHIlsMFY2Ws2JHWUh4WAXMfydAOnhwwkOZ9JbiLSrJCUriB95AT97QDj43OY'
        self.site_id = '21587738'
        # self.site_id = '8393754' # 原有的


        
    def get_trend_data(self, start_date, end_date):
        """获取趋势数据"""
        payload = {
            "header": {
                "userName": self.username,
                "accessToken": self.access_token
            },
            "body": {
                "site_id": self.site_id,
                "start_date": start_date,
                "end_date": end_date,
                "metrics": "pv_count,visitor_count",
                "method": "overview/getTimeTrendRpt"
            }
        }
        
        print("\n发送API请求:")
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        
        response = self._make_request(payload)
        
        print("\nAPI响应:")
        print(json.dumps(response, indent=2, ensure_ascii=False))
        
        return response
        
    def get_page_data(self, start_date, end_date):
        """获取页面访问数据"""
        payload = {
            "header": {
                "userName": self.username,
                "accessToken": self.access_token
            },
            "body": {
                "site_id": self.site_id,
                "start_date": start_date,
                "end_date": end_date,
                "metrics": "pv_count,outward_count",
                "method": "visit/toppage/a"
            }
        }
        
        print("\n发送页面访问数据API请求:")
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        
        response = self._make_request(payload)
        
        print("\nAPI响应:")
        print(json.dumps(response, indent=2, ensure_ascii=False))
        
        return response
        
    def _make_request(self, payload):
        """发送API请求"""
        try:
            response = requests.post(self.api_url, headers=self.headers, data=json.dumps(payload))
            return response.json()
        except Exception as e:
            print(f"请求失败: {e}")
            return None 