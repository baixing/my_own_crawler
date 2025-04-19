#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify, request, send_file
from datetime import datetime, timedelta, date
from baidu_tongji_api import BaiduTongji
import json
import argparse
import pymysql
from decimal import Decimal
import pandas as pd
import io
import os
import sys

app = Flask(__name__)
tongji = BaiduTongji()

# 读取用户行业数据
INDUSTRY_DATA = {}
try:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, 'fengming_user_industory.json')
    print(f"[DEBUG] 当前目录: {current_dir}")
    print(f"[DEBUG] JSON文件路径: {json_path}")
    print(f"[DEBUG] 文件是否存在: {os.path.exists(json_path)}")
    sys.stdout.flush()
    
    with open(json_path, 'r', encoding='utf-8') as f:
        content = f.read()
        print(f"[DEBUG] 读取到的内容长度: {len(content)} 字节")
        print(f"[DEBUG] 内容前100个字符: {content[:100]}")
        sys.stdout.flush()
        
        INDUSTRY_DATA = json.loads(content)
        print(f"[DEBUG] 成功解析JSON数据")
        print(f"[DEBUG] 数据类型: {type(INDUSTRY_DATA)}")
        print(f"[DEBUG] 行业数据共 {len(INDUSTRY_DATA)} 条记录")
        print(f"[DEBUG] 数据示例: {dict(list(INDUSTRY_DATA.items())[:3])}")
        sys.stdout.flush()
except Exception as e:
    print(f"[ERROR] 加载行业数据失败: {str(e)}")
    print(f"[ERROR] 错误类型: {type(e)}")
    import traceback
    print(f"[ERROR] 详细错误信息: {traceback.format_exc()}")
    sys.stdout.flush()

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        if isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        return super(DecimalEncoder, self).default(obj)

app.json_encoder = DecimalEncoder

# 数据库配置
DB_CONFIG = {
    'host': 'rt-8vb30k6yqyd2t2v94uo.mysql.zhangbei.rds.aliyuncs.com',
    'port': 3306,
    'user': 'cgread',
    'password': 'ILovePepsi',
    'database': 'account',
    'charset': 'utf8mb4'
}

def get_db_connection():
    return pymysql.connect(**DB_CONFIG)

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

