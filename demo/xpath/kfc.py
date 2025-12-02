import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}

data = {"cname": "", "pid": "", "keyword": "广州", "pageIndex": "1", "pageSize": "10"}

url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"

response = requests.post(url=url, headers=headers, data=data)

page_text = response.json()
print(f"Data Type: {type(page_text)}", end="\n\n")
for dic in page_text["Table1"]:
    name = dic["storeName"]
    address = dic["addressDetail"]
    print(f"KFC Store Name: {name}, Address: {address}")
