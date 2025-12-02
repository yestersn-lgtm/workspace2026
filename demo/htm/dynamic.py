import requests

def demo1():
    url = "https://zyk.icve.com.cn/prod-api/website/course/list"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
    }
    params = {
        "sort": "create_time",
        "pageNum": 1,
        "pageSize": 15,
        "keyword": "数据"
    }
    
    response = requests.get(url, headers=header, params=params)

    dict_data = response.json()
    print(f"Data Type: {type(dict_data)}", end="\n\n")
    print(f"Data Content: {dict_data}", end="\n\n")
    
    for dic in dict_data['rows']:
        print(f"Course Name: {dic['name']}, Teacher Name: {dic['userName']}")    
    print("Request completed.")

    with open("demo/htm/zyk_courses.json", "w", encoding="utf-8") as file:
        file.write(response.text)
        print("Page content written to demo/htm/zyk_courses.json")

def demo2():
    url = "https://zyk.icve.com.cn/prod-api/website/course/list"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
    }
    params = {
        "sort": "create_time",
        "pageNum": None,
        "pageSize": 15,
        "keyword": "数据"
    }
    for page in range(1, 4):
        params['pageNum'] = page
        response = requests.get(url, headers=header, params=params)
        dict_data = response.json()
        print(f"Data Type: {type(dict_data)}", dict_data, end="\n\n")
        print(f"--- Page {page} ---")
        for dic in dict_data['rows']:
            print(f"Course Name: {dic['name']}, Teacher Name: {dic['userName']}")
        print(end="\n\n")
    print("All requests completed.")

if __name__ == "__main__":
    # demo1()
    demo2()