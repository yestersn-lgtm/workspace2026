import requests


def demo1():
    url = "http://www.cpta.com.cn/"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=header)
    page_text = response.text
    print(f"Page Text Type: {type(page_text)}")
    print(f"Page Text Content (first 500 chars): {page_text[:500]}")

    with open("demo/htm/cpta_with_ua.html", "w", encoding="utf-8") as file:
        file.write(page_text)
        print("Page content written to demo/htm/cpta_with_ua.html")
    print("Request completed.")

def demo2():
    url = "http://www.cpta.com.cn/category/search"
    param = {
        "keywords": "人力资源",
        "搜 索": "搜 索"
    }
    header = {
        "User-Agent":  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
    }
    response = requests.post(url, data=param, headers=header)
    page_text = response.text

    with open("demo/htm/cpta_站内搜索.html", "w", encoding="utf-8") as file:
        file.write(page_text)
        print("Page content written to demo/htm/cpta_站内搜索.html")
    print("Request completed.")

if __name__ == "__main__":
    # demo1()
    demo2()