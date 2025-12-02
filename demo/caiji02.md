## 东方财富首页数据采集
 
- https://www.eastmoney.com/
 
- ```python
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
  print('数据采集结束！')
  ```
 
​     发现：采集的页面数据出现了中文乱码。
 
## 中文乱码解决
 
- ```python
  import requests
  # 1. 指定服务器的URL
  url = 'https://www.eastmoney.com/'
   
  # 2. 发送请求:根据指定的url发送get请求，得到响应对象
  response = requests.get(url)
   
  # 查看响应状态码
  # print(f'响应状态码：{response.status_code}')
   
  # 设置响应数据的编码格式
  response.encoding = 'utf-8'  # gbk
   
  # 3. 获取响应数据
  data_str = response.text  # text 字符串形式的响应数据【html响应文件】
  # print(type(data_str))
  # print(data_str)
   
  # 4. 持久化存储
  with open('caifu.html',mode='w',encoding='utf-8') as f:
      f.write(data_str)
  print('数据采集结束！')
  ```
 
​   注意：
 
​   如果，以后我们采集的数据出现乱码情况了，尝试两种代码：
 
```
# 设置响应数据的编码格式
response.encoding = 'utf-8'
response.encoding = 'gbk'
```
 
 
 
## 采集51游戏中任何游戏对应的搜索结果页面数据
 
- url：https://www.51.com/
 
- ```python
  import requests
   
  game_title = input('请输入游戏名的关键字：')
   
  # 字典类型承载携带的所有请求参数
  p = {
      'q': game_title,
  }
  # 制定url
  url = 'https://game.51.com/search/action/game/'
   
  # 发送携带请求参数的get请求
  response = requests.get(url,params=p)
   
  # 获取响应数据
  page_html = response.text
   
  # 持久化存储
  with open(f'{game_title}.html',mode='w',encoding='utf-8') as f1:
      f1.write(page_html)
   
  print('数据采集完毕！！！')
  ```
 
## 中国人事考试网（UA检测）
 
- url：http://www.cpta.com.cn/
 
  - 爬虫模拟浏览器主要是模拟请求参数和主要的请求头。
    - User-Agent:请求载体的身份标识。
      - 使用浏览器发请求，则请求载体就是浏览器
      - 使用爬虫程序发请求，则请求载体就是爬虫程序
  - 反爬机制：UA检测
    - 网站后台会检测请求的载体是不是浏览器，如果是则返回正常数据，不是则返回错误数据。
  - 反反爬机制：UA伪装
    - 将爬虫发起请求的User-Agent伪装成浏览器的身份。
 
- ```python
  import requests
   
  url = 'http://www.cpta.com.cn/'
   
  #User-Agent:请求载体（浏览器，爬虫程序）的身份表示
  header = {
      'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
  }
  #伪装了浏览器的请求头
  response = requests.get(url=url,headers=header)
   
  page_text = response.text
   
  with open('kaoshi.html','w') as fp:
      fp.write(page_text)
   
  #程序模拟浏览器的力度不够
  ```
 
## 中国人事考试网---站内搜索（post请求+请求参数）
 
- ```python
  import requests
  url = 'http://www.cpta.com.cn/category/search'
  param = {
      "keywords": "人力资源",
      "搜 索": "搜 索"
  }
  header = {
      'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
  }
  #发起了post请求：通过data参数携带了请求参数
  response = requests.post(url=url,data=param,headers=header)
   
  page_text = response.text
   
  with open('renshi.html','w') as fp:
      fp.write(page_text)
   
  #通过抓包工具定位了指定的数据包：
      #提取：url，请求方式，请求参数，请求头信息
  ```
 
   
 
## 智慧职教（动态加载数据采集）**(重点)**
 
- 抓取智慧职教官网中课程板块下的所有课程数据
 
  - url : https://zyk.icve.com.cn/course
 
- 测试：直接使用浏览器地址栏中的url，进行请求发送查看是否可以采集到数据？
 
  - 不用写程序，基于抓包工具测试观察即可。
 
- 经过测试发现，我们采集到的数据并没有包含想要的数据，why？
 