@app.route('/api/fengming/query', methods=['POST'])
def fengming_query():
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        types = data.get('types', [])
        date_range = data.get('date_range', '')
        page = data.get('page', 1)
        page_size = 20  # 每页显示20条记录
        
        connection = get_db_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        # 构建用户ID条件
        user_condition = "AND account_id IN (SELECT id FROM account WHERE user_id = %s)" if user_id else ""
        base_params = [user_id] if user_id else []

        # 获取消耗统计
        consumption_sql = """
            SELECT 
                SUM(amount) as total_amount,
                DATE(created_time) as date
            FROM account_log 
            WHERE type IN (4,5) 
            {}
            AND created_time >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)
            GROUP BY DATE(created_time)
            ORDER BY date DESC
        """.format(user_condition)
        
        cursor.execute(consumption_sql, base_params)
        consumption_data = cursor.fetchall()
        
        # 获取充值统计
        recharge_sql = """
            SELECT 
                SUM(amount) as total_amount,
                DATE(created_time) as date
            FROM account_log 
            WHERE type = 0 
            {}
            AND created_time >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)
            GROUP BY DATE(created_time)
            ORDER BY date DESC
        """.format(user_condition)
        
        cursor.execute(recharge_sql, base_params)
        recharge_data = cursor.fetchall()
        
        # 处理消耗统计数据
        today = datetime.now().date()
        yesterday = today - timedelta(days=1)
        week_ago = today - timedelta(days=7)
        month_ago = today - timedelta(days=30)
        
        consumption_stats = {
            'today': 0,
            'yesterday': 0,
            'last_7_days': 0,
            'last_30_days': 0
        }
        
        recharge_stats = {
            'today': 0,
            'yesterday': 0,
            'last_7_days': 0,
            'last_30_days': 0
        }
        
        for record in consumption_data:
            amount = float(record['total_amount'] or 0)
            date = record['date']
            
            if date == today:
                consumption_stats['today'] = amount
            elif date == yesterday:
                consumption_stats['yesterday'] = amount
                
            if date >= week_ago:
                consumption_stats['last_7_days'] += amount
            if date >= month_ago:
                consumption_stats['last_30_days'] += amount

        for record in recharge_data:
            amount = float(record['total_amount'] or 0)
            date = record['date']
            
            if date == today:
                recharge_stats['today'] = amount
            elif date == yesterday:
                recharge_stats['yesterday'] = amount
                
            if date >= week_ago:
                recharge_stats['last_7_days'] += amount
            if date >= month_ago:
                recharge_stats['last_30_days'] += amount

        # 获取账户余额信息
        account_info = []
        if user_id:  # 只有在指定用户ID时才获取账户信息
            account_sql = """
                SELECT 
                    type as account_type,
                    amount as history_amount,
                    balance as current_balance,
                    amo_money as history_money,
                    bal_money as current_money
                FROM account 
                WHERE user_id = %s AND type IN (0, 9)
            """
            
            # 获取账户信息
            cursor.execute(account_sql, [user_id])
            account_info = cursor.fetchall()
            
            # 转换Decimal为float
            for account in account_info:
                account['history_amount'] = float(account['history_amount'])
                account['current_balance'] = float(account['current_balance'])
                account['history_money'] = float(account['history_money'])
                account['current_money'] = float(account['current_money'])

        # 构建查询参数列表
        params = base_params.copy()
        
        # 处理类型条件
        type_condition = ""
        if types:
            type_condition = "AND type IN ({})".format(','.join(['%s'] * len(types)))
            params.extend(types)
        
        # 处理日期范围
        date_condition = ""
        if date_range:
            try:
                start_date, end_date = date_range.split(' - ')
                date_condition = "AND DATE(created_time) BETWEEN %s AND %s"
                params.extend([start_date, end_date])
            except:
                pass
        
        # 计算总记录数
        count_sql = f"""
            SELECT COUNT(*) as total
            FROM account_log
            WHERE 1=1
            {user_condition}
            {type_condition}
            {date_condition}
        """
        
        # 查询数据
        query_sql = f"""
            SELECT
                CASE
                    WHEN type = 0 THEN '充值'
                    WHEN type = 1 THEN '退款'
                    WHEN type = 2 THEN '冻结'
                    WHEN type = 3 THEN '解冻'
                    WHEN type = 4 THEN '从冻结消耗'
                    WHEN type = 5 THEN '直接消耗'
                    WHEN type = 6 THEN '从负债消耗'
                    WHEN type = 7 THEN '过期'
                    WHEN type = 8 THEN '负债'
                    ELSE '未知类型'
                END AS type_desc,
                DATE(created_time) AS created_date,
                amount,
                money,
                (SELECT user_id FROM account WHERE id = account_log.account_id) as user_id
            FROM account_log
            WHERE 1=1
            {user_condition}
            {type_condition}
            {date_condition}
            ORDER BY created_time DESC
            LIMIT %s, %s
        """
        
        # 获取总记录数
        cursor.execute(count_sql, params)
        total = cursor.fetchone()['total']
        
        # 获取分页数据
        offset = (page - 1) * page_size
        query_params = params + [offset, page_size]
        cursor.execute(query_sql, query_params)
        results = cursor.fetchall()
        
        # 转换Decimal为float并添加行业信息
        for result in results:
            result['amount'] = float(result['amount'])
            result['money'] = float(result['money'])
            result['created_date'] = result['created_date'].strftime('%y-%m-%d')
            
            # 添加行业信息
            user_id = result['user_id']
            if user_id is not None:
                try:
                    user_id_str = str(int(user_id))
                    industry_info = INDUSTRY_DATA.get(user_id_str)
                    
                    # 初始化默认值
                    result['first_category'] = '未知'  # 所属大类
                    result['second_category'] = '未知'  # 细分类目
                    
                    if industry_info:
                        if isinstance(industry_info, dict) and 'first' in industry_info and 'second' in industry_info:
                            result['first_category'] = industry_info['first']  # 所属大类
                            result['second_category'] = industry_info['second']  # 细分类目
                            print(f"[DEBUG] 用户 {user_id} 的行业信息: 所属大类={result['first_category']}, 细分类目={result['second_category']}")
                        else:
                            # 如果是旧格式，两个分类都设置为相同的值
                            result['first_category'] = industry_info
                            result['second_category'] = industry_info
                            print(f"[DEBUG] 用户 {user_id} 使用旧格式行业信息: {industry_info}")
                except Exception as e:
                    print(f"[ERROR] 处理用户 {user_id} 的行业信息时出错: {str(e)}")
                    result['first_category'] = '未知'
                    result['second_category'] = '未知'
            
            sys.stdout.flush()
        
        cursor.close()
        connection.close()
        
        return jsonify({
            'success': True,
            'data': results,
            'account_info': account_info,
            'consumption_stats': consumption_stats,
            'recharge_stats': recharge_stats,
            'total': total,
            'page': page,
            'page_size': page_size
        })
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'success': False, 'message': str(e)})

