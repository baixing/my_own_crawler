#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify
from datetime import datetime, timedelta
from baidu_tongji_api import BaiduTongji
import json
import argparse

app = Flask(__name__)
tongji = BaiduTongji()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/stats/today')
def get_today_stats():
    today = datetime.now().strftime('%Y%m%d')
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y%m%d')
    
    # 获取今日和昨日数据
    data = tongji.get_trend_data(yesterday, today)
    
    try:
        today_stats = {'pv': 0, 'uv': 0}
        yesterday_stats = {'pv': 0, 'uv': 0}
        
        if data and 'body' in data and 'data' in data['body'] and data['body']['data']:
            result = data['body']['data'][0]['result']
            items = result.get('items', [])
            
            if len(items) >= 2:
                dates = items[0]  # 日期数组
                values = items[1]  # 值数组
                
                # 找到今天和昨天的数据
                for i, date_item in enumerate(dates):
                    date = date_item[0]  # 获取日期字符串
                    if today in date.replace('/', ''):  # 今天的数据
                        today_stats = {
                            'pv': int(values[i][0]),  # pv_count
                            'uv': int(values[i][1])   # visitor_count
                        }
                    elif yesterday in date.replace('/', ''):  # 昨天的数据
                        yesterday_stats = {
                            'pv': int(values[i][0]),  # pv_count
                            'uv': int(values[i][1])   # visitor_count
                        }
        
        return jsonify({
            'success': True,
            'data': {
                **today_stats,
                'yesterday_pv': yesterday_stats['pv'],
                'yesterday_uv': yesterday_stats['uv']
            }
        })
                
    except Exception as e:
        print(f"处理数据时出错: {e}")
        import traceback
        print(traceback.format_exc())
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/stats/trend')
def get_trend_stats():
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)
    data = tongji.get_trend_data(
        start_date.strftime('%Y%m%d'),
        end_date.strftime('%Y%m%d')
    )
    
    try:
        if data and 'body' in data and 'data' in data['body'] and data['body']['data']:
            result = data['body']['data'][0]['result']
            items = result.get('items', [])
            
            if len(items) >= 2:
                dates = [item[0] for item in items[0]]  # 提取日期
                values = items[1]  # 值数组
                
                return jsonify({
                    'success': True,
                    'data': {
                        'dates': dates,
                        'values': values
                    }
                })
        
        return jsonify({
            'success': True,
            'data': {
                'dates': [],
                'values': []
            }
        })
        
    except Exception as e:
        print(f"处理趋势数据时出错: {e}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/stats/pages')
def get_page_stats():
    today = datetime.now().strftime('%Y%m%d')
    
    data = tongji.get_page_data(today, today)
    
    try:
        if data and 'body' in data and 'data' in data['body'] and data['body']['data']:
            result = data['body']['data'][0]['result']
            items = result.get('items', [])
            
            if len(items) >= 2:
                pages = items[0]  # 页面数组
                values = items[1]  # 值数组
                
                # 组合页面数据
                page_data = []
                for i in range(len(pages)):
                    page_info = {
                        'url': pages[i][0]['name'],
                        'pageId': pages[i][0]['pageId'],
                        'pv': int(values[i][0]),
                        'outward': int(values[i][1])
                    }
                    page_data.append(page_info)
                
                # 获取总计数据
                total = result.get('total', 0)
                sum_data = result.get('sum', [[0, 0]])[0]
                
                return jsonify({
                    'success': True,
                    'data': {
                        'total': total,
                        'sum': {
                            'pv': sum_data[0],
                            'outward': sum_data[1]
                        },
                        'pages': page_data
                    }
                })
        
        return jsonify({
            'success': True,
            'data': {
                'total': 0,
                'sum': {
                    'pv': 0,
                    'outward': 0
                },
                'pages': []
            }
        })
        
    except Exception as e:
        print(f"处理页面数据时出错: {e}")
        import traceback
        print(traceback.format_exc())
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='百姓网监控应用')
    parser.add_argument('--port', type=int, default=8081, help='服务端口号')
    args = parser.parse_args()
    app.run(host='0.0.0.0', debug=True, port=args.port) 