import requests
head = { #存放需要伪装的头信息
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
#post请求的请求参数
data = {
    "cname": "",
    "pid": "",
    "keyword": "天津",
    "pageIndex": "1",
    "pageSize": "10",
}
#在抓包工具中：Form Data存放的是post请求的请求参数，而Query String中存放的是get请求的请求参数
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
#在post请求中，处理请求参数的是data这个参数不是params
response = requests.post(url=url,headers=head,data=data)
#将响应数据进行反序列化
page_text = response.json()
for dic in page_text['Table1']:
    name = dic['storeName']
    addr = dic['addressDetail']
    print(name,addr)