@app.route('/api/fengming/export', methods=['POST'])
def fengming_export():
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        types = data.get('types', [])
        date_range = data.get('date_range', '')
        
        connection = get_db_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        # 构建用户ID条件
        user_condition = "AND account_id IN (SELECT id FROM account WHERE user_id = %s)" if user_id else ""
        base_params = [user_id] if user_id else []
        
        # 构建查询参数列表
        params = base_params.copy()
        
        # 处理类型条件
        type_condition = ""
        if types:
            type_condition = "AND type IN ({})".format(','.join(['%s'] * len(types)))
            params.extend(types)
        
        # 处理日期范围
        date_condition = ""
        if date_range:
            try:
                start_date, end_date = date_range.split(' - ')
                date_condition = "AND DATE(created_time) BETWEEN %s AND %s"
                params.extend([start_date, end_date])
            except:
                pass
        
        # 查询所有数据（不分页）
        query_sql = f"""
            SELECT
                (SELECT user_id FROM account WHERE id = account_log.account_id) as user_id,
                DATE(created_time) AS created_date,
                amount,
                money,
                CASE
                    WHEN type = 0 THEN '充值'
                    WHEN type = 1 THEN '退款'
                    WHEN type = 2 THEN '冻结'
                    WHEN type = 3 THEN '解冻'
                    WHEN type = 4 THEN '从冻结消耗'
                    WHEN type = 5 THEN '直接消耗'
                    WHEN type = 6 THEN '从负债消耗'
                    WHEN type = 7 THEN '过期'
                    WHEN type = 8 THEN '负债'
                    ELSE '未知类型'
                END AS type_desc
            FROM account_log
            WHERE 1=1
            {user_condition}
            {type_condition}
            {date_condition}
            ORDER BY created_time DESC
        """
        
        cursor.execute(query_sql, params)
        results = cursor.fetchall()
        
        # 转换数据并添加行业信息
        for result in results:
            result['amount'] = float(result['amount'])
            result['money'] = float(result['money'])
            result['created_date'] = result['created_date'].strftime('%Y-%m-%d')
            
            # 添加行业信息
            user_id = result['user_id']
            if user_id is not None:
                try:
                    user_id_str = str(int(user_id))
                    industry_info = INDUSTRY_DATA.get(user_id_str)
                    
                    # 初始化默认值
                    result['first_category'] = '未知'  # 所属大类
                    result['second_category'] = '未知'  # 细分类目
                    
                    if industry_info:
                        if isinstance(industry_info, dict) and 'first' in industry_info and 'second' in industry_info:
                            result['first_category'] = industry_info['first']  # 所属大类
                            result['second_category'] = industry_info['second']  # 细分类目
                            print(f"[DEBUG] 用户 {user_id} 的行业信息: 所属大类={result['first_category']}, 细分类目={result['second_category']}")
                        else:
                            # 如果是旧格式，两个分类都设置为相同的值
                            result['first_category'] = industry_info
                            result['second_category'] = industry_info
                            print(f"[DEBUG] 用户 {user_id} 使用旧格式行业信息: {industry_info}")
                except Exception as e:
                    print(f"[ERROR] 处理用户 {user_id} 的行业信息时出错: {str(e)}")
                    result['first_category'] = '未知'
                    result['second_category'] = '未知'
        
        # 创建DataFrame
        df = pd.DataFrame(results)
        
        # 重命名列并调整顺序
        df = df[['user_id', 'first_category', 'second_category', 'type_desc', 'created_date', 'amount', 'money']]
        df.columns = ['用户ID', '所属大类', '细分类目', '类型', '日期', '金额（分）', '真钱（分）']
        
        # 创建一个字节流
        output = io.BytesIO()
        
        # 将DataFrame写入Excel
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='数据导出')
            
            # 调整列宽
            worksheet = writer.sheets['数据导出']
            for idx, col in enumerate(df.columns):
                max_length = max(df[col].astype(str).apply(len).max(), len(col)) + 2
                worksheet.column_dimensions[chr(65 + idx)].width = max_length
        
        output.seek(0)
        
        # 生成文件名
        filename = f"fengming_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        
        return send_file(
            output,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            as_attachment=True,
            download_name=filename
        )
        
    except Exception as e:
        print(f"Export Error: {str(e)}")
        return jsonify({'success': False, 'message': str(e)})

@app.route('/api/fengming/count', methods=['POST'])
def fengming_count():
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        types = data.get('types', [])
        date_range = data.get('date_range', '')
        
        connection = get_db_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        # 构建用户ID条件
        user_condition = "AND account_id IN (SELECT id FROM account WHERE user_id = %s)" if user_id else ""
        base_params = [user_id] if user_id else []
        
        # 构建查询参数列表
        params = base_params.copy()
        
        # 处理类型条件
        type_condition = ""
        if types:
            type_condition = "AND type IN ({})".format(','.join(['%s'] * len(types)))
            params.extend(types)
        
        # 处理日期范围
        date_condition = ""
        if date_range:
            try:
                start_date, end_date = date_range.split(' - ')
                date_condition = "AND DATE(created_time) BETWEEN %s AND %s"
                params.extend([start_date, end_date])
            except:
                pass
        
        # 计算总记录数
        count_sql = f"""
            SELECT COUNT(*) as total
            FROM account_log
            WHERE 1=1
            {user_condition}
            {type_condition}
            {date_condition}
        """
        
        cursor.execute(count_sql, params)
        total = cursor.fetchone()['total']
        
        cursor.close()
        connection.close()
        
        return jsonify({
            'success': True,
            'count': total
        })
        
    except Exception as e:
        print(f"Count Error: {str(e)}")
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='百姓网监控应用')
    parser.add_argument('--port', type=int, default=8081, help='服务端口号')
    args = parser.parse_args()
    app.run(host='0.0.0.0', debug=True, port=args.port) 