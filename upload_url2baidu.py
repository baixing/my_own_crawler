import requests

urls = [
    'http://huaian.baixing.com/ershouqiche/a2362322152.html',
]
api_url = 'http://data.zz.baidu.com/urls?site=https://huaian.baixing.com&token=8cpODGN0LWdMtXij'

# 将URL列表用换行符连接成字符串
post_data = '\n'.join(urls)

# 设置请求头
headers = {
    'Content-Type': 'text/plain'
}

# 发送POST请求
response = requests.post(api_url, data=post_data, headers=headers)

# 输出结果
print(response.text)
