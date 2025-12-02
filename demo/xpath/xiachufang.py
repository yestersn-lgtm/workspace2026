import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}

title = input("please input the recipe title you want to search: ")

params = {
    "keyword": title,
    "cat": "1001"
}

url = "https://www.xiachufang.com/search/"

response = requests.get(url=url, headers=headers, params=params)
response.encoding = 'utf-8'

page_txt = response.text
print(f"Data Type: {type(page_txt)}")

file_name = f"demo/xpath/{title}.html"
with open(file_name, "w", encoding="utf-8") as file:
    file.write(page_txt)
    print(f"Page content written to {file_name}")