- 动态加载数据：
 
  - 在一个网页中看到的数据，并不一定是通过浏览器地址栏中的url发起请求请求到的。如果请求不到，一定是基于其他的请求请求到的数据。
 
    ```
    动态请求数据两种情况：
    1. 请求数据包中，没有与当前页面url一致的请求数据包。
    2. 请求数据包中，有与当前页面url一致的请求数据包，但是经过我们的分析响应数据之后，发现，这个数据包没有我们想要采集的数据。
    ```
 
  - 动态加载数据值的就是：
    - 不是直接通过浏览器地址栏的url请求到的数据，这些数据叫做动态加载数据。
     
  - 如何获取动态加载数据？
    - 确定动态加载的数据是基于哪一个数据包请求到的？
    - 数据包数据的全局搜索：
      - 点击抓包工具中任何一个数据包
      - control+f进行全局搜索（弹出全局搜索框）
        - 目的：定位动态加载数据是在哪一个数据包中
      - 定位到动态加载数据对应的数据包，模拟该数据包进行请求发送即可：
        - 从数据包中提取出：
          - url
          - 请求参数   
 
  **注意：请求头中需要携带Referer。（体现模拟浏览器的力度）**
 
- ```python
  import requests
   
  url = 'https://zyk.icve.com.cn/prod-api/website/course/list'
   
  headers = {
      "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
  }
   
  # 请求参数
  params = {
      "sort": "create_time",
      "pageNum": 1,
      "pageSize": 15,
      "keyWord": "数据"
  }
   
  response = requests.get(url, headers=headers,params=params)
   
  dict_data = response.json()  # json类型的响应数据
  # print(type(dict_data), dict_data)
   
   
  for dic in dict_data['rows']:
      print(f'课程名称：{dic["name"]}, 老师姓名：{dic["userName"]}')
   
  print('采集数据成功！')
  ```
   
  ```python
  import requests
   
  url = 'https://zyk.icve.com.cn/prod-api/website/course/list'
   
  headers = {
      "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
  }
   
  # 请求参数
  params = {
      "sort": "create_time",
      "pageNum": None,
      "pageSize": 15,
      "keyWord": "数据"
  }
   
  for page in range(1,4):  # 采集前三页的数据
      params['pageNum'] = page
   
      response = requests.get(url, headers=headers,params=params)
   
      dict_data = response.json()
      # print(type(dict_data), dict_data)
   
      for dic in dict_data['rows']:
          print(f'课程名称：{dic["name"]}, 老师姓名：{dic["userName"]}')
   
   
      print('采集数据成功！')
  ```
 
## 图片数据采集
 
图片，视频，音频，压缩包，这些都是二进制的响应数据，response.content方法。
 
- ```python
  #方式1：
  import requests
  url = 'https://img0.baidu.com/it/u=540025525,3089532369&fm=253&fmt=auto&app=138&f=JPEG?w=889&h=500'
  response = requests.get(url=url)
  #content获取二进制形式的响应数据
  img_data = response.content
  with open('1.jpg','wb') as fp:
      fp.write(img_data)
  ```
 
- ```python
  #方式2
  from urllib.request import urlretrieve
  #图片地址
  img_url = 'https://img0.baidu.com/it/u=4271728134,3217174685&fm=253&fmt=auto&app=138&f=JPEG?w=400&h=500'
  #参数1：图片地址
  #参数2：图片存储路径
  #urlretrieve可以根据图片地址将图片数据请求到直接存储到参数2表示的图片存储路径中
  urlretrieve(img_url,'1.jpg')
  ```
   
- 采集图片的时候需要做UA伪装使用方式1，否则使用方式2
 
 
 
##
 
小试牛刀：
 
- url：https://www.xiachufang.com/
- 实现采集下厨房网站中任意菜谱搜索结果数据采集
 
小试牛刀：
 
- url ：https://sogou.com/
- 采集任意关键字对应的搜索页面
 
肯德基（POST请求、动态加载数据、UA检测）
 
- http://www.kfc.com.cn/kfccda/storelist/index.aspx
 
  - 将餐厅的位置信息进行数据采集
 
 
 
总结：
 
1. 定义url
    定义头部部分键值对  UA  referer 
    携带参数 字典形式
 
2. 发送get post 请求 请求数据
 
3. 获取响应数据
    响应数据content-type:html文件                                 response.text
    响应数据content-type:json[字典，列表数据]         response.json()
    响应数据其他【图片，视频，音频，安装包等】               response.content
     
4.持久化存储
 
    动态加载数据