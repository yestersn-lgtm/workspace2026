import requests
# 1. 指定服务器的URL
url = 'https://www.eastmoney.com/'

# 2. 发送请求:根据指定的url发送get请求，得到响应对象
response = requests.get(url)

# 查看响应状态码
# print(f'响应状态码：{response.status_code}')

# 3. 获取响应数据
data_str = response.text  # text 字符串形式的响应数据【html响应文件】
# print(type(data_str))
# print(data_str)

# 4. 持久化存储
with open('caifu.html',mode='w',encoding='utf-8') as f:
    f.write(data_str)
print('数据爬取结束！